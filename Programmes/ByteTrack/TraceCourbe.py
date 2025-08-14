import json
import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt

plt.ion()


filename = "TrackTrajectories.json"

# Clés à conserver
cles_retenues1 = {"69", "146", "169", "383"}
cles_retenues2 = {"17","766", "582"}

# Pour stocker les points (x2-x1, y2-y1)
x_vals1 = []
y_vals1 = []
x_vals2 = []
y_vals2 = []
z_vals = []

# Chargement du fichier JSON
with open(filename, "r") as f:
    data = json.load(f)


for cle in cles_retenues1:
    if cle in data:
        for i, (x1, y1, x2, y2) in enumerate(data[cle]):
            dx = x1 + (x2 - x1)/2
            dy = y1 + (y2 - y1)/2
            x_vals1.append(dx)
            y_vals1.append(dy)
            z_vals.append(i)

# for cle in cles_retenues2:
#     if cle in data:
#         for x1, y1, x2, y2 in data[cle]:
#             dx = x1 + (x2 - x1)/2
#             dy = y1 + (y2 - y1)/2
#             x_vals2.append(dx)
#             y_vals2.append(dy)

# Tracé de la courbe
plt.figure(figsize=(6, 6))

## Courbes ##
plt.plot(x_vals1, y_vals1, color="red")
# plt.plot(x_vals2, y_vals2)

## Nuage de points ##
# plt.scatter(x_vals1, y_vals1, color="blue", s=5)
# plt.scatter(x_vals2, y_vals2, color="red", s=5)

plt.xlabel(r"$x_{centre}$")
plt.ylabel(r"$y_{centre}$")
plt.title("Tracé de la dance N°1")
plt.grid(False)
plt.axis('equal')  # Pour garder les proportions
plt.savefig("Dance1.svg")
plt.show()

##### Création du graphique 3D #####
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')

# # Tracé d'une courbe 3D reliant les points dans l'ordre
# ax.plot(x_vals1, y_vals1, z_vals, color='blue', linewidth=1.5)

# # Légendes et titre
# ax.set_xlabel(r"$x_2 - x_1$")
# ax.set_ylabel(r"$y_2 - y_1$")
# ax.set_zlabel("Index incrémenté")
# ax.set_title("Courbe 3D des points filtrés (17, 582, 766)")

# plt.show()
# input("Appuyez sur Entrée pour fermer...")
