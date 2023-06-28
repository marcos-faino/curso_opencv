import cv2

img = cv2.imread('objetos/objetos.jpg')
img = cv2.resize(img, (600,500))

# colocando em escala de cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# mapeando os contornos das imagens
imgCanny = cv2.Canny(imgCinza, 30, 200) # Os números definem o que é contorno

# Aplicando a morfologia de Close para termos um melhor 'fechamento' de cada objeto
imgClose = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, (7,7))

# Separando os contornos de cada objeto
contornos, hierarquia = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# print(contornos)

# percorrendo os contornos e capturando item por item dos objetos
numOb = 1
for cnt in contornos:
    # mostrando os contornos em azul na imagem original
    #cv2.drawContours(img, cnt, -1, (255,0,0), 2)
    # colocando um retângulo ao redor de cada contorno
    x,y,w,h = cv2.boundingRect(cnt) # capturando x, y, largura e altura dos contornos
    # salvando individualmente cada imagem.
    objeto = img[y:y+h, x: x+w] # recortando a imagem
    cv2.imwrite(f'objetos/objeto{numOb}.jpg', objeto)
    cv2.rectangle(img,(x,y), (x+w, y+h), (255, 0, 0), 2) # desenhando o retângulo
    numOb += 1



cv2.imshow('Imagem', img)
cv2.imshow('Imagem cinza', imgCinza)
cv2.imshow('Imagem Canny', imgCanny)
cv2.waitKey(0)