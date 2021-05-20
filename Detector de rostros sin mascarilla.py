
from matplotlib import pyplot
import imutils
import os
from mtcnn.mtcnn import MTCNN
import cv2

nombre = 'Sin_tapabocas'
direccion = 'E:/Documentos/Universidad/7 Semestre/4 Analisis de Sistemas I/Proyecto de clase/fotos'
carpeta = direccion + '/' + nombre



#si la carpeta no existe se creara
if not os.path.exists(carpeta):
    os.makedirs(carpeta)



detector = MTCNN()
cap = cv2.VideoCapture(0)
count = 0 







        
