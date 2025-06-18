---
tags:
  - "#compte-rendu"
  - "#programme"
Fichier mère: copié/collé du README
Date: 2025-05-05
Objectif: Projet simple de découverte de YOLOv10
---
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
![[IGN-remote/Modèles/YOLOv10/HWP/test.jpg]] 
On obtient le résultat suivant :  
![[resultimage.png]]
  
Ainsi on remarque que la reconnaissance est efficiente et n'a pris que 2s avec le réseau `yolov10n`.  
## HelloWorld Webcam  
Deuxième test avec l'utilisation de la webcam, relativement efficace mais pas fiable. Des erreurs de reconnaissances ont été aperçues. Voici un exemple réussi de la reconnaissance en direct :  
![[IGN-remote/Modèles/YOLOv10/HWP/resultwebcam.png]]