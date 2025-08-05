8-10 pages
 
## Chapitre 0
Nous  etions le lui 28 avril, j’étais à la fois stressé et impatient. On m’avait dit d’arriver à 9h, mais moi, toujours en retard et soucieux de faire bonne impression, j’avais pris de l’avance. Résultat : je suis arrivé avec presque 1h d’avance. Le bâtiment s’éveillait lentement au rythme des premiers cafés, tandis que le couloir où j’avais rendez-vous somnolait encore dans la pénombre. J'ai alors attendu, assis, devant cette pièce dont les murs laissaient tout transparaître de l'intérieur, sans même savoir que cela deviendrait mon bureau. C'est Laura, ingénieure de recherche au laboratoire depuis quelques temps déjà, qui avait été missionnée par Guillaume (en télétravail), pour m’accueillir en ce premier jour du premier stage.  

Si pour elle cela devait être une intégration parmi tant d’autres, pour moi, c’était une journée charnière, à la fois importante et décisive. Importante car c'est durant cette matinée que j'ai eu le droit à la visite guidée de ce qui deviendrait mon quotidien pour les 4 prochains mois. Et décisive car dès les premières minutes j'étais convaincu d'être intégré dans une équipe souriante, agréable et dynamique. Que rêver de plus pour un premier stage ?  J'ai alors très rapidement pris place dans mon bureau tout de verre vêtu avec Paul à ma gauche et Justin à ma droite ; enfin cela à l'heure où j'écris ce rapport. En réalité, lorsque je suis arrivé j'étais dos à eux, face à un couloir où les regards ne font que se croiser. Cependant j'ai très vite été invité à me joindre plus encore à eux. Ils m'ont alors aidé à m'installer, à commander le matériel et à faire les démarches logistiques nécessaire à ma mobilité. Même si j'en étais un, je ne me sentais pas stagiaire. A l'image de Paul et Justin, tout le monde dans cette équipe m'a dès le début fait sentir comme un collègue à part entière.  

Je passerai rapidement sur les détails rocambolesques de mon installation informatique… quoique. Ce fut presque romanesque : d’abord aucun ordinateur disponible, puis une machine qui, une fois en main, écrivait toute seule (!). Finalement, après plusieurs ajustements, il fut décidé que je travaillerais sur une machine Linux dédiée, encore en transit depuis un autre site. En attendant, on m’attribua un PC bureautique temporaire, inadapté aux calculs nécessaires à mes tâches, et que je devais bientôt restituer. Résultat : je me suis vite replié sur mon ordinateur personnel, le temps que ma station de travail arrive. Ce qui devait prendre deux semaines mais qui s’est transformé en un mois et demi.  

Bien que peu facilitant, cet épisode kafkaïen aura au moins eu le mérite d’ajouter une touche de suspense à mes débuts de stage. Malgré ces aléas matériels, j’ai pu commencer à travailler sans attendre, puisque ma première mission consistait à effectuer un état de l’art approfondi. Armé de Python et de mon fidèle moteur de recherche, j’ai consacré une bonne semaine et demie à explorer la littérature sur le projet Dance, le fonctionnement physique et algorithmique de la GeoDanceHive, ainsi que les travaux de Sylvain Galopin. Cette recherche m’a même permis d’identifier quelques éléments complémentaires que j’ai pu transmettre pour enrichir l’état de l’art de la thèse de Sylvain. C’est aussi lors ces premiers jours que j’ai mis en place une rigueur d’organisation qui me manquait jusque-là. Étudiant souvent éparpillé, j’ai pris le parti de structurer strictement mon travail, conscient que c’était une condition sine qua non pour progresser efficacement dans ce contexte de recherche exigeant.

## **Méthodologie de travail et collaboration**
Cette organisation a reposé majoritairement sur un outil que je n’oublierai pas de mentionner dans mes remerciements tant il m'a été indispensable : Obsidian. Bien que déjà familier avec ce logiciel que j’utilisais à l’école comme simple éditeur de texte, j'ai à travers ce stage, eu l'occasion de découvrir toute sa force. Sa vue graphique permettant de visualiser les connexions entre les sujets m’a été précieuse pour structurer ma compréhension du projet. Son espace de toile, irremplaçable quand il a s'agit de construire des réflexions, m’a permis de poser et d’articuler mes idées. Les notes quotidiennes automatisées, quant à elles, ont instauré une rigueur d’écriture et de suivi que je n’avais jamais atteinte jusque-là. Ou encore son intégration a Git permettant la portabilité et la sauvegarde de tout l'espace de travail... Non, vraiment, je n'ai aucun doute. Pour que ce logiciel soit gratuit et qui plus est, open source, c'est qu'il est divin !  

