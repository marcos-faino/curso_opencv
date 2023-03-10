import cv2

camera = cv2.VideoCapture(0)
# setando configurações da camera
camera.set(3, 640) # 3 para setar a largura da imagem
camera.set(4, 360) # 4 para setar a altura da imagem
camera.set(10, 150) # 10 para setar brilho da imagem

while True:
    check, img = camera.read()

    cv2.imshow('web cam', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break