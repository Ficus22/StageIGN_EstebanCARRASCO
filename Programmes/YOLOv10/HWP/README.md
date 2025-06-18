## Démarrer
Une fois dans à l'adresse suivante : `C:\Users\esteb\Documents\ESILV\IGN\YOLOv10-Test`

Lancer l'environnement virtuel :
```shell
  .\.venv\Scripts\activate
```
### Installation des bibliothèques (très long)
```shell
  pip install torch torchvision ultralytics
```

## HelloWorld Image
Test simple avec une image de chien pour voir si le réseau de neurones reconnait l'image.
![test.jpg](IGN-remote/Programmes/YOLOv10/HWP/ImageTest/test.jpg)
On obtient le résultat suivant :
![result.PNG](result.PNG)

Ainsi on remarque que la reconnaissance est efficiente et n'a pris que 2s avec le réseau `yolov10n`.  

## HelloWorld Webcam
Deuxième test avec l'utilisation de la webcam, relativement efficace mais pas fiable. Des erreurs de reconnaissances ont été aperçues. Voici un exemple réussi de la reconnaissance en dierect :
![resultwebcam.png](IGN-remote/Programmes/YOLOv10/HWP/WebcamTest/resultwebcam.png)
