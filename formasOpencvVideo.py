import cv2

video = cv2.VideoCapture('runners.mp4')

while True:
    check, img = video.read()
    # parâmetros: imagem, (px inicial),(px final), (corRGB), espessura(-1) preenche a forma
    cv2.rectangle(img, (50,50), (200,200), (255,0,0), 3)
    cv2.circle(img, (220,200), 50, (0,0,255), 3)
    cv2.line(img, (300,400), (500, 400), (24, 255,0), 3)

    texto = 'Correeee Galeraaaaa'
    cv2.putText(img, texto, (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 34, 0), 2)

    cv2.imshow('Imagem', img)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break  #0 ver frame a frame