---
Date: 2025-05-20
tags:
  - communication
---
Bonjour l'équipe !

En cette Journée internationale des abeilles 🐝, je me permets de vous envoyer ce petit message pour vous faire part de mon besoin d’aide 😊  
Pour celleux qui ne le savent pas encore, je travaille sur le projet **Geo Dance Hive**, dans lequel nous essayons d’implémenter un algorithme de deep learning capable de reconnaître les abeilles qui dansent sur les cadres.

Comme vous vous en doutez, qui dit IA dit données… et entraînement !

 🐝 C’est là que vous intervenez 🐝  
Malheureusement, je ne dispose pas encore d’assez de données annotées pour entraîner le modèle. L’annotation est longue (~20 minutes par image), et j’avance lentement car la tâche est fatigante.  
C’est pourquoi je vous propose une petite activité collective (🕺)

### Le concept est simple :
Si, dans votre journée, vous avez envie de m’aider et de faire une pause de 10 minutes dans vos travaux, vous pouvez annoter quelques images pour moi en dessinant des boîtes autour des abeilles visibles sur mes photos.

### 🤓 Comment faire ?
Il vous suffit de **réagir à ce message** pour que je vous ajoute comme contributeur·ice à mon dataset sur Roboflow.  
Vous aurez alors accès à un dossier contenant une centaine d’images non annotées.

Dès qu’une boîte est dessinée sur une image, celle-ci passe automatiquement dans la catégorie des images annotées.  
Cependant, comme il y a souvent une grosse centaine d’abeilles par cadre, une seule boîte ne suffit pas à considérer l’image comme « terminée ».  
Pour cela, je vous propose qu’on ajoute un **tag `NotFinished`** (disponible dans l’onglet "Labels" en mode annotation) tant que toutes les abeilles visibles n’ont pas été entourées.  
Ainsi, vous aurez le choix : commencer une nouvelle image, ou continuer une image déjà entamée.

### 📌 Quelques consignes de labélisation :

- Dessinez une boîte autour de chaque forme que vous identifiez comme une abeille, même si elle est floue.
- Ne pas annoter les tâches trop petites ou douteuses.
- Je vous deconseille d’utiliser le système d’annotation intelligent : il génère souvent des boîtes approximatives et pénibles à corriger.
- En cas de doute, vous pouvez consulter l'image `up0000028020.jpg` dans l’onglet "annotées", que j’ai moi-même labélisée (mais qui n'est pas parfaite).

Je crée ce canal Abeilles si jamais vous avez des remarques à faire relatives à ce sujet. 

Voilà, je crois que j’ai fait le tour !  
**Réagissez à ce message** si vous êtes partant·e·s, afin que je puisse ajouter votre e-mail aux contributeur·ices.

Merci à toustes, et belle journée à vous 🌼  
**Bzz Bzz**🍯

---
# Petit complément 
Lorsque je vous ajoute, vous recevez un mail (sur votre boite IGN), vous devez alors vous créer un compte si vous n'en avez pas déjà un. Ensuite on vous demandera de nommer votre workspace (mettez ce que vous voulez). Un fois sur votre page d'accueil, changez votre workspace (en haut à gauche) pour **GeoDanceHive**. Dès que vous avez changé, allez dans **Annotate** puis **Burst3** pour rentrer dans le dossier d'image à libeller. 
Vous y êtes, vous voyez désormais les deux onglets Unannotated/Annotated. 🐝💛