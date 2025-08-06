8-10 pages
 
## Chapitre 0
Nous  étions le lundi 28 avril, j’étais à la fois stressé et impatient. On m’avait dit d’arriver à 9h, mais moi, toujours en retard et soucieux de faire bonne impression, j’avais pris de l’avance. Résultat : je suis arrivé avec presque 1h d’avance. Le bâtiment s’éveillait lentement au rythme des premiers cafés, tandis que le couloir où j’avais rendez-vous somnolait encore dans la pénombre. J'ai alors attendu, assis, devant cette pièce dont les murs laissaient tout transparaître de l'intérieur, sans même savoir que cela deviendrait mon bureau. C'est Laura, ingénieure de recherche au laboratoire depuis quelques temps déjà, qui avait été missionnée par Guillaume (en télétravail), pour m’accueillir en ce premier jour du premier stage.  

Si pour elle cela devait être une intégration parmi tant d’autres, pour moi, c’était une journée charnière, à la fois importante et décisive. Importante car c'est durant cette matinée que j'ai eu le droit à la visite guidée de ce qui deviendrait mon quotidien pour les 4 prochains mois. Et décisive car dès les premières minutes j'étais convaincu d'être intégré dans une équipe souriante, agréable et dynamique. Que rêver de plus pour un premier stage ?  J'ai alors très rapidement pris place dans mon bureau tout de verre vêtu avec Paul à ma gauche et Justin à ma droite ; enfin cela à l'heure où j'écris ce rapport. En réalité, lorsque je suis arrivé j'étais dos à eux, face à un couloir où les regards ne font que se croiser. Cependant j'ai très vite été invité à me joindre plus encore à eux. Ils m'ont alors aidé à m'installer, à commander le matériel et à faire les démarches logistiques nécessaire à ma mobilité. Même si j'en étais un, je ne me sentais pas stagiaire. A l'image de Paul et Justin, tout le monde dans cette équipe m'a dès le début fait sentir comme un collègue à part entière.  

Je passerai rapidement sur les détails rocambolesques de mon installation informatique… quoique. Ce fut presque romanesque : d’abord aucun ordinateur disponible, puis une machine qui, une fois en main, écrivait toute seule (!). Finalement, après plusieurs ajustements, il fut décidé que je travaillerais sur une machine Linux dédiée, encore en transit depuis un autre site. En attendant, on m’attribua un PC bureautique temporaire, inadapté aux calculs nécessaires à mes tâches, et que je devais bientôt restituer. Résultat : je me suis vite replié sur mon ordinateur personnel, le temps que ma station de travail arrive. Ce qui devait prendre deux semaines mais qui s’est transformé en un mois et demi.  

Bien que peu facilitant, cet épisode kafkaïen aura au moins eu le mérite d’ajouter une touche de suspense à mes débuts de stage. Malgré ces aléas matériels, j’ai pu commencer à travailler sans attendre, puisque ma première mission consistait à effectuer un état de l’art approfondi. Armé de Python et de mon fidèle moteur de recherche, j’ai consacré une bonne semaine et demie à explorer la littérature sur le projet Dance, le fonctionnement physique et algorithmique de la GeoDanceHive, ainsi que les travaux de Sylvain Galopin. Ces recherches m’ont même permis d’identifier quelques éléments complémentaires que j’ai pu transmettre pour enrichir l’état de l’art de la thèse de Sylvain. C’est aussi lors ces premiers jours que j’ai mis en place une rigueur d’organisation qui me manquait jusque-là. Étudiant souvent éparpillé, j’ai pris le parti de structurer strictement mon travail, conscient que c’était une condition sine qua non pour progresser efficacement dans ce contexte de recherche exigeant.

