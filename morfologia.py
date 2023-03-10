import cv2

img = cv2.imread('piramide.jpg')
img = cv2.resize(img, (500, 400))
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# os números reference a qtd de linhas e colunas que sofrerão alteração na imagem
# o zero é o sigma
imgBlur = cv2.GaussianBlur(imgCinza, (7,7),0)
#para achar os contornos da imagem
# passar o valor de thrash road (limite de confiança) para considerar a diferenciação de cor entre o contorno e o que não é contorno
imgCanny = cv2.Canny(img, 50, 100)
#dilatação da imagem
# expande os pontos da imagem. Passo a imagem e a matriz que informa a quantidade linhas e colunas que serão alteradas
imgDilat = cv2.dilate(imgCanny, (5,5), iterations=5)
# contrário da dilatação
imgErode = cv2.erode(imgCanny, (5,5), iterations=2)
# usando dilate e erode de uma só vez
imgOpening = cv2.morphologyEx(imgCanny, cv2.MORPH_OPEN, (5,5))
imgClosing = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, (5,5))


# cv2.imshow('Img Original', img)
# cv2.imshow('Img Cinza', imgCinza)
# cv2.imshow('Img Blur', imgBlur)
cv2.imshow('Img Canny', imgCanny)
# cv2.imshow('Img Dilatada', imgDilat)
# cv2.imshow('Img Erode', imgErode)
cv2.imshow('Img Open', imgOpening)
cv2.imshow('Img Close', imgClosing)
cv2.waitKey(0)