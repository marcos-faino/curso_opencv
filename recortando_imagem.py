import cv2

img = cv2.imread('farol.jpg')

#recortando com opencv
dim = cv2.selectROI("Selecione a área a recortar",
                    img,
                    False) # retorna os números das coordenadas
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])


recorte = img[v2:v2+v4, v1:v1+v3]


#abrir a imagem no paint e marcar as os valores para os eixos x e y

#recorte = img[310:520, 120:420]


cv2.imshow('Original', img)
cv2.imshow('Recorte', recorte)

cv2.waitKey(0)