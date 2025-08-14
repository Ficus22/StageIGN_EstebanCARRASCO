import json
import matplotlib.pyplot as plt
import itertools

# === Paramètres ===
fichier_json = "NByteTrack9-float.json"  # Chemin vers ton fichier

# === Chargement du JSON ===
with open(fichier_json, "r") as f:
    data = json.load(f)

# === Création du graphique 2D ===
plt.figure(figsize=(8, 6))

# Générateur infini de couleurs
couleurs = itertools.cycle(plt.cm.tab20.colors)  # 20 couleurs distinctes

for cle, quadruplets in data.items():
    x_vals = []
    y_vals = []
    for (x1, y1, x2, y2) in quadruplets:
        dx = x1 + (x2 - x1)/2
        dy = y1 + (y2 - y1)/2
        x_vals.append(dx)
        y_vals.append(dy)

    # Courbe en 2D
    plt.plot(x_vals, y_vals, label=f"Index {cle}", color=next(couleurs))

# === Légendes et mise en page ===
plt.xlabel(r"$x_{centre}$")
plt.ylabel(r"$y_{centre}$")
plt.title("Tracé de toutes les trajectoires")
plt.grid(False)
plt.axis('equal')


# === Affichage ou sauvegarde ===
plt.show()
plt.savefig("AllTrajectoires.svg")
