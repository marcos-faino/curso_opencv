# Binarização de imagens.
import cv2

img = cv2.imread('img02.jpg')
img = cv2.resize(img,(700, 800))

imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# preciso de duas variáveis para esse processo
# então chamamos a primeira variável de _
# o valor 127 é o limite da intensidade de cor que deve ser considerada
# para definir se o valor é preto ou branco
_, th1 = cv2.threshold(imgCinza, 127, 255, cv2.THRESH_BINARY)

# primeira forma de adaptação
th2 = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 16)

# segunda forma de adaptação
th3 = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 16)

cv2.imshow('Original', img)
cv2.imshow('TH1', th1)
cv2.imshow('TH2', th2)
cv2.imshow('TH3', th3)
cv2.waitKey(0)