import cv2
import os
import numpy as np

#---------------- Importacion de fotos anteriores -----------------------------------------
direccion = 'E:/Documentos/Universidad/7 Semestre/4 Analisis de Sistemas I/Proyecto de clase/fotos'
lista = os.listdir(direccion)

etiquetas = []
rostros = []
con = 0

for nameDir in lista: 
    nombre = direccion +'/' + nameDir

    for fileName in os.listdir(nombre): 
        etiquetas.append(con)
        rostros.append(cv2.imread(nombre + '/' +  fileName,0))

    con = con + 1


#--------------------- Creamos el Modelo ------------------------------------------
reconocimiento = cv2.face.LBPHFaceRecognizer_create()




#---- Empieza a entrenar con las fotos
reconocimiento.train(rostros, np.array(etiquetas))

#guarda el modelo
reconocimiento.write('modeloLBP.xml')
print("Modelo Creado")