À cette organisation personnelle s’est ajoutée la cadence structurante des points hebdomadaires avec Guillaume. Ces échanges réguliers, renforcés à mi-parcours par des réunions d’équipe plus élargies, ont rythmé mon stage avec efficacité. 

Ils m’ont permis d’ajuster ma trajectoire au fil de l’avancement, de partager mes réussites, mais aussi d’exprimer mes doutes ou blocages. Ce cadre d’échange, à la fois bienveillant et stimulant, a grandement facilité mon immersion dans un univers de recherche pourtant nouveau pour moi. 

Grâce à cette organisation bien en place j’ai pu aborder sans encombre la première étape concrète du pipeline : la détection d’abeilles à l’aide de YOLOv10. Ce fut le début du travail technique à proprement parler, où il ne s’agissait plus de lire ou de structurer, mais de manipuler des scripts, des images, des modèles... Bref, de rentrer dans le cœur de mon stage.

## Développement de la première brique : détection d’abeilles avec YOLOv10
Si le cadre de travail était clair, le chemin pour y parvenir, lui, l'était beaucoup moins. L'objectif était de faire “simple” : détecter les abeilles dans une vidéo. Facile à dire, mois surtout lorsqu’on sait que ces vidéos sont tournées dans une ruche, dans des conditions lumineuses instables, sur des supports mobiles, et que les abeilles elles-mêmes s’empilent, se fondent dans le décor, disparaissent et réapparaissent comme par magie. 

C’est donc dans ce contexte que j’ai entamé mes travaux sur YOLOv10, un modèle de détection en temps réel réputé rapide et efficace. Le plan initial ? Le fine-tuner sur un petit jeu de données annoté manuellement pour vérifier s’il pouvait repérer nos abeilles sur les cadres de la GeoDanceHive.

### Les débuts chaotiques
L’installation du modèle, bien qu'encadrée par une documentation dense, n’a pas été de tout repos. Il a d’abord fallu préparer l’environnement de travail : configuration de l’environnement virtuel, installation des bibliothèques, ajustement de la version de Python, abandon de WSL en route… Une série d’obstacles techniques classiques, mais chronophages, qui m'ont parfois fait regretter le confort d’un simple IDE tel qu’Arduino. 

Une fois l’environnement stable, les premiers tests ont pu commencer. J’ai d’abord utilisé un dataset existant sur RobotFlow, enrichi de de deux images de la GDH annotées à la main. Deux modèles ont été entraînés, avec et sans les ajouts personnels, mais les résultats ont été décevants : les abeilles n’étaient pas du tout détectées. Trop peu de données, trop de bruit, trop d’abeilles ?

### Améliorer le dataset, affiner le modèle
Alors, la suite logique a été d’améliorer la qualité des données. C'est ainsi, que j’ai entamé un travail sur l’amélioration des images : application de filtres CLAHE, ajustement de la saturation et de la netteté, choix validé après un mini-sondage lancé sur Zulip auprès de l’équipe. Néanmoins pour aboutir à cette combinaison précise d’étape améliorantes, il a fallu que je procède a de nombreux test et exploration afin de déterminer ce qui méritait mon attention ou pas.   

Côté annotation, toute l’équipe a mis la main à la pâte. A travers la plateforme Robotflow, nous avons pu procéder à une annotation collaborative des images de la GDH. Initialement plein de bonne volontés, j’avais prévu un set de 100 images à annoter à la main. Malheureusement une seule image prenait presque 30 min a une seule personne pour être entièrement complété. De ces 100 images, seules 9 ont été complètements annotés. Il fallait trouver une solution pour multiplier le datset sans multiplier nos efforts. C’est ainsi qu’est ne le Cisor2000, un script que j’ai développé capable de découper les images et leur fichier label. De ce fait une image annote en donnait neuf. Cela était possible du fait de la densité de population et de la qualité des images.    

Néanmoins, il fallait trouver une manière de récupérer les images déjà annote sur Robotflow de façon à ne pas perdre le travail déjà amorce. C’est a ce moment qu’intervient YOLOExtractor, mon petit script de scraping, qui extrait du code source du site le json des coordonnées des boites et le transforme en fichier label au format Yolo. Finalement, je n’avais plus qu’à réinjecter mes images découpées dans la BDD. Ainsi de neuf images annotes plus de soixante sont apparues.  

