## Pour copier un fichier d'une machine à l'autre :
#### Local > SSH
Se mettre dans le dossier du fichier concerné
```bash
scp -O fichier.txt ecarrasco@del2304s004.ign.fr:/home/ECarrasco/destination
```

#### SSH > Local
Se mettre dans le dossier d'arrivé
```bash
scp -O ecarrasco@del2304s004.ign.fr:/home/ECarrasco/fichier.txt destination/du/fichier.txt
```

## Pour copier un dossier d'une machine à l'autre :
#### Local > SSH
Se mettre dans le dossier parent du dossier concerné
```bash
scp -rO dossier ecarrasco@del2304s004.ign.fr:/home/ECarrasco/destination
```

#### SSH > Local
Se mettre dans le dossier d'arrivé
```bash
scp -rO ecarrasco@del2304s004.ign.fr:/home/ECarrasco/dossier destination/du/dossier
```