## Méthodologie de travail et collaboration
Cette organisation a reposé majoritairement sur un outil que je n’oublierai pas de mentionner dans mes remerciements tant il m'a été indispensable : Obsidian. Bien que déjà familier avec ce logiciel que j’utilisais à l’école comme simple éditeur de texte, j'ai à travers ce stage, eu l'occasion de découvrir toute sa force. Sa vue graphique permettant de visualiser les connexions entre les sujets m’a été précieuse pour structurer ma compréhension du projet. Son espace de toile, irremplaçable quand il a s'agit de construire des réflexions, m’a permis de poser et d’articuler mes idées. Les notes quotidiennes automatisées, quant à elles, ont instauré une rigueur d’écriture et de suivi que je n’avais jamais atteinte jusque-là. Ou encore son intégration a Git permettant la portabilité et la sauvegarde de tout l'espace de travail... Non, vraiment, je n'ai aucun doute. Pour que ce logiciel soit gratuit et qui plus est, open source, c'est qu'il est divin !  

À cette organisation personnelle s’est ajoutée la cadence structurante des points hebdomadaires avec Guillaume. Ces échanges réguliers, renforcés à mi-parcours par des réunions d’équipe plus élargies, ont rythmé mon stage avec efficacité. 

Ils m’ont permis d’ajuster ma trajectoire au fil de l’avancement, de partager mes réussites, mais aussi d’exprimer mes doutes ou blocages. Ce cadre d’échange, à la fois bienveillant et stimulant, a grandement facilité mon immersion dans un univers de recherche pourtant nouveau pour moi. 

Grâce à cette organisation bien en place j’ai pu aborder sans encombre la première étape concrète du pipeline : la détection d’abeilles à l’aide de YOLOv10. Ce fut le début du travail technique à proprement parler, où il ne s’agissait plus de lire ou de structurer, mais de manipuler des scripts, des images, des modèles... Bref, de rentrer dans le cœur de mon stage.

## Développement de la première brique : détection d’abeilles avec YOLOv10
Si le cadre de travail était clair, le chemin pour y parvenir, lui, l'était beaucoup moins. L'objectif était de faire “simple” : détecter les abeilles dans une vidéo. Facile à dire, moins à faire, surtout lorsqu’on sait que ces vidéos sont tournées dans une ruche, dans des conditions lumineuses instables et que les abeilles elles-mêmes s’empilent, se fondent dans le décor, disparaissent et réapparaissent comme par magie. 

C’est donc dans ce contexte que j’ai entamé mes travaux sur YOLOv10. Le plan initial ? Le fine-tuner sur un petit jeu de données annoté manuellement pour vérifier s’il pouvait repérer nos abeilles sur les cadres de la GeoDanceHive.

### Les débuts chaotiques
L’installation du modèle, bien qu'aidé par une documentation dense, ne fut pas de tout repos. Il fallut d’abord préparer l’environnement de travail : configuration de l’environnement virtuel, installation des bibliothèques, ajustement de la version de Python, abandon de WSL en route pour cause de sécurité informatique… Une série d’obstacles techniques classiques, mais chronophages, qui m'ont parfois fait regretter le confort d’une simple Arduino. D'autant plus, que malgré que cela soit prévu, du fait que j'eusse commencé sans ordinateur IGN, je n'avais pas accés au calculateur. J'ai donc lancé mes premiers entrainements de modèle sur le GPU de Google Collab. 

Une fois l’environnement installé, les premiers tests ont pu commencer. Lors de mes recherches, j'avais trouvé un dataset de plus de 900 images d'abeilles sur RobotFlow. Je me suis alors servis initialement de ce dernier, enrichi de de deux images de la GDH annotées à la main. Deux modèles ont été entraînés (sur Google Collab), avec et sans les ajouts personnels, mais les résultats furent décevants : les abeilles n’étaient pas du tout détectées. 
Les raisons pouvaient être multiples : trop peu de données, trop de bruit, de mauvais hyper paramètres, trop d’abeilles ?

