import keyboard
import cv2

# lendo uma imagem
# img = cv2.imread('farol.jpg')
# transformando em escala de cinza
# imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# print(img.shape)
# print(imgCinza.shape)
# print(imgCinza)

# cv2.imshow('Imagem', img)
# cv2.imshow('Imagem Cinza', imgCinza)

# cv2.waitKey(0)

video = cv2.VideoCapture('runners.mp4')

while True:
    check, img = video.read()
    # se quiser redimensionar a imagem
    imgRedim = cv2.resize(img, (640,420))
    cv2.imshow('video', imgRedim)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break  #0 ver frame a frame

