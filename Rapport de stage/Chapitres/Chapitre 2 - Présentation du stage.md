5-10 pages
## 1. Contextualisation

S’il y a bien une chose que je ne soupçonnais pas avant ce stage, c’est à quel point les abeilles sont bavardes. Enfin, à leur manière. Car oui, ces petits insectes sont capables de communiquer entre elles de façon étonnamment sophistiquée, en indiquant à leurs congénères où se trouvent les bonnes ressources à butiner. Leur outil ? Une sorte de chorégraphie millimétrée qu’on appelle la danse frétillante, ou waggle dance en anglais. 

Comprendre cette danse et savoir l’interpréter automatiquement n’est pas juste une curiosité scientifique. Cela représente une aide précieuse pour les biologistes, les écologues, les apiculteurs et plus largement tous ceux qui s’inquiètent (à juste titre) du déclin des pollinisateurs. Et c’est justement dans cette optique qu’est née la GeoDanceHive, un dispositif d’étude aussi fascinant que complet. 

Ce projet, porté par Sylvain Galopin, est issu d’une thèse financée par l’OFB dans le cadre du plan Écophyto, sous la direction de Guillaume Touya (IGN) et Freddie-Jeanne Richard (INRAE). Ensemble, ils ont imaginé une ruche un peu particulière : la GeoDanceHive, une ruche expérimentale pensée pour observer sans déranger. 

Concrètement, il s’agit d’un assemblage de deux ruches : l’une classique, et l’autre vide, servant de “studio”, où l’on peut filmer les abeilles sur le premier cadre, sans les perturber. Ce “studio” embarque des caméras haute définition, un éclairage LED UV, et un mini-ordinateur équipé d’un algorithme de vision par ordinateur, capable de détecter et d’analyser ces fameuses danses. 

Tout ça, pour quoi faire ? Pour mieux comprendre les dynamiques de butinage, identifier les fleurs réellement visitées, et obtenir des données fines sur la manière dont les abeilles interagissent avec leur environnement. En somme, c’est un outil au service du suivi écologique, de la protection des pollinisateurs, et de l’amélioration des pratiques agricoles. 

Mais pour bien saisir l’utilité de tout ça, il faut plonger un instant dans le monde de la communication chez l’abeille. Car au-delà de leur petite taille, ces insectes ont mis en place un système de transmission d’informations extrêmement élaboré. 

Quand une butineuse trouve une source de nourriture intéressante, elle revient à la ruche et exécute, dans l’obscurité et au contact de ses sœurs, une danse en forme de 8, au centre de laquelle elle frétille en ligne droite. Ce frétillement encode deux informations clés : 

- la direction de la ressource (par rapport au soleil), 
- la distance à parcourir (estimée par la durée du frétillement). 

Oui, c’est un langage symbolique, chez un animal non humain. Ce n’est pas rien. 

Mais ce n’est pas tout : elles utilisent aussi des phéromones, des vibrations, des contacts physiques, voire des échanges de nourriture pour se transmettre des signaux d’alerte, d’organisation ou d’identification. C’est une organisation sociale incroyablement bien rodée, où tout semble pensé pour assurer la survie collective. 

C’est donc dans ce contexte (entre biologie comportementale, écologie, et nouvelles technologies) qu’intervient la GeoDanceHive. Et c’est dans ce cadre, aussi surprenant que stimulant, que j’ai réalisé mon stage. Autant dire que, même en n’étant pas fan des modèles d’apprentissage automatique, je n’ai pas pu rester insensible au potentiel de cet outil, pensé pour comprendre et protéger le vivant.

## 2. Problématique
Il suffit d’un simple coup d’œil sur une carte de ruchers pour comprendre une chose évidente : les abeilles ne vivent pas à côté de centres de calcul. En général, elles préfèrent les champs, les lisières, les zones isolées… Là où ni fibre optique, ni prises électriques, ni GPU dernier cri ne sont à portée de main. 

Et pourtant, la GeoDanceHive repose sur une analyse vidéo complexe, qui, dans sa version actuelle, nécessite environ quatre minutes de calcul pour dix minutes de vidéo, le tout sur un ordinateur classique. Autant dire que, dans l’état, aucune chance de l’embarquer au fond d’un champ sans une rallonge de deux kilomètres. Le défi est donc vite posé : comment faire tenir cette intelligence dans une ruche autonome électriquement ? Comment adapter ou repenser un système aussi gourmand, pour qu’il fonctionne en temps réel, sur un micro-ordinateur, sans renoncer à la qualité de détection attendue ?

## 3. Objectif du stage
C’est donc dans le sillage direct de cette problématique que s’est dessiné le sujet de mon stage. Face à un algorithme trop lourd pour être embarqué tel quel, il devenait indispensable de réfléchir à des pistes d’allègement, d’optimisation, et même d’amélioration. Mon rôle ? Explorer ces pistes, les tester, et voir jusqu’où je pouvais aller. 

