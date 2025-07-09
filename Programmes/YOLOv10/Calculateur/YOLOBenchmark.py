from ultralytics import YOLO
import pandas as pd
import numpy as np
import os
import shutil



# Charge les prédictions du modèle YOLO sur une image et renvoie le dataframe
def load_pred_labels(model_path, image_path, id_num, nb_epochs, nb_batch):
    model = YOLO(model_path, task='detect')
    results = model(image_path)
    results[0].save(f'Results/Result_e{nb_epochs}_b{nb_batch}_t{id_num}/ResultImage_e{nb_epochs}_b{nb_batch}_t{id_num}.jpg', )
    pred_labels = results[0].to_df()  # id | Name | Class | Confidence | Box (tuple)
    return pred_labels



# Charge la verité terrain depuis un fichier label.txt
def load_ground_truth_labels(txt_path):
    df = pd.read_csv(txt_path, sep=' ', header=None, names=['class', 'x_center', 'y_center', 'width', 'height'])
    return df



# Convertit les dataframes en liste de dict (pour match_boxes)
def ground_truth_df_to_labels(df):
    labels = []
    for _, row in df.iterrows():
        bbox = [row['x_center'], row['y_center'], row['width'], row['height']]
        labels.append({
            'class': int(row['class']),
            'bbox': bbox
        })
    return labels


def pred_df_to_labels(df, conf_threshold=0.2):
    labels = []
    for _, row in df.iterrows():
        if row['confidence'] < conf_threshold:
            continue
        box = row['box']
        x1, y1, x2, y2 = box['x1'], box['y1'], box['x2'], box['y2']
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        width = x2 - x1
        height = y2 - y1
        labels.append({
            'class': int(row['class']),
            'bbox': [x_center, y_center, width, height]
        })
    return labels




def bbox_iou(box1, box2):
    def to_corners(box):
        x, y, w, h = box
        return [x - w/2, y - h/2, x + w/2, y + h/2]
    b1 = to_corners(box1)
    b2 = to_corners(box2)
    xi1, yi1 = max(b1[0], b2[0]), max(b1[1], b2[1])
    xi2, yi2 = min(b1[2], b2[2]), min(b1[3], b2[3])
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    b1_area = (b1[2] - b1[0]) * (b1[3] - b1[1])
    b2_area = (b2[2] - b2[0]) * (b2[3] - b2[1])
    union_area = b1_area + b2_area - inter_area
    return inter_area / union_area if union_area > 0 else 0





def match_boxes(gt_labels, pred_labels, iou_thresh=0.5):
    matches = []
    gt_matched = set()
    pred_matched = set()
    for i, gt in enumerate(gt_labels):
        best_iou = 0
        best_j = -1
        for j, pred in enumerate(pred_labels):
            if pred['class'] == gt['class'] and j not in pred_matched:
                iou = bbox_iou(gt['bbox'], pred['bbox'])
                if iou > best_iou:
                    best_iou = iou
                    best_j = j
        if best_iou >= iou_thresh and best_j >= 0:
            matches.append((i, best_j, best_iou))
            gt_matched.add(i)
            pred_matched.add(best_j)
    return matches, gt_matched, pred_matched




