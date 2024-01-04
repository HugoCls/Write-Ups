import cv2
from pwn import xor

img1 = cv2.imread('img1.png')

img2 = cv2.imread('img2.png')

print(img1)

hauteur, largeur, _ = img1.shape  # Ignorer le canal alpha (_)

# Parcourir chaque pixel de l'image
for y in range(hauteur):
    for x in range(largeur):
        # Obtenir la valeur du pixel à la position (x, y)
        pixel1 = img1[y, x]
        pixel2 = img2[y, x]

        for j in range(3):
            pixel1[j] = pixel1[j] ^ pixel2[j]

cv2.imshow("adzad", img1)
cv2.waitKey(0)