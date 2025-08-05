---
tags:
  - compte-rendu
Début période: 2025-07-01
Fin de période: 2025-07-31
---

## 30 Juillet 2025 - Mercredi

Ajout de couleurs uniques par identifiant dans les tracés ByteTrack.  
Correction de la méthode `from_matplotlib` dans la classe `ColorPalette` pour permettre la génération d’une palette de couleurs distinctes.  Génération de plusieurs versions vidéo avec fond modifiable et export JSON.  Je me suis rendu compte que tous les depuis le début des essais, ByteTrack et DeepSORT, je lançais le script sur la vidéo avec les bbox de YOLO plutôt que sur l'originale améliorée. Ce qui change considérablement les résultats. Il est donc nécessaire de re-procéder aux évaluations des hypers-paramètres. . 


## 29 Juillet 2025 - Mardi

Tests approfondis avec ByteTrack. Génération des vidéos ByteTrack1 à ByteTrack10 avec ajustements progressifs des paramètres (track threshold, lost buffer, matching threshold).  
Ajout d’un compteur d’individus et fonction label mode.  
Identification d'une erreur de test : les vidéos d’inférence contenaient déjà des boîtes, faussant les suivis.


## 28 Juillet 2025 - Lundi

Derniers essais avec DeepSORT sur plusieurs variantes (DeepSORT2 à DeepSORT7).  Modifications du filtre de Kalman dans la bibliothèque pour réduire sa confiance.  
Passage à ByteTrack après des résultats insatisfaisants avec DeepSORT.


## 25 Juillet 2025 - Vendredi

Intégration de plusieurs scripts de tracking (yolo_detection_tracking.py, detector.py, ToutEnUn.py).  
Étude comparative des trackers de différents dépôts. Première implémentation complète de DeepSORT.  Constat d’une inefficacité du suivi, probablement à cause d’un mauvais appariement d’objets.


## 24 Juillet 2025 - Jeudi

Relecture complète de l’ébauche du rapport. Finalisation de la version 1 à envoyer à Guillaume et FDR.


## 23 Juillet 2025 - Mercredi

Construction de l’arborescence LaTeX pour la rédaction finale.  
Rédaction de notes préliminaires sur DeepSORT. Import des textes existants dans Obsidian. Préparation à la soumission du rapport en formats Word et PDF.


## 22 Juillet 2025 - Mardi

Inférence vidéo (15 secondes, zone faible densité) avec Best015.pt.  
Création d’un GIF pour illustrer le résultat. Problèmes d’affichage des images corrigés après mise à jour d’Obsidian. Amélioration de la lisibilité des résultats en supprimant les labels gênants.


## 21 Juillet 2025 - Lundi

Import des sections déjà rédigées dans Obsidian. Rédaction du chapitre 4 et de l’abstract du rapport. Préparation d’un rendez-vous avec Guillaume.


## 17 Juillet 2025 - Jeudi

Participation à une réunion LostInZoom. Rédaction du retour d’expérience avec un membre de la famille.


## 16 Juillet 2025 - Mercredi

Poursuite de l’Ablation Study. Consolidation des résultats des différentes configurations YOLOv10.


## 15 Juillet 2025 - Mardi

Génération des graphes et matrices de corrélation dans Benchmark.ods. Confirmation du rendez-vous avec Guillaume.  
Organisation des fichiers dans Obsidian.


## 11 Juillet 2025 - Vendredi

Finalisation des entraînements (train14 à train18). Migration du dossier Results vers la machine locale. Derniers commits avant le passage à distance. To do list rédigée pour télétravail.

Problème de mémoire GPU avec CUDA (train14), probablement causé par un batch size trop élevé.


## 10 Juillet 2025 - Jeudi

Débogage du script YOLOBenchmark.py. Reprise du benchmark avec les fichiers `.txt` pour corriger les erreurs d’appariement. Lancement de tous les entraînements planifiés sur les datasets 1 à 3. Remplissage du tableau Benchmark.ods.

Problèmes rencontrés :
- Absence de fichier de prédiction lorsque rien n’est détecté
- Erreur de format entraînant un taux d’appariement nul


## 09 Juillet 2025 - Mercredi

Finalisation de l’annotation de l’image vérité, validée par Guillaume.  
Amélioration du script de benchmark, notamment sur le traitement des formats dataset/label.  
Lancement des premiers entraînements sur le dataset 1.

---

Souhaites-tu une version exportable (PDF, DOCX ou autre) ou une version synthétique à côté ?

## 08 Juillet 2025 - Mardi

Détails: [[08-07-2025]]

Réunion avec Guillaume en début de journée. Poursuite de l’annotation de l’image vérité sur Robotflow.  
Le script de benchmark a été amélioré avec l’ajout de l’affichage du score F1. La documentation du projet a également été mise à jour.


## 07 Juillet 2025 - Lundi

Détails: [[07-07-2025]]

Début de l’annotation de l’image vérité sur Robotflow. Génération de l’image à partir du script `YOLOBenchmark.py`.  
Mise en place du script d’évaluation et finalisation du fichier ablation study. Une réunion avec Guillaume a été programmée pour la suite.


## 04 Juillet 2025 - Vendredi

Détails: [[04-07-2025]]

Création du score d'évaluation du modèle YOLOv10. 

## 03 Juillet 2025 - Jeudi

Détails: [[03-07-2025]]

Finalisation de la présentation pour l’entretien avec FJ Richard. Réunion importante avec lui dans la journée, qui a permis de confirmer la direction à suivre : le pipeline Esteban.  
Participation également à une réunion "LostInZoom" où une tâche a été attribuée : faire tester l’expérience à des membres de la famille.


## 02 Juillet 2025 - Mercredi

Détails: [[02-07-2025]]

Réunion avec Guillaume. Lancement d'une inférence sur quelques images : YOUPI, ça fonctionne.  Observation des premiers résultats de détection. 
Préparation de l’entretien avec FJ Richard via un canvas dédié.

## 01 Juillet 2025 - Mardi
Détails: [[01-07-2025]]

Essaie d'inférence du modèle entraîné non aboutis en raison de la version python trop récente du calculateur. Je vais devoir relancer un entrainement du modèle avec python 3.11 ou inférieur. 
Le chapitre 2 du rapport de stage a été terminé. 