import pandas as pd
import numpy as np

# --- PARAMÈTRES ---
image_width = 1280
image_height = 720
iou_threshold = 0.5

gt_path = "YOLOv10/Calculateur/Debug/truthImage.txt"
pred_path = "YOLOv10/Calculateur/Debug/predImage.txt"


# --- FONCTIONS ---
def bbox_iou(box1, box2):
    def to_corners(box):
        x, y, w, h = box
        return [x - w / 2, y - h / 2, x + w / 2, y + h / 2]
    
    b1 = to_corners(box1)
    b2 = to_corners(box2)

    xi1 = max(b1[0], b2[0])
    yi1 = max(b1[1], b2[1])
    xi2 = min(b1[2], b2[2])
    yi2 = min(b1[3], b2[3])
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)

    b1_area = (b1[2] - b1[0]) * (b1[3] - b1[1])
    b2_area = (b2[2] - b2[0]) * (b2[3] - b2[1])
    union_area = b1_area + b2_area - inter_area
    return inter_area / union_area if union_area > 0 else 0


def load_yolo_labels(path, img_w, img_h):
    df = pd.read_csv(path, sep=' ', header=None, names=['class', 'x_center', 'y_center', 'width', 'height'])
    df['x_center'] *= img_w
    df['y_center'] *= img_h
    df['width'] *= img_w
    df['height'] *= img_h
    return df


def df_to_label_list(df):
    labels = []
    for _, row in df.iterrows():
        labels.append({
            'class': int(row['class']),
            'bbox': [row['x_center'], row['y_center'], row['width'], row['height']]
        })
    return labels


# --- MAIN ---
gt_df = load_yolo_labels(gt_path, image_width, image_height)
pred_df = load_yolo_labels(pred_path, image_width, image_height)

gt_labels = df_to_label_list(gt_df)
pred_labels = df_to_label_list(pred_df)

print(f"GT : {len(gt_labels)} boîtes | PRED : {len(pred_labels)} boîtes")

print("\n--- Matching IoU ---")
match_found = False
for i, gt in enumerate(gt_labels):
    for j, pred in enumerate(pred_labels):
        if gt['class'] == pred['class']:
            iou = bbox_iou(gt['bbox'], pred['bbox'])
            if iou > 0:
                match_found = True
                status = "V" if iou >= iou_threshold else "X"
                print(f"GT[{i}] ↔ Pred[{j}] | class={gt['class']} | IoU = {iou:.3f} {status}")

if not match_found:
    print("! Aucun appariement valide trouvé. Vérifie les classes et les positions.")
