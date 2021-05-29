from tkinter import *
from typing import ContextManager 


raiz=Tk()

def abrirarchivo():
   import Reconocimiento_facial 

def abrirarchivo2():
   import Detector_de_rostros_sin_mascarilla 

def abrirarchivo3():
   import Detector_Con_cubrebocas 

def abrirarchivo4():
   import Entrenamiento 


raiz.title("Detector de rostros")
raiz.resizable(False,False)

miframe=Frame(raiz, width=620, height=480)
miframe.pack()


Label(miframe, text="Registro y captura ", fg="red", font=("Comic Sans MS", 14)).place(x=50,y=30)

miImagen=PhotoImage(file="conmas.png")
Label(miframe, image=miImagen).place(x=70, y=80)

Abrircon=Button(raiz, text="Registro con mascarilla" , command=abrirarchivo3)
Abrircon.place(x=50, y=170)

miImagen2=PhotoImage(file="sinmas.png")
Label(miframe, image=miImagen2).place(x=70, y=210)

Abrirsin=Button(raiz, text="Registro sin mascarilla" , command=abrirarchivo2)
Abrirsin.place(x=50, y=300)


miImagen3=PhotoImage(file="perfil.png")
Label(miframe, image=miImagen3).place(x=360, y=100)

Abrirpy=Button(raiz, text="Iniciar Reconocimiento" , command=abrirarchivo)
Abrirpy.place(x=350, y=210)



Label(miframe, text="Creación de Modelo", fg="red", font=("Comic Sans MS", 14)).place(x=50,y=350)

Abrirmodelo=Button(raiz, text="Crear Modelo" , command=abrirarchivo4)
Abrirmodelo.place(x=50, y=400)


raiz.mainloop()