Ainsi, ma mission lors de ce stage a été de développer un modèle d'apprentissage profond capable de détecter certains comportements spécifiques des abeilles comme les danses frétillantes. Du moins c'est l'intention que j'avais en amorçant mes premiers jours de travail. Les objectifs ont néanmoins été très rapidement réajusté par Guillaume, qui m'a expliqué que patience et longueur de temps étaient de rigueur dans la recherche. Effectivement, il était inenvisageable ou utopique d'espérer aboutir à un modèle fonctionnel en seulement 4 mois. C'est pourquoi l'une de mes premières taches fut d'entamer des recherches préliminaires, après un état d'art du projet, dans le but de dresser un plan de route et des objectifs réalistes.  

A plus large échelle, ce projet permettrait aussi et surtout le développement de vrai laboratoire d’étude portable. Nous accordant la possibilité d’étudier divers comportements et réactions des abeilles aux pesticides par exemple.

## 4. Plan de route 
Alors, le 7 mai, après deux semaines de recherche et d'assimilation du projet, je dressai ce pipeline que Guillaume approuva. Enfin pas du premier coup, en effet j'ai d'abord proposé d'autre modèle aussi pré-entraîné que je trouvais pertinent. DeepLabCut fut l'un d'entre eux. Je finis par le mettre de côté à la suite d'échange avec Guillaume car l'overview et les recherches associés à ce modèle montraient son efficacité dans la recherche lorsqu'il était utilisé sur des populations de faible données. Or nos cadres possède une densité importante d'individus par image, c'est pourquoi la barre fur redresser sur YOLOv10. 
Néanmoins, Guillaume me mit en garde quant au fait que je n'arriverai très certainement pas au terme de ce dernier dans les temps incombant mon stage. "Tu risques de passer tout ton stage sur la première étape, mais c'est ok !" me dit-il lors d'une réunion hebdomadaire, remarque que j'ai d'abord pris à la dérision, convaincu que je parviendrai à aller au bout. C'est seulement quelques jours après que j'ai saisi la véracité de son propos. Effectivement, bien que plein de bonnes intentions, je risquais de passer tout mon stage sur cette première étape.  

Dans l'unique but de préserver le suspense de ce rapport, je ne dévoilerai pas ici, si je suis parvenu à avancer plus loin que cette étape une.  

Voici donc le pipeline originel dressé à la genèse de ce stage. 

![[image du pipeline]] 

Détaillons brièvement l'anatomie de ce pipeline. Dans cette forme-là, il s'agit de sa première version, on verra par la suite que cette dernière a légèrement évolué au fils des semaines.

#### Etape 1 - YOLO Abeilles
Dans cette première étape l'idée est de détecter le plus d'abeilles possibles, mais individuellement. Ici on fait fi de leur position ou même de leur comportement. Le but est de faire une détection de masse que l'on discrétisera ensuite à travers les prochaines étapes. 

Pour se faire, je prévois d'utiliser un modèle d'apprentissage profond déjà entrainé une sur une importante quantité d'image, il s'agit de YOLOv10. L'enjeu ici est donc de parvenir à réentraîner soit fine-tuner le modèle pour qu'il reconnaisse les abeilles de la GDH.
#### Etape 2 - Deep sort
Une fois les individus discrétisés, l'objectif dans cette étape, et d'utiliser Deep Sort pour faire un tracé de leur trajectoire. Ainsi chacune de nos polinisatrices auraient un identifiant propre, ce qui nous permettrai alors d'installer une logique de suivi à travers les frames d'une vidéo. Ainsi nous serions en mesure de tracer les trajectoires de leurs coordonnées de déplacement, ou tout du moins de les récupérer.

> [!info] Deep SORT
> Deep SORT (Simple Online and Realtime Tracking with a Deep Association Metric) est un algorithme de suivi d’objets en temps réel qui améliore le système SORT original en y intégrant une composante d’apprentissage profond. Alors que SORT utilise uniquement les données de position et de mouvement (comme les boîtes englobantes et la vélocité) pour suivre les objets d’une image à l’autre, Deep SORT ajoute une dimension d’analyse visuelle en extrayant des descripteurs d’apparence via un réseau de neurones convolutifs. Concrètement, chaque objet détecté est associé à une empreinte visuelle, ce qui permet de le reconnaître plus facilement même s’il disparaît temporairement ou subit une occlusion. Le système combine ces informations avec un filtre de Kalman pour prédire la position future de chaque objet, et utilise l’algorithme de Hongrie pour résoudre le problème d’association entre détections et trajectoires existantes. En croisant les données de mouvement et d’apparence, Deep SORT améliore la robustesse du suivi multi-objets, en particulier dans des scènes complexes où les objets peuvent se croiser ou se ressembler visuellement.