def compute_metrics(gt_labels, pred_labels, inference_time_ms):
    n_gt = len(gt_labels)
    n_pred = len(pred_labels)
    matches, gt_matched, pred_matched = match_boxes(gt_labels, pred_labels)
    n_matched = len(matches)
    ious = [iou for _, _, iou in matches]

    # 1. Nombre d'individus détectés (25 points)
    rel_error = abs(n_pred - n_gt) / max(1, n_gt)
    score_count = 25 * (1 - min(rel_error / 0.5, 1))

    # 2. IoU moyen (25 points)
    iou_mean = np.mean(ious) if ious else 0
    score_iou = 25 * (iou_mean - 0.5) / 0.35 if iou_mean >= 0.5 else 0
    score_iou = min(max(score_iou, 0), 25)

    # 3. Précision (10 points)
    precision = n_matched / n_pred if n_pred > 0 else 0
    score_precision = 10 * (precision - 0.7) / 0.25 if precision >= 0.7 else 0
    score_precision = min(max(score_precision, 0), 10)

    # 4. Rappel (10 points)
    recall = n_matched / n_gt if n_gt > 0 else 0
    score_recall = 10 * (recall - 0.7) / 0.25 if recall >= 0.7 else 0
    score_recall = min(max(score_recall, 0), 10)

    # 5. mAP@0.5 (approximation) (10 points)
    ap = n_matched / (n_pred + n_gt - n_matched) if (n_pred + n_gt - n_matched) > 0 else 0
    score_map = 10 * (ap - 0.7) / 0.25 if ap >= 0.7 else 0
    score_map = min(max(score_map, 0), 10)

    # 6. Temps d'inférence (10 points)
    if inference_time_ms < 15:
        score_time = 10
    elif inference_time_ms > 1000:
        score_time = 0
    else:
        score_time = 10 * (1 - (inference_time_ms - 15) / 900)

    # 7. Faux positifs (10 points)
    false_positives = n_pred - len(pred_matched)
    fpr = false_positives / max(1, n_pred)
    if fpr <= 0.05:
        score_fpr = 10
    elif fpr >= 0.3:
        score_fpr = 0
    else:
        score_fpr = 10 * (1 - (fpr - 0.05) / 0.25)

    # Score F1 (Affichage seulement)
    if recall + precision > 0:
        score_f1 = 2 * ((recall * precision) / (recall + precision))
    else:
        score_f1 = 0


    # Score final
    score_total = score_count + score_iou + score_precision + score_recall + score_map + score_time + score_fpr

    details = {
        'score_total': round(score_total, 2),
        'score_count': round(score_count, 2),  
		'score_iou': round(score_iou, 2),  
		'score_precision': round(score_precision, 2),  
		'score_recall': round(score_recall, 2),
        'score_f1': round(score_f1, 2),  
		'score_map': round(score_map, 2),  
		'score_time': round(score_time, 2),  
		'score_fpr': round(score_fpr, 2),  
		'precision': round(precision, 3),  
		'recall': round(recall, 3),  
		'iou_mean': round(iou_mean, 3),  
		'n_gt': n_gt,  
		'n_pred': n_pred,  
		'n_matched': n_matched,  
		'inference_time_ms': inference_time_ms,  
		'false_positives': false_positives,  
		'fpr': round(fpr, 3)  
		}  
    return details



def save_metrics_to_txt(score_details, model_path, nb_epochs, nb_batch, id_num):
    file_name = f"Results/Result_e{nb_epochs}_b{nb_batch}_t{id_num}/ResultsResum_e{nb_epochs}_b{nb_batch}_t{id_num}.txt"
    os.makedirs(f"Results/Result_e{nb_epochs}_b{nb_batch}_t{id_num}", exist_ok=True)

    shutil.copyfile(model_path, f"Results/Result_e{nb_epochs}_b{nb_batch}_t{id_num}/Best00{id_num}.pt")

    with open(file_name, 'w') as f:
        f.write(f"Résultats \n\nepochs={nb_epochs}, batch={nb_batch}, BDD vesrion={bdd_version}, train ID={id_num}\n\n")
        f.write(f"Score global (/100): {score_details['score_total']}\n")
        f.write("---- Détails ----\n")
        f.write(f"Nombre individus (score): {score_details['score_count']}/25\n")
        f.write(f"IoU moyen (score): {score_details['score_iou']}/25 (valeur={score_details['iou_mean']})\n")
        f.write(f"Précision (score): {score_details['score_precision']}/10 (valeur={score_details['precision']})\n")
        f.write(f"Rappel (score): {score_details['score_recall']}/10 (valeur={score_details['recall']})\n")
        f.write(f"Score F1: {score_details['score_f1']}\n")
        f.write(f"mAP@0.5 (score): {score_details['score_map']}/10\n")
        f.write(f"Temps d’inférence (score): {score_details['score_time']}/10 ({score_details['inference_time_ms']} ms)\n")
        f.write(f"Faux positifs (score): {score_details['score_fpr']}/10 (fpr={score_details['fpr']})\n\n")
        f.write("---- Statistiques brutes ----\n")
        f.write(f"Nombre total réels d'individus: {score_details['n_gt']}\n")
        f.write(f"Nombre total détectés d'individus: {score_details['n_pred']}\n")
        f.write(f"Invidus réels détectés: {score_details['n_matched']}\n")
        f.write(f"Faux positifs: {score_details['false_positives']}\n")


#----

image_path = 'Truth/truthImage.jpg'
gt_txt = 'Truth/truthImage.txt'

nb_epochs = 100
nb_batch = 32
bdd_version = 3
train_num = 1

model_path = f'runs/detect/train{train_num}/weights/best.pt'


inference_time_ms = 61.9

gt_labels = ground_truth_df_to_labels(load_ground_truth_labels(gt_txt))
pred_labels = pred_df_to_labels(load_pred_labels(model_path, image_path, train_num, nb_epochs, nb_batch))


score_details = compute_metrics(gt_labels, pred_labels, inference_time_ms)

save_metrics_to_txt(score_details, model_path, nb_epochs, nb_batch, train_num)

print("Score global (/100) :", score_details['score_total'])
print("Détail du score :", score_details)
