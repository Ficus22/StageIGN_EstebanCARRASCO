from PIL import Image
import shutil
import os
from tqdm import tqdm

DOSSIER = "valid"

dossier_img = f"datasets_RF/GeoDanceHive-BeeDataset-1/{DOSSIER}/images"
dossier_label = f"datasets_RF/GeoDanceHive-BeeDataset-1/{DOSSIER}/labels"
dossier_img_out = f"DataAugmentor/{DOSSIER}/images"
dossier_label_out = f"DataAugmentor/{DOSSIER}/labels"

os.makedirs(dossier_img_out, exist_ok=True)
os.makedirs(dossier_label_out, exist_ok=True)

def red_filtrer(old_r, old_g, old_b):

    new_r = old_r    # On laisse le rouge
    new_g = old_g // 3    # On diminue le vert
    new_b = old_b // 3    # On diminue le bleu
    return (new_r, new_g, new_b)

def mallow_filtrer(old_r, old_g, old_b):

    new_r = old_r * 1.1
    new_g = old_g // 5
    new_b = old_b * 1.5

    #print(new_r, new_g, new_b)
    return (int(new_r), int(new_g), int(new_b))

def img_filter(nom_image):
    try:
        img = Image.open(nom_image)
        img.load()  # force le chargement complet

        for y in range(img.height):
            for x in range(img.width):
                if len(img.getbands()) == 3:
                    r, g, b = img.getpixel((x, y))
                    r, g, b = mallow_filtrer(r, g, b)
                    img.putpixel((x, y), (r, g, b))

                elif len(img.getbands()) == 4:
                    r, g, b, a = img.getpixel((x, y))
                    r, g, b = mallow_filtrer(r, g, b)
                    img.putpixel((x, y), (r, g, b, a))

        nom_fichier = os.path.basename(nom_image)
        img.save(os.path.join(dossier_img_out, f'FM_{nom_fichier}'))

    except Exception as e:
        print(f"[ERREUR] Échec du traitement de l’image : {nom_image} -> {e}")
 
    # img.show()
    nom_fichier = os.path.basename(nom_image)
    img.save(os.path.join(dossier_img_out, f'FM_{nom_fichier}'))
    #print(f'FM_{nom_image}')
    return



for image in tqdm(os.listdir(dossier_img), desc="Transformation des images"):
    if image.lower().endswith((".jpg", ".jpeg", ".png")):
        chemin_image = os.path.join(dossier_img, image)
        img_filter(chemin_image)


for label in tqdm(os.listdir(dossier_label), desc="Cpie des labels"):
    label_name = f"FM_{label}"
    chemin_label = os.path.join(dossier_label, label)
    shutil.copy(chemin_label, os.path.join(dossier_label_out, label_name))
