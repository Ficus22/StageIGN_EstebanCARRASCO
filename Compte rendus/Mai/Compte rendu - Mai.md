---
tags:
  - compte-rendu
Début période: 2025-05-05
Fin de période: 2025-05-28
---

## 28 Mai 2025 - Mercredi
Détails: [[28-05-2025]]

En cherchant un quelconque filtre dans les codes de Sylvain, je me suis rendu compte qu'il ne s'en servait a priori pas. Une visio devait être programmée pour que l'on puisse échanger à ce sujet mais n'a pu être réalisée. Ainsi j'ai moi même réalisé un filtre sur des ROI en appliquant des réglages différents et en repartant de l'image originale. Je pense avoir trouvé la combinaison des paramètres la plus optimale relativement aux zones concernées. 


## 27 Mai 2025 - Mardi
Détails: [[27-05-2025]]

Une visio de 1h30 a été réalisé avec Guillaume ce martin. Il a réabordé les filtres qu'utilise Silvain pour réduire le "blanc" sur les frame et m'a relancé sur la découpe d'image annotée (auparavant abandonné).
Le programme est terminé et fonctionnel. Il ne reste plus qu'à déterminer le ratio acceptable pour conserver une bounding box (dans le cadre de nos images).


## 26 Mai 2025 - Lundi
Détails: [[26-05-2025]]

Aujourd'hui, j'ai déterminé la bonne modification colorimétrique à appliquer aux images pour qu'elles ressemblent à nos données. L'algorithme a ensuite été lancé sur les données de validation et d'entraînement.


## 23 Mai 2025 - Vendredi
Détails: [[23-05-2025]]

Des recherches sur le fine tuning ont était réalisées, et plus spécialement sur la façon dont est organisé le fichier de configuration. Le fichier mère YOLO a également été mis à jours. J'ai également compris le fonctionnement et l'utilités des anchor box. Les recherches ont aboutis à une fiche recherche. 


## 21 Mai 2025 - Mercredi
Détails: [[21-05-2025]]

Aujourd'hui, les recherche sur l'augmentation du dataset ont été menée. Ces dernières nous ont amenées à deux possibilités :
- soit faire une augmentation virtuel via YOLO
- soit une réelle augmentation, en copiant et modifiant les photos existantes
Mon attention s'est portée sur cette dernière option. 


## 20 Mai 2025 - Mardi
Détails: [[20-05-2025]]

De nouvelles images ont été annotées aujourd'hui. Et 100 nouvelle frame ont été générées. Un message sur le zulip a été poster pour une demande d'aide de la part de l'équipe. Lors des moments informels, j'ai eu l'occasion d'échanger avec des collègues au sujet du déroulement d'un parcours de recherche. Des recherches sur le fine tuning ont été amorcées. 


## 19 Mai 2025 - Lundi
Détails: [[19-05-2025]]

La conclusion du jour et qu'il faut améliorer le fine tuning et augmenter notre dataset. De ces faits, le modèles sera alors peut être plus performant. Pour se faire je devrais pouvoir utiliser la collaboration de l'équipe ainsi qu'un petit modèle pré entrainé pour nous aider à annoter. 


## 16 Mai 2025 - Vendredi
Détails: [[16-05-2025]]

Journée intense de pars la redondance des actions exécutées. Ce matin j'ai fais un programme qui prend x frames au hasard dans un dossier définit et qui leur applique le même traitement. De cette façon toutes les images ont les mêmes modifications/ J'ai ensuite cette après midi annoté deux images (fatiguant). 


## 14 Mai 2025 - Mercredi
Détails: [[14-05-2025]]

Aujourd'hui, j'ai dessiné une pipeline de traitement d'image, puis je l'ai implémenté en python à l'aide de la bibliothèque OpenCV. J'espère que les traitements des images permettra une meilleure reconnaissance à l'IA. Il ne reste plus qu'à tester !


## 13 Mai 2025 - Mardi
Détails: [[13-05-2025]]

