---
tags:
  - compte-rendu
Début période: 2025-04-28
Fin de période: 2025-04-30
---
## 30 Avril 2025 - Mercredi
Détails: [[30-04-2025]]

Aujourd’hui, j’ai réussi à faire fonctionner le code de Sylvain après qu’il m’a envoyé quelques précisions. Le problème venait simplement d’un oubli de deux tirets avant l’adresse de la vidéo.  
Cependant, la détection ne fonctionne toujours pas. Cela pourrait être lié à un problème d’installation de bibliothèques ou à la configuration de l’environnement Python. Sylvain m’a recommandé d’utiliser PyCharm ainsi qu’une machine sous Linux.  
En conséquence, le besoin d’un changement de système d’exploitation se confirme. Il serait donc pertinent, dans la mesure du possible, de faire une demande au RSI pour passer ma machine sous Linux avant de la récupérer.

J’ai également eu une visioconférence de plus de deux heures avec Sylvain. Il m’a réexpliqué le projet en détail, a levé les zones d’ombre concernant son programme, et m’a présenté ses objectifs pour le projet ainsi que pour ma mission. Je lui ai ensuite exposé la démarche que je prévois de suivre, qu’il a validée.

Enfin, avant cet échange, j’ai commencé des recherches préliminaires sur YOLOv10.
## 29 Avril 2025 - Mardi
Détails: [[29-04-2025]]

Aujourd'hui, le service informatique m'a installé un écran, un clavier, une souris et un hub.  
J'ai d'abord tenté de lancer le code ce matin sur le PC de la planif, mais ce fut sans succès, puisque ce dernier n'est pas sous Linux. J'ai alors tenté de lancer le programme sur mon PC personnel afin de ne pas perdre de temps dans une nouvelle réinstallation de Git et de VS Code (dans la VM).  
J'ai dû reparamétrer ma clé SSH pour connecter le clone au GitLab.  

En début d'après-midi, il y avait une présentation de la CGT ; par curiosité, j'y suis resté 50 minutes.

Enfin, j'ai tenté toute cette après-midi de lancer le programme de détection sur une vidéo de la BDD, mais ce fut sans succès pour une raison que j'ignore. J'ai d'abord pensé à un problème d'installation de Python (j'avais une version trop récente), j'ai alors réinstallé Python 3.10. Ne fonctionnant toujours pas, j'ai tenté de désinstaller toutes les dépendances (très long) et de les réinstaller le tout deux fois : sans succès non plus.  
Finalement, je ne sais pas pourquoi, mais cela ne fonctionne pas.

A titre indicatif, voici le code que j'ai tenté : 
```bash
wpm detection /mnt/c/Users/esteb/Documents/ESILV/IGN/Data/Videos/Record_2022-6-28_13-9-17_csi0.mp4 --mapping__hive_location_latitude 46.15390619890339 --mapping__hive_location_longitude -0.6890196830553591 --mapping__hive_location_timezone Europe/Paris

wpm detection /mnt/c/Users/esteb/Documents/ESILV/IGN/Data/Videos/Record_2022-6-28_13-9-17_csi0.mp4 46.15390619890339 -0.6890196830553591 Europe/Paris
```
J'obtiens l'erreur suivante : 
```bash
Usage: wpm detection [OPTIONS] FILE_PATH HIVE_LATITUDE HIVE_LONGITUDE
                     HIVE_TIMEZONE
Try 'wpm detection -h' for help.

Error: No such option: --mapping__hive_location_latitude
```


## 28 Avril 2025 - Lundi
Détails: [[28-04-2025]]

J'ai entièrement pris connaissance des articles [[agile-giss-5-24-2024.pdf]] et [[animals-13-01182.pdf]]. J'ai du faire quelques recherches annexes sur certains points particuliers tels que la "waggle dance" ou les "harmonic radiations".  
J'ai également eu l'occasion d'échanger avec Emmanuel après la pause déjeuner sur le fonctionnement des abeilles (au sens biologique). Nous avons abordé leur méthode de reproduction ainsi que le processus principal d'une apiculture.  
Côté GitLab, je n'ai eu le temps que de consulter le code sur l'allumage des LEDs.

Quant à ma compréhension, il reste des zones de flou sur la constitution 3D de la ruche (notamment sur le positionnement des plaques de plexiglas). Je ne suis pas sûr d'avoir bien saisi l'utilité de la "petite rampe" (Fig. 5 [[animals-13-01182.pdf]]), ni d'avoir complètement compris le fonctionnement software de toute la ruche.

Enfin, d'un point de vue administratif et pratique, Laura m'a fait visiter les locaux ce matin et j'ai pu rencontrer le service informatique. Je n'ai malheureusement pas pu récupérer ma machine qui était défectueuse, alors un pc de la "planif" m'a été confié en attendant. 