Désormais il ne reste plus qu’à tester.

### Une première lumière au bout du tunnel
Houra !! \*danse de la joie\* 

Les premières inférences réussies ont eu lieu début juillet. Mon model détectait les abeilles, imparfaitement certes, mais de façon cohérente. Quelle satisfaction de voir ces petites boîtes bleues apparaître autour de ces minuscules tâches, dans des images pourtant si denses ! Un vrai tournant dans le stage, confirmé par une série de réunions avec Guillaume et F.-J. Richard, qui ont aidé à fixer la trajectoire à suivre : continuer à fiabiliser ce pipeline, tout en gardant en tête qu’il ne s’agit que d’un maillon de la chaîne plus ambitieuse du projet. 

A ce stade j’ai également conceptualisé un benchmark complet pour le test des différents model avec différentes variation d’hyperparamètres ou de base de données.

### Et après ?
Cette étape YOLO, bien que semée d’embûches, m’a beaucoup appris. À la fois sur les modèles de détection en temps réel, sur les limites d’un dataset bricolé maison, mais surtout sur la patience nécessaire quand on travaille sur avec des objets vivants, dans un cadre réel, avec tout ce que cela implique de bruit, d’imprévus et d’incertitudes. Et c’est peut-être ça, le plus précieux. 

YOLOv10 m’a permis de poser les bases d’un système de détection robuste même s’il ne s’agit encore que du premier étage de la fusée. Car détecter les abeilles sur une image, c’est une chose. Mais les suivre dans le temps, image après image, pour reconstituer leurs trajectoires et, à terme, tenter d’interpréter leur comportement… c’en est une autre. 

A ce moment-là, il ne s’agissait plus seulement de dire où se trouve une abeille, mais où elle va, d’où elle vient, et combien de temps elle reste. Ce changement de perspective m’a naturellement conduit vers l'étape suivante du pipeline : Deep SORT.

## Implémentation du suivi multi-objets avec Deep SORT

> [!tip]-
> - Intégration de Deep SORT au modèle YOLOv10.
> - Configuration du tracker : dimension des descripteurs visuels, réglage du filtre de Kalman, seuils d’association.
> - Visualisation des trajectoires sur des séquences réelles.
> - Analyse critique :
>     - Les identifiants restent-ils stables ?
>     - Quels cas d’erreur sont les plus fréquents ?
>     - Comment la lumière, l’angle de vue ou la densité d’abeilles influencent-ils les résultats ?
> 
> > 🎯 _Ici, souligne ton apport analytique : comment tu as exploré les erreurs et cherché à les comprendre._
> 


## **Documentation et outils développés**
> [!tip]-
> 
> - Scripts créés :
>     
>     - Prétraitement des données.
>         
>     - Pipeline d’entraînement YOLO.
>         
>     - Pipeline d’inférence et suivi avec Deep SORT.
>         
> - Structure du code développée : modularité, reproductibilité.
>     
> - Suivi des expériences (fichiers logs, notebooks, Git ?).
>     

différents scripts et Ablation study

## Résultats obtenus à la fin du stage

> [!tip]-
> - Fonctionnement des deux premières briques validé :
>     
>     - Détection d’abeilles efficace dans certaines conditions.
>         
>     - Tracking opérationnel mais à affiner.
>         
> - Limites rencontrées qui bloquent les étapes suivantes :
>     
>     - Trajectoires trop bruitées.
>         
>     - Trop peu de stabilité pour distinguer des formes précises.
>         
> - Potentiel de réutilisation du travail :
>     
>     - Base solide pour la suite du pipeline.
>         
>     - Suggestions pour la suite du projet (ex : nettoyage des trajectoires, intégration de post-traitement...).
>         



> [!tip]-
> ## 8. **Transition vers l’analyse critique (chapitre 5)**
> 
> _(Courte phrase de transition, **sans contenu réflexif**)_
> 
> > Le travail mené pendant ce stage m’a permis de comprendre en profondeur les enjeux techniques liés à la détection et au suivi de comportements animaux en environnement non contrôlé. Le chapitre suivant propose une analyse plus globale du stage, à travers les compétences développées, les difficultés rencontrées, et les enseignements personnels et professionnels tirés de cette expérience.
