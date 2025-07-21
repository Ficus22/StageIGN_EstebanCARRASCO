---
tags:
  - recherches
  - compte-rendu
Date: 2025-07-15
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Déterminer le modèle le plus performant
aliases:
---
## Introduction
Cette *Ablation study* constitue une étude dont l'objectif est de conclure quant au modèle le plus performant. 
Sur le même calculateur, 18 modèles ont été entrainés avec 4 bases de données différentes et des nombres d'époques et de batch différents. S'il y a bien 4 datasets différents, il ne s'agit ici que de versions améliorées d'un dataset open source constitué de 909 images d'abeilles annotée en 3 classes différentes (bee, queen, drone).

Chaque version de bdd a bénéficier d'au moins 4 entrainements avec son jeu de données. Avant de survoler les résultats obtenus et de plonger dans l'étude à proprement dit, voici la correspondances des différentes version des BDD :

- **version 1 :** dataset open source original
- **version 2 :** ajout de deux images de la GDH annotées
- **version 3 :** duplication du dataset version 2 pour appliquer un filtre de couleur violet au image (sans modification de leurs labels)
- **version 4 :** ajout de plus d'une soixantaines d'images de la GDH annotées

## Méthodologie
### Données et variables suivies
Pour procéder à cette *Ablation study* j'ai réaliser un script de benchmark ayant pour but d'évaluer équitablement les différents modèles entrainés. Dix-huit paramètres et données ont été suivis et reportés sur une feuille de calcul manuellement.

Voici les paramètres en question :
- époques
- batch
- version de la bdd
- nb. d'images
- appareil de calcul
- durée de l'entrainement
- précision 
- rappel
- IuO moyen
- nombre d'individus détecté
- nombre d'individus confirmé
- temps d'inférence (fixé à 65ms pour train>3)
- nombre de faux positifs
- taux de faux positif
- score F1

### Protocole expérimental
Avant toutes choses, je me devais de modifier le script d'entrainement [[YOLOTrain.py]] pour renseigner la bonne version de la bdd à utiliser ainsi que paramétrer les nombres d'époques et de batch. Une fois l'entrainement lancé le programme nous renvoie la durée totale de l'entrainement, et stock l'ensemble des fichiers qu'il a généré (graphiques, résultats et model) dans un dossier *train* correspondant à l'itération de l'entrainement concerné. 
Cela fait, il est désormais nécessaire de lancer le script [[YOLOBenchmark.py]] qui nous permet de tester tous les modèles équitablement et de copier puis ranger les fichiers poids des modèles dans des dossiers, individuel à chaque entrainement, préalablement créé (par le script). 
Les résultats de [[YOLOBenchmark.py]] sont ensuite stockés dans les fichiers log eux aussi rangé dans les dossiers individuels. 


## Résultats
### Résumé global des performances
Dans ce résumé, nous excluons l'entrainement n°0 correspondant à un premier essais lancé sur Google Collab. 

### Modèles les plus performants au regard du score total

|ID|Score total|F1 score|Precision|Recall|IoU mean|FP rate|
|---|---|---|---|---|---|---|
|**train2**|**74,99**|0,7345|0,738|0,731|0,766|0,262|
|**train10**|**72,3**|0,7142|0,729|0,7|0,764|0,271|
|**train13**|**72,98**|0,7260|0,721|0,731|0,754|0,279|
|**train18**|**71,02**|0,7430|0,717|0,771|0,765|0,283|
|**train12**|**69,15**|0,7417|0,707|0,78|0,763|0,293|

Ces modèles combinent bon F1-score, haut IoU et faible taux de faux positifs (FP rate).


### Modèles sous-performants
Ci-dessous la liste des modèles relevés comme sous-performant.

|ID|Score total|F1 score|Précision|Recall|IoU|Commentaire|
|---|---|---|---|---|---|---|
|train4|0|0|0|0|0|Aucune détection|
|train5|0|0|0|0|0|Idem|
|train6|0|0|0|0|0|Idem|
|train3|43,15|0,008|1|0,004|0,691|Détection unique sur 223 GT|


### Impact de l’augmentation des epochs

|Epochs|Moyenne Score total (environ)|
|---|---|
|50|~63–74|
|100|~65–72|
|200|72,98|
|500|69,21|

Le gain au-delà de 100 epochs semble marginal voire stagnant (plateau), sauf pour certains cas (ex : train13 à 200 epochs). 500 epochs n’apporte pas d’avantage clair par rapport à 100 ou 200.


### Analyse par BDD version

|BDD version|Meilleur modèle (Score total)|ID|
|---|---|---|
|1|Aucun (tous très faibles)|train3-6|
|2|72,3|train10|
|3|74,99|train2|
|4|71,02|train18|

La BDD version 3 semble fournir les meilleurs résultats globalement, suivie de la version 4.


### Équilibre précision / rappel (F1 Score)

Tous les modèles avec F1 > 0,73 ont :
- IoU > 0,76
- FP rate < 0,3
- Score total > 69

Cela confirme que le Score total maison est globalement bien corrélé avec le F1 et la qualité des détections (pas trop biaisé par un seul paramètre).

### Matrice de corrélation
Cette matrice montre la corrélation de Pearson entre différentes métriques (score, précision, rappel, IoU, etc.). Les corrélations proches de 1 indiquent une forte relation positive, proches de 0 une absence de relation, et négatives (proches de -1) une relation inverse.

