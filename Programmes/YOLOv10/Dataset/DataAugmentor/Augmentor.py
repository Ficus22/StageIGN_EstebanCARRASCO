from PIL import Image
import shutil
import os
from tqdm import tqdm

dossier_img = "datasets_RF/GeoDanceHive-BeeDataset-2/train/images"
dossier_label = "datasets_RF/GeoDanceHive-BeeDataset-2/train/labels"
dossier_img_out = "DataAugmentor/train/images"
dossier_label_out = "DataAugmentor/train/labels"


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

    img = Image.open(nom_image)

    for y in range(img.height):
        for x in range(img.width):

            if len(img.getbands()) == 3:
                    r, g, b = img.getpixel( (x,y) )
                    r, g, b = mallow_filtrer(r, g, b)
                    img.putpixel( (x, y), (r,g,b) )

            elif len(img.getbands()) == 4:
                    r, g, b, a = img.getpixel( (x,y) )
                    r, g, b = mallow_filtrer(r, g, b)
                    img.putpixel( (x,y), (r,g,b,a))

    # img.show()
    img.save(f'FM_{nom_image}', fp=dossier_img_out)
    #print(f'FM_{nom_image}')
    return



for image in tqdm(os.listdir(dossier_img), desc="Transformation des images"):
    #print(image)
    img_filter(image)

for label in tqdm(os.listdir(dossier_label), desc="Cpie des labels"):
    label_name = f"FM_{label}"
    shutil.copy(label, os.path.join(dossier_label_out, label_name))