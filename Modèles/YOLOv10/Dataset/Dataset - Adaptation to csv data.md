---
tags:
  - recherches
  - caduc
Date: 2025-05-06
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Réussir à extraire la donnée des csv d'identification des danses
---
## 1. Format de la donnée .csv
Dans le fichier .csv, chaque détection de frétillements constitue une ligne (à l'exception de la première). Dans le fichier `runs-with-coordinates.csv`, on retrouve 3647 lignes (soit 3646 frétillements) qui décrivent 140 danses. Ces détections sont décrit par 18 colones qui donnent des informations relatives :

- Frétillement
	- Frame de départ
	- Cellule de départ
	- Coordonnée sur l'image de départ du centre de l'abeille danseuse
	- Frame de fin
	- Coordonnée sur l'image de fin du centre de l'abeille danseuse
	- Type de détection (linéaire, non linéaire, stoppée, sortie du cadre)
	- Type de déplacement (linéaire ou non linéaire)
	- Clarté (claire, stoppée, hors cadre, hors temps)
- Danse
	- ID de la danse correspondante
	- Angle de danse
	- Date et heure
	- Durée de la danse
- Coordonnée géographique
	- Longitude
	- Latitude
	- Point géographique

Toutes ces données ne sont pas utiles dans le cadre de la création d'un dataset d'entrainement pour YOLOv10. 


## 2. Nettoyage de la donnée .csv
Dans le cadre de la création d'un dataset pour YOLOv10, nous savons (cf. [[Dataset - Format]]) qui nous suffit simplement de connaitre les coordonnées du centre de la bounding box de l'élément à détecter. 