#### Corrélations fortes avec le score total

|Variable|Corrélation avec Score total|
|---|---|
|**IoU mean**|**0,97** (très fort)|
|**Recall**|**0,91**|
|**Matched**|**0,91**|
|**FP rate**|**0,91**|
|**Nb. Detect.**|**0,90**|
|**Precision**|**0,88**|
|**FP**|**0,85**|
|**BDD version**|**0,74**|
Le score total est **fortement influencé** par les métriques de performance fondamentales : IoU, recall, matched, et précision. L'augmentation du rappel (récupération) et du taux de détection entraîne clairement une hausse du score. 
Cela relevé, rien d'anormal n'apparait ici. En effet intrinsèquement à sa construction le score total ne dépend que de ces paramètres.



#### Corrélations internes entre métriques

- **Recall et Nb. Detections** : **0,997** -> presque parfaitement corrélés.

- **Matched et Nb. Detections** : **0,997** -> logique, matched est un sous-ensemble des détections.

- **Recall et Matched** : **0,971** -> très logique aussi.

- **FP et FP rate** : **0,967** -> cela peut refléter que plus un modèle détecte, plus il prend de risques (et en retire du gain, malgré des erreurs).

- **IoU et Precision** : **0,954** -> la qualité des détections influe sur la précision.

Les métriques liées à la détection (recall, matched, FP) sont fortement liées entre elles, donc non indépendantes.


#### Corrélations avec les hyperparamètres

|Hyperparamètre|Score total|Corrélations notables|
|---|---|---|
|**Epochs**|0,18|Faible impact mais **positif**|
|**Batch**|0,06|Pratiquement **aucun impact direct**|
|**BDD version**|0,74|Très **fort impact** positif|

Comment interpréter ces corrélations :
- Le nombre d’epochs joue un rôle modéré mais non négligeable.
- Le batch size n’a presque aucun effet (voire légèrement négatif sur précision).
- Le choix de la BDD version influence fortement toutes les métriques de performance -> choix des données crucial.


#### Corrélations faibles ou négligeables

- Batch vs Score total : **0,06**
- Batch vs Precision : **-0,025**
- Epochs vs FP : **0,05**

Cela montre que certains hyperparamètres n'ont pas d'effet significatif isolément sur la performance globale.


### Discussion
Les résultats de cette étude mettent en évidence plusieurs enseignements intéressants sur la performance des modèles YOLO selon les versions de dataset, les paramètres d’entraînement et les métriques de détection. D’abord, la version de la base de données utilisée a un impact considérable sur la performance globale du modèle, bien plus significatif que celui des hyperparamètres classiques tels que le nombre d’epochs ou la taille du batch. En particulier, la version 3 du dataset, issue d’un simple filtrage colorimétrique sur la version 2, semble produire les modèles les plus efficaces, ce qui suggère que des modifications visuelles même mineures peuvent renforcer la robustesse du modèle en apportant une forme d’augmentation de données implicite. La version 4, enrichie de nombreuses nouvelles images annotées, confirme également cette tendance à l’amélioration via l’enrichissement des données.

Les modèles les mieux notés, comme _train2_, _train10_ et _train13_, présentent une combinaison optimale entre F1-score élevé, IoU supérieur à 0,76 et faible taux de faux positifs, indiquant que le score total construit pour cette étude est cohérent avec les standards d’évaluation classiques. À l’inverse, certains entraînements (notamment ceux réalisés sur la version 1 du dataset) échouent complètement à détecter quoi que ce soit, illustrant la limite des données d'origine pour une utilisation avec la GeoDanceHive. 

La matrice de corrélation vient appuyer ces conclusions quantitativement. Elle montre que le score total est fortement corrélé avec des métriques clés telles que le recall, le IoU, le taux de détection ou encore la précision, confirmant qu’il est un indicateur global pertinent. D’ailleurs, les corrélations très fortes entre certaines variables, comme celles entre recall, matched et nombre de détections, indiquent une dépendance structurelle entre les métriques de détection, rendant certaines d’entre elles redondantes dans l’analyse.

Enfin, du côté des hyperparamètres, l’impact du nombre d’epochs, bien que positif, reste modeste et tend à saturer rapidement, surtout au-delà de 100 epochs. Le batch size, quant à lui, s'avère globalement insignifiant. Cela souligne que dans un cadre à ressources limitées (durée du stage), la priorité devrait être donnée à la qualité et la diversité du dataset plutôt qu’à l’ajustement fin de ces hyperparamètres.

## Conclusion
Cette _Ablation study_ confirme de manière claire que la qualité et l’enrichissement du dataset sont les facteurs déterminants pour obtenir de bonnes performances dans une tâche de détection d'objets. La version 3 du dataset, combinant annotations issues du terrain et transformation colorimétrique, permet d’atteindre les meilleurs résultats, supplantant même les apports d’un entraînement prolongé. Le score total utilisé, construit à partir des métriques classiques, reflète fidèlement la performance globale des modèles. Par ailleurs, l’analyse statistique confirme que les métriques de détection sont fortement liées entre elles, mais surtout que l’impact des hyperparamètres comme les epochs ou le batch size reste marginal en comparaison avec le choix du dataset. En résumé, pour optimiser les performances dans ce contexte, il vaudrait mieux investir dans la diversification et l’enrichissement des données plutôt que dans le raffinement des paramètres d’entraînement.