Ca y est, les choses sérieuses ont commencé aujourd'hui ! Les premiers entrainement du modèle ont été effectué, puis tester. Un premier avec un dataset déjà annoté, trouvé sur RF. et un seconde avec ce même dataset et en suppléments deux images issues des vidéos de sylvain et annotées par mes soins. Malheureusement, ces deux modèles se sont montrés inefficaces quant à la détection des abeilles sur le cadre (avec les images de la GDH).

Ce résultat se justifie peut-être par le nombre d'époques ou de bash. A ce stade, je n'en sais encore rien. 


## 12 Mai 2025 - Lundi
Détails: [[12-05-2025]]

La marche générale a été validée lors de la visio avec Guillaume cet après-midi. Je suis donc le pipeline n°5 de YOLOv10 (*cf. toile associée*). Je me focalise d'abord sur la détection primaire soit la détection des abeilles sur le cadre. Pour se faire un dataset déjà annoté a été trouvé sur Robotflow. Je dois lancer de premiers tests dessus afin de savoir, s'il nécessite un fine-tuning supplémentaire. Au besoin, j'aurais accès à une machine de calcul pour entrainer les modèles. Sinon, dans un premier temps GoogleCollab pourrait suffire. 


## 7 Mai 2025 - Mercredi
Détails: [[07-05-2025]]

La quasi entièreté du coffre a été réorganisé pour s'adapter au plus à l'architecture Obsidian. De cette façon, les tags ont été mis à jours et un dossier *Modèles* ainsi que sont contenu ont été crées.
La bibliographie a elle aussi était mise à jour, et a changé de format. Elle est passée de fichier texte à toile. 
Concernant le dilemme de la veille ce dernier a été levé dès le matin. La stratégie à alors été retaillée et a donc aboutie à la creation d'un comparatif de pipelines pour YOLOv10 et DeepLabCut. Une overview de DeepLabCut à partir de la documentation officielle a aussi été réalisé. 


## 6 Mai 2025 - Mardi
Détails: [[06-05-2025]]

La section Pipeline a était ajoutée à la bibliographie. Les recherches sur le dataset ont aboutie à la création de deux document (Format et Adaptation csv) ainsi qu'au soulèvement d'un problème.

Le choix de la pipeline a été perturbé. En effectuant des recherches sur l'état d'art des algorithme de motif vidéo, j'ai trouvé que l'utilisation de YOLOv10 n'était pas la plus adaptée et qu'il existait d'autre pipeline. Parmi elles, on trouve DeepLabCut qui permet de suivre des points sur un ou quelques individus de manière précise. Mais je suis aussi tombé sur DeepWDT, une pipeline développé spécialement pour réaliser les missions que nous cherchons à réaliser. 
La question est donc la suivante : 
- Quel est l'intérêt de redévelopper un programme déjà existant ?
- Une simple adaptation est-elle attendue ? 

Un message a été envoyé à Guillaume : sans réponse. Dans l'attente d'une quelconque consigne spécifique, je vais tenter d'implémenter DeepWDT à notre cas d'étude. Un réentrainement du modèle sur un nouveau dataset sera surement nécessaire. 


## 5 Mai 2025 - Lundi
Détails: [[05-05-2025]]

Aujourd’hui, plusieurs avancées importantes ont été réalisées. Tout d’abord, une prise en main du modèle YOLOv10 a été effectuée à travers une première exploration de ses fonctionnalités. Ensuite, l’environnement de développement a été mis en place avec l’installation de PyCharm, la création d’un environnement virtuel et l’installation des bibliothèques nécessaires, une étape particulièrement longue. Un projet “HelloWorld” a également été lancé pour tester le bon fonctionnement de l’ensemble.

Dans le cadre du suivi scientifique et administratif, un entretien vidéo de deux heures avec Guillaume a permis de faire le point sur les différentes orientations à venir. En parallèle, une To Do List générale a été créée afin de structurer les prochaines étapes, et la bibliographie a été enrichie. Des recherches ont également été amorcées sur le contouring avec YOLOv10.

Cependant, un problème a été rencontré concernant l’environnement de développement : il a fallu réinstaller l’environnement virtuel sur Windows, abandonnant l’usage initial de WSL, ce qui a occasionné une perte de temps.