#### Etape 3 - YOLO Trajectoires
À partir des coordonnées extraites via le suivi Deep SORT, il devient désormais possible de reconstruire visuellement les trajectoires des abeilles sous forme d’images binaires (noir et blanc), où les tracés représentent leurs déplacements au fil du temps. Ce type de représentation simplifiée permettrait de repérer visuellement certaines formes caractéristiques, notamment la fameuse trajectoire en "8" associée aux danses frétillantes. L’orientation de ces boucles par rapport à la verticale de l’image pourrait être exploitée pour déterminer l’angle de la danse, tandis que la longueur du segment central (la phase de frétillement) donnerait une indication sur la distance annoncée, à condition de connaître le nombre d’images sur lequel elle s’étale. 

À partir de ces images synthétiques, plusieurs stratégies peuvent être envisagées. L’une consiste à entraîner un modèle comme YOLOv10 spécifiquement pour la reconnaissance des formes de trajectoires caractéristiques des danses. Et l’autre, peut-être plus adaptée à la nature binaire des images, serait de recourir à un modèle de segmentation comme U-Net, capable de détecter des motifs spatiaux même dans des contextes visuellement simples. Le choix du modèle reviendrait en quelque sorte à décider entre utiliser un bulldozer ou une pelle pour creuser un château de sable : tout dépend de la précision, de la consommation de ressources et du niveau de généralisation attendu. 

Quoi qu’il en soit, cette étape vise à produire une première reconnaissance automatique des danses, en extrayant les motifs correspondant aux comportements recherchés. Les résultats obtenus resteront probablement imparfaits à ce stade : du bruit, des faux positifs et des trajectoires incomplètes sont à prévoir.

#### Etape 4 - LSTM Découpage
C’est à cette étape que l’usage du LSTM (Long Short-Term Memory) prend tout son sens. Ce type de réseau neuronal récurrent est particulièrement adapté au traitement de séquences temporelles, comme celles issues des danses de nos abeilles. Son rôle ici serait de découper les trajectoires complètes en segments pertinents, en identifiant précisément les moments où commence et se termine les communications. 

Contrairement aux approches basées uniquement sur des caractéristiques visuelles statiques, le LSTM peut prendre en compte la dynamique du mouvement : accélérations, virages, répétitions rythmiques, etc. Il apprend à reconnaître des motifs temporels récurrents qui signalent une danse, même lorsque celle-ci est partiellement masquée ou perturbée par du bruit. On pourrait lui fournir en entrée une séquence de positions (ou leur représentation visuelle dans une série d’images) et lui demander de produire un signal binaire indiquant la présence ou non d’une danse sur chaque intervalle temporel. 

Ce découpage affinerait donc la détection brute de l’étape précédente, en filtrant les faux positifs et en localisant précisément les danses effectives dans la vidéo.

#### Etape 5 - CNN Nettoyage ?
Enfin, le nettoyage. Cette étape s'arbore d'un point d'interrogation car à ce stade je ne sais dire si elle sera nécessaire ou si le LSTM dans sa performance annihilera son besoin. Mais dans l'idée, une fois les séquences candidates extraites et découpées, il reste encore à valider, nettoyer et affiner les détections. C’est là qu’interviendrait un réseau convolutif (CNN), utilisé ici comme un filtre final ou comme un classifieur binaire chargé de confirmer (ou non) la présence d’une danse frétillante. Ce modèle pourrait être entraîné sur un ensemble de séquences annotées pour éliminer les fragments ambigus, incomplets ou trop bruyants, et pour garantir un certain niveau de confiance dans les détections retenues. 

L’objectif n’est pas forcément de faire une classification exhaustive, mais plutôt de nettoyer les résultats précédents en éliminant les erreurs résiduelles et en s’assurant que seules les trajectoires vraiment caractéristiques soient conservées pour l’analyse finale.

### En somme
Nous avons désormais en main les bases scientifiques, techniques et méthodologiques du projet dans lequel s’inscrit mon stage. En recontextualisant les enjeux liés à l’étude des danses frétillantes des abeilles, en présentant la GeoDanceHive et en exposant la problématique de son embarquabilité, nous avons pu cerner les contours d’un défi aussi intéressant que complexe. Ce qui m'offre l'occasion de rappeler que bien que ce stage ne se profilait dans mes intérêts il a merveilleusement su les solliciter.  

Le pipeline théorique détaillé ici illustre l’ambition du projet, mais aussi la vision que j’en avais avant même de mettre les mains dans le charbon. Il constitue une feuille de route précieuse, sur laquelle s’est appuyée la totalité de mon travail. Car, bien qu’il ait été conçu dans l’enthousiasme des premiers jours, il s’est heurté à la réalité du temps, des moyens, et des aléas inhérents à tout travail de recherche. Même à la fin de stage je ne saurais dire si nous n’aurions pas eu un résultat satisfaisant à la fin de l’étape 3. 

Dans le chapitre suivant, nous aurons l'occasion de nous pencher plus profondément sur le déroulé de mon stage, en abordant les choix techniques, les expérimentations, les obstacles rencontrés, les ajustements effectués… et peut-être les surprises qui ont ponctué cette aventure scientifique.