### Améliorer le dataset, affiner le modèle
A ce stade là, pour moi, la suite logique était l'amélioration des images du dataset GDH. Il fallait réussir à améliorer la qualité des frames des vidéos afin d'augmenter la lisibilité et donc le potentiel discernement des modèles. Pour ce faire, j'ai d'abord penser à de simples modification de contraste et de luminosité superposé. Toujours dans la même logique, après des recherches et discussions avec Guillaume, j'avais une idée d'un workflow à suivre pour augmenter la résolution de mes images. J'ai donc une nouvelle fois abouti à un pipeline que voici.

\[pipeline traitement d'image]

J'ai alors entamé le travail par la création d'un script prenant des images au hasard dans un dossier contenant toutes les frames de la vidéo de travail (obtenue aussi à partir d'un script) et leur applicant les mêmes modifications. 

C'est ainsi, que j’ai entamé un travail sur l’amélioration des images. application de filtres CLAHE, ajustement de la saturation et de la netteté, choix validé après un mini-sondage lancé sur Zulip auprès de l’équipe. Néanmoins pour aboutir à cette combinaison précise d’étape améliorantes, il a fallu que je procède a de nombreux test et exploration afin de déterminer ce qui méritait mon attention ou pas. A ce moment-ci je pensais avoir une amélioration optimale de mes images. Il ne fallait donc plus qu'à la développer sur un plus grand nombre d'image de la GDH. J'avais donc besoin d'un grand nombre d'image annoté, or seulement deux m'avait pris presque une après-midi entière. C'est ici que l'intéret d'avoir intégré une équipe de recherche s'est fait sentir. J'ai donc mobilisé tout le potentiel du laboratoire et ai demandé l'aide de toute l'équipe.

Grâce à Robotflow et sa plateforme en ligne, nous avons pu procéder à une annotation collaborative des images de la GDH. Initialement plein de bonne volontés, j’avais prévu un set de 100 images à annoter à la main. Malheureusement une seule image prenait presque 30 min a une seule personne pour être entièrement complété. C'est d'ailleurs pourquoi de ces 100 images, seules 9 furent complètements annotés. Il fallait trouver une solution pour multiplier le dataset sans multiplier nos efforts. Deux possibilité s'offraient à moi : une augmentation virtuelle ou physique du jeux de données. 
C’est ainsi qu’est né le Cisor2000, un script que j’ai développé capable de découper les images et leur fichier label. De ce fait une image annotée en donnait neuf. Cela était possible du fait de la densité de population et de la qualité des images. J'avais donc désormais une augmentation physique significative de mon dataset. Pour 9 images, je pouvais en généré 89. Dans les même temps Guillaume me proposa de copier le dataset original et d'en faire une copie "violetisée". En effet nous supposions que cela pouvait aider le modèle. 
J'ai donc appliqué un filtre de couleur que je jugeais ressemblant aux images de la GDH aux 900 images du dataset original. 

Désormais, j'avais un jeu de donné de 89 images dont la qualité avait été amélioré. Cependant malgré l'amélioration, il restait des zones illisibles. En effet les régions sous les projecteurs UV étaient cramée, de ce fait toutes les abeilles dans ces espaces étaient invisibles. Pour régler ce problème, j'ai d'abord pensé et mis en place une stratégie de ROI. 

L'idée était la suivante. Après avoir déterminé les coordonnées précise des région d'intérets (cramées) sur paint, je n'avais qu'a appliqué des modifications différentes dans ces périmètres dans mon pipeline de traitement. Pourtant fonctionnel, les résultats obtenues laissaient apparaître des frontières incisives aux abords de ces ROI. Lors d'une réunion d'équipe ou je présenta ces résultats Sylvain, me fit part de ses doutes quant aux produits obtenus et m'encouragea a me pencher du côtés des filtres dynamiques. C'est ainsi que le filtre CLAHE est arrivé dans mon pipeline de traitement d'image. Les résultats étaient sans appels. La pipeline définitive de traitement d'image venait d'être re-designée avec l'aide d'un petit sondage sur Zulip.

\[pipeline définitive traitement d'image]

Maintenant, il fallait trouver une manière de récupérer les images déjà annoté sur Robotflow de façon à ne pas perdre le travail déjà amorcé et surtout de façon à pouvoir le complété. C’est apparu le YOLOExtractor, mon petit script de scraping, capable d'extraire du code source du site Robotflow, le json des coordonnées des boites et de le transformer en fichier label au format Yolo.

Finalement, je n’avais plus qu’à réinjecter mes images découpées, traité et compété dans la BDD. Ainsi d'initialement neuf images annotés plus de soixante sont apparues (comme je n'ai pas relancé de phase d'annotation certaines image peu annoté n'ont pas été intégré au dataset).  

Désormais j'avais 1800 images dans ma base de données,  il ne reste plus qu’à les tester !

### Une première lumière au bout du tunnel
Houra !! \*danse de la joie\* 

Les premières inférences réussies ont eu lieu début juillet. Mon model détectait les abeilles, imparfaitement certes, mais de façon cohérente. Quelle satisfaction de voir ces petites boîtes bleues apparaître autour de ces minuscules tâches, dans des images pourtant si denses ! Un vrai tournant dans le stage, confirmé par une série de réunions avec Guillaume et F.-J. Richard, qui ont aidé à fixer la marche à suivre : continuer à fiabiliser ce pipeline, tout en gardant en tête qu’il ne s’agit que d’un maillon de la chaîne plus ambitieuse du projet. 

Comme mes premiers entrainements (avec le calculateur de l'IGN à travers une connexion ssh) étaient concluants il me fallait désormais déterminer quelle combinaison d'hyper paramètres était la plus optimale. Pour ce faire j'ai développer un script de benchmark me permettant de procéder à la même évaluation sur mes différents modèles. J'ai alors pu évaluer 21 modèles entrainés différemment. Grâce à une matrice de correlation j'ai pu déterminé quels paramètres étaient importants et quel modèle était le plus efficace. Notre grand vainqueur est ainsi le modèle 15.

### Et après ?
Cette étape YOLO, bien que semée d’embûches, m’a beaucoup appris. À la fois sur les modèles de détection en temps réel, sur les limites d’un dataset bricolé maison, mais surtout sur la patience nécessaire quand on travaille avec des objets vivants, dans un cadre réel, avec tout ce que cela implique de bruit, d’imprévus et d’incertitudes. Et c’est peut-être ça, le plus important. 

YOLOv10 m’a permis d'installer la première brique d’un système de détection complexe même s’il ne s’agit encore que du début. Car détecter les abeilles sur une image, c’est une chose. Mais les suivre dans le temps, image après image, pour reconstituer leurs trajectoires et, à terme, tenter d’interpréter leur comportement… c’en est une autre (!).

A ce moment-là, il ne s’agissait plus seulement de dire où se trouve une abeille, mais où elle va, d’où elle vient, et combien de temps elle reste. Ce changement de perspective m’a naturellement conduit vers l'étape suivante du pipeline : Deep SORT.

Néanmoins, avant de changer de bloc, permettez moi de vous partager les premiers résultats. Fruits de toutes les étapes précédentes, vous pourrez trouver une courte vidéo issue de l'inférence du modèle 15 sur un extrait de la vidéo de travail (en scannant ce qr-code).

## Implémentation du suivi multi-objets avec Deep SORT
Comme on peut le remarquer la grande majorité des abeilles sont ici détecté cependant elles ne sont pas identifiées. C'est à dire que d'une image (frame) à l'autre le modèle ne fait pas lien entre les individus détectés. Il n'est pas conscient que la meme détection au même endroit mais sur la frame d'après relate à la même abeille. 

De ce fait, il était nécessaire d'intégré un algorithme de suivi multi-objets. Mes recherches en début de stage laissaient sous-entendre que Deep SORT était la meilleure solution pour cette étape du workflow. 

Me voilà alors lancé dans le décorticage de Deep SORT. Sur la base de projet déjà existant. J'ai alors tenté de procéder à des implémentation simple en copiant simplement des dépôts GitHub. Mais malheureusement le modèle était très peu performant. Malgré la tentative de modification de certaines méthodes dans les classes ou même la modification des hyperparamètres ou du filtre Kalman, les résultats n'étaient pas satisfaisants. En témoigne la meilleure vidéo généré, les suivies sont faux, les bbox de détection attachées aux centres malgré les tentatives de correction ou de remplacements par une croix. De plus le modèle mettait plus de 490s pour généré une vidéo de 15s (ce qui représente plus de 8min). Cette inefficience s'explique peut être dans la définition objet du tracker ou par la complexité des images, mais je n'ai entamé aucunes recherches approfondies pour confirmer ou pas ces hypothèses. 

Il était alors nécessaire de se réorienté vers un autre algorithme de suivi pour tenter de parvenir à des résultats plus satisfaisants. 

## Abandon de Deep SORT et découverte de Byte Track
C'est une nouvelle salve de recherches qui m'ont mené à Byte Track. Faisons un rapide point sur les différence entre Deep SORT et Byte Track. 

Si DeepSORT excelle dans le maintien de l’identité sur de longues séquences grâce aux embeddings visuels, il peut être plus lourd côté calcul et nécessite un détecteur et un extracteur de caractéristiques puissants. Or dans notre cas de figure, le détecteur (YOLO) ne donne pas que des résultats à forte confiance. ByteTrack, en revanche, est plus léger et plus rapide,  tout en obtenant de meilleurs scores MOTA et IDF1 que DeepSORT dans plusieurs études, ce qui défend sa fiabilité malgré l’absence de modèle d’apparence ([ResearchGate](https://www.researchgate.net/figure/Comparison-of-BYTE-and-DeepSORT-using-light-detec-tion-models-on-the-MOT17-validation_tbl3_355237366?utm_source=chatgpt.com "Comparison of BYTE and DeepSORT using light detec- tion models ...")).

Pour faire simple, DeepSORT privilégie une association basée sur l’apparence (en tenant de redétecter de son côté) pour garantir la continuité d’identité dans des scènes encombrées, tandis que ByteTrack mise sur une stratégie duale d’association (haute et basse confiance) pour maximiser la récupération des objets en mouvement rapide ou partiellement occultés. 

C'est pourquoi ByteTrack offre un excellent compromis entre vitesse et performance.

Alors, de la même façon que pour Deep SORT, j'ai d'abord procédé à une simple implémentation par copie de dépôt, qui s'est avéré encourageante. J'ai alors commencé de plus ample modification impliquant nottament l'ajustement des hyperparamètres. 

Après quelques essais pour ajuster les hyperparamètres, les résultats étaient bien mieux que Deep SORT pour un temps de compilation nettement inférieur (~72s), néanmoins je n'étais pas très satisfait de la différence entre les détections YOLO et celles de ByteTrack. Il m'aura fallut une journée pour me rendre compte que depuis le début des test, je ne lui avait pas donné la bonne vidéo. En effet, j'envoyer à l'algorithme la vidéo de sortie de YOLO avec les bbox dessinées dessus. En relançant les tests avec la vidéo originale dont seule la qualité a été touchée, les résultats était très satisfaisant. ByteTrack parvient à détecter et suivre presque toutes les détections de YOLO. Je me suis alors complétement approprié le script originel en y intégrant plusieurs modes, nottament la possibilité d'afficher ou pas les labels, de généré une couleur différente pour chaque individus ou de modifier le format de la vidéo de sortie (le fond et les infos à afficher).

Bien que imparfait le résultat le plus optimale, généré avec la meilleure combinaison d'hyperpramètre m'a permis de généré une réel preuve de concept que voici. 

Il est possible de détecter, suivre des abeilles et tracer leurs trajectoires bien qu'elle soit sur des images à population très dense. 

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
