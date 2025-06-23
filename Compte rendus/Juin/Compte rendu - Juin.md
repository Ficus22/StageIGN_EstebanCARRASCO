---
tags:
  - compte-rendu
Début période: 2025-06-02
Fin de période: ""
---
## 23 Juin 2025 - Lundi
Détails: [[23-06-2025]]

En voulant achever l'annotation des fichiers je me suis rendu compte que nous avions un problème concernant les zones illisibles sur robot flow (zones cramées). Effectivement même si les abeilles dans ces zones sont méconnaissables, lorsque le changement d'image aura lieu, elles apparaîtront et ne seront pas annoté. Pour régler cela, j'ai récupérer le code source des annotations réalisées et à l'aide d'un script et je l'ai transformé en fichier d'annotation. Pour ensuite les re-uploader sur robot flow et finaliser leur annotation. Il ne reste plus qu'a vérifier que chaque image est complètement annotée. 

## 20 Juin 2025 - Vendredi
Détails: [[20-06-2025]]

La réunion de mi-stage a été réalisé avec Mme Frankart et fut très positive. Aujourd'hui j'ai avancé sur l'amélioration des image modifiées avec CLAHE. Grâce à un sondage sur zulip j'ai pu tranché quand à la transformation la plus efficace (CLAHE + sat + sharp). 


## 18 Juin 2025 - Mercredi
Détails: [[18-06-2025]]

L'entretient vidéo avec Guillaume a permis de trancher sur les prochaines pistes à suivre : je continu sur le suivie individuel des abeilles en tentant de toujours plus améliorer la qualité des images et dans un second temps, en tâche de fond, je peux me pencher sur la reconnaissance des danse depuis les différentiels (et Unet). YOWO quant à lui est mi de côté car surement trop difficile a utiliser sans une annotation spécifique d'une base d donnée. En effet les données terrain contiennent des trous et sont incomplète pour fabriquer algorithmiquement un dataset de qualité pour un YOWO. 

Aujourd'hui malgré quelques complications quant à la connexion de obsidian, git et au passage de pycharm vers code, un premier test très concluant de CLAHE laisse pressentir de bon résultat sur l'amélioration des images.  


## 17 Juin 2025 - Mardi
Détails: [[17-06-2025]]

La majeure partie de la journée a été consacrée à la prise de connaissances et mise en place des rendus du stage. Des recherches sur des modification de contraste dynamique on été amorcées. 


## 06 Juin 2025 - Vendredi
Détails: [[06-06-2025]]

Des recherches préliminaires sur YOWOv3 laissent entendre que l'on pourrait entraîner un tel modèle pour qu'il reconnaisse la danse des abeilles. Néanmoins il a été difficile de comprendre comment ce dernier traitait la donnée. En effet les différents datasets présenté avec le modèle, ne sont pas tous de la même forme. Ainsi, il va falloir déterminer concrètement ce dont a besoin le modèle pour fonctionner, et ainsi pouvoir l’entraîner. Le prochain rdv avec Guillaume me permettra de décider d’entamer de plus profondes recherches sur le sujet ou pas. 


## 04 Juin 2025 - Mercredi
Détails: [[04-06-2025]]

Réunion d'équipe


## 03 Juin 2025 - Mardi
Détails: [[03-06-2025]]

La réunion avec Guillaume et Sylvain ce matin a permis de clarifier la direction que va emprunter mon stage sur les prochaines semaines. 
Je vais donc continuer d'approfondir notre approche initiale qui vise à détecter toutes les abeilles puis à tracer leur trajectoire. Cependant, je vais devoir en plus entamer des recherches sur YOWOv2/v3 et évaluer si ce modèle (en cours de développement) est une approche à considérer et intéressante dans notre cas d'étude. 


## 02 Juin 2025 - Lundi
Détails: [[02-06-2025]]

**Journée télétravaillée**

Une visio avec Sylvain juste après celle avec Guillaume a dessiné une contre direction dans les choix que nous avions entrepris. En effet, Sylvain évoque le fait qu'une détection générale de toutes les abeilles, n'est selon lui, pas la bonne méthode à opter. Une visio demain, en conférence à 3 (avec Guillaume) est nécessaire pour fixer les choix à entreprendre.  