from matplotlib import pyplot
import imutils
import os
from mtcnn.mtcnn import MTCNN
import cv2

nombre = 'Con_tapabocas'
direccion = 'E:/Documentos/Universidad/7 Semestre/4 Analisis de Sistemas I/Proyecto de clase/fotos'
carpeta = direccion + '/' + nombre



#si la carpeta no existe se creara
if not os.path.exists(carpeta):
    os.makedirs(carpeta)



detector = MTCNN()
cap = cv2.VideoCapture(0)
count = 0 



while True:
    ret, frame = cap.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    copia= frame.copy()

    #detector de rostro 
    caras= detector.detect_faces(copia)



    for i in range(len (caras)):
        x1,y1, ancho, alto = caras[i]['box']
        x2,y2 = x1 + ancho, y1 + alto
        cara_reg = frame [y1:y2, x1:x2]
        cara_reg = cv2.resize(cara_reg, (150,200), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(carpeta + "/rostro_{}.jpg".format(count), cara_reg)
        count = count + 1
    cv2.imshow("Entrenamiento", frame)

    t= cv2.waitKey(1)
    if t== 27 or count >=300:
        break 

cap.realease()
cv2.destroyAllWindows()





        