
##  1. Préparation du matériel

##### ApeStick XL: 
- vérifier que batterie chargée (tubes allumés en vert)
- fixer les aimants ou supports selon l'utilisation

#### Ape Labs Connect Grey :
- Brancher ou utiliser sur batterie (≈ 50 h d’autonomie) 
- Brancher antennes 2,4 GHz.
- Vérifier que la LED de statut est prête (bleue, vert ou rouge selon mode).


## 2. Association des lampes (Pairing)

### ⚙️ Avec smartphone / app Ape Labs

1. Ouvrir l’app Ape Labs (iOS ou Android).
    
2. Connecter le smartphone en BT au Connect (dans un rayon de ~10 m) ([prolighting.de](https://www.prolighting.de/en/apelabs/ape-labs-accessories/ape-labs-connect-grey.html?utm_source=chatgpt.com "APE Labs CONNECT - grey")).
    
3. Dans **Service Mode** :
    
    - Sélectionner **Pairing**.
        
    - Allumer l’ApeStick XL (appui long ~5 s jusqu’à clignotement RGB) ([Ape Labs](https://apelabs.com/software-updates-support/?utm_source=chatgpt.com "Software / Updates / Support - Ape Labs")).
        
    - L’app et lampes clignotent, confirmer la connexion.
        
4. Répéter pour chaque lampe. Le Connect peut gérer jusqu’à 4 univers DMX ([prolighting.de](https://www.prolighting.de/en/apelabs/ape-labs-accessories/ape-labs-connect-grey.html?utm_source=chatgpt.com "APE Labs CONNECT - grey")).
    

### 🪄 Avec télécommande ApeRemote

1. Allumer l’ApeStick XL (appui ~1 s).
    
2. Appuyer sur le bouton **Group** (« +/- ») de la télécommande pour sélectionner le groupe (1 à 4).
    
3. Associer : appuyer simultanément sur le bouton de groupe et sur l’ApeStick. La lampe clignote en bleu pour confirmer ([ManualsLib](https://www.manualslib.com/manual/2803141/Ape-Labs-Apestick4.html?utm_source=chatgpt.com "APE LABS APESTICK4 INSTRUCTION MANUAL Pdf Download | ManualsLib")).
    

---

## 💡 3. Mode d’utilisation

### A. Utilisation directe (Standalone / télécommande)

- **Allumer/Éteindre** : appui long (~1 s) sur l’un des extrémités (lampe) .
    
- **Changer de groupe** : télécommande → boutons +/- groupe.
    
- **Changer programme/définit un blanc/coloration** : appuis courts sur télécommande ; délai avant veille activé.
    
- **Standalone (sans app ni télécommande)** :
    
    - Activer : appui long ~5 s → clignotement RGB ([ManualsLib](https://www.manualslib.com/manual/2803141/Ape-Labs-Apestick4.html?utm_source=chatgpt.com "APE LABS APESTICK4 INSTRUCTION MANUAL Pdf Download | ManualsLib"), [nlfxpro.com](https://www.nlfxpro.com/connect/?utm_source=chatgpt.com "Ape Labs Connect | DMX Transceiver and Controller (Creme)"), [Ape Labs](https://apelabs.com/manual/?utm_source=chatgpt.com "Manual - Ape Labs")).
        
    - Changer presets via appui courts. Idem pour désactivation.
        

### B. Utilisation via Connect / DMX + Lightkey

1. Depuis l’app Ape Labs :
    
    - Activer **Wireless DMX Transmitter** dans Connect ([ManualsLib](https://www.manualslib.com/manual/2803141/Ape-Labs-Apestick4.html?utm_source=chatgpt.com "APE LABS APESTICK4 INSTRUCTION MANUAL Pdf Download | ManualsLib"), [prolighting.de](https://www.prolighting.de/en/apelabs/ape-labs-accessories/ape-labs-connect-grey.html?utm_source=chatgpt.com "APE Labs CONNECT - grey")).
        
    - Définir adresse DMX pour chaque lampe/Groupe (1 à 512) via app.
        
    - Choisir résolution DMX (8-bit ou 16-bit) ([Reddit](https://www.reddit.com/r/lightingdesign/comments/11zzpcu?utm_source=chatgpt.com "Please help a noob. I have absolutely no idea how to use this.")).
        
2. Sur Lightkey :
    
    - Créer un univers DMX correspondant.
        
    - Ajouter lampes avec profil « Generic RGBW 8‑bit/16‑bit » (suivant choix) ([ManualsLib](https://www.manualslib.com/manual/2803141/Ape-Labs-Apestick4.html?utm_source=chatgpt.com "APE LABS APESTICK4 INSTRUCTION MANUAL Pdf Download | ManualsLib")).
        
    - Affecter canaux DMX aux faders/couleurs/intensité selon la table DMX.
        
3. Transmettre le signal DMX via le Connect :
    
    - Le Connect émet sans fil jusqu’à ~1200 m (ligne de vue) ([prolighting.de](https://www.prolighting.de/en/apelabs/ape-labs-accessories/ape-labs-connect-grey.html?utm_source=chatgpt.com "APE Labs CONNECT - grey")).
        
4. Appuyez sur **Play** dans Lightkey, les lampes s’illuminent via DMX.
    

---

## 📊 4. Tableau synthétique comparatif

|Fonction|Télécommande / standalone|Connect + app / Lightkey DMX|
|---|---|---|
|Allumer / éteindre|Appui long (~1 s)|Depuis Lightkey ou app → DMX|
|Changement de groupe|Télécommande (+/- groupe)|App ApeLabs ou DMX|
|Couleurs / programmes|Télécommande (programmes)|Lightkey / app DMX UI|
|Adressage DMX|N/A|App → adresse & résolution|
|Synchronisation|Lampe ↔ lampe cascade automatique|Connect répète + app|
|Autonomie|~8–10 h (lampe)|Connect ~50 h batterie|

---

## 📌 5. Bonnes pratiques et astuces

- **Charge avant chaque service** : chargeur 27 W fourni avec Connect ([Reddit](https://www.reddit.com/r/lightingdesign/comments/gg4e8w?utm_source=chatgpt.com "Connect dmx controller to light"), [Reddit](https://www.reddit.com/r/mobileDJ/comments/1cszmwp?utm_source=chatgpt.com "Upgrading lighting. Questions about Ape Labs connectivity.")).
    
- **Mode Flicker‑Free** : à activer dans app Service Mode pour tournages vidéo (PWM 500–4000 Hz) ([Ape Labs](https://apelabs.com/apelight-apestick/?utm_source=chatgpt.com "ApeStick - ApeLabs")).
    
- **Gardez la portée BT** : smartphone à ≤10 m du Connect .
    
- **Planifiez les adresses DMX** selon la configuration Lightkey (1 univers par groupe).
    
- **Test avant le culte** : envoyer un blackout ou couleur unie via Lightkey pour vérifier chaque lampe.
    

---

## 📑 6. FAQ rapide

**Q : Puis-je sans app ni Connect gérer plusieurs lampes ?**  
R : Non, la télécommande ne gère qu’un seul groupe à la fois. Utilisez l’app ou DMX pour gérer plusieurs univers.

**Q : Comment activer le mode Sound‑Active ?**  
R : Depuis l’app, activer la fonction “Master Microphone” sur le Connect pour synchroniser les lampes à l’audio via DMX ([Reddit](https://www.reddit.com/r/lightingdesign/comments/11zzpcu?utm_source=chatgpt.com "Please help a noob. I have absolutely no idea how to use this."), [nlfxpro.com](https://www.nlfxpro.com/connect/?utm_source=chatgpt.com "Ape Labs Connect | DMX Transceiver and Controller (Creme)")).

**Q : Peut-on piloter avec KNX ?**  
R : Oui, via un adaptateur KNX‑DMX branché sur Connect. Attention, achat supplémentaire requis ([prolighting.de](https://www.prolighting.de/en/apelabs/ape-labs-accessories/ape-labs-connect-grey.html?utm_source=chatgpt.com "APE Labs CONNECT - grey")).

---

Ce guide peut être complété avec des captures Lightkey (ex. paramétrage faders), ou un diagramme de câblage Connect → Lightkey → lampes.

Souhaites-tu que je rédige un PDF finalisé ou inclue une partie visuelle ?