import pyautogui
import time
import sys
from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, PhotoImage


def exit_program():
    ventana.quit  

#===========================================================================
#CONFIGURACION DE VENTANA PRINCIPAL
#===========================================================================





ventana = tk.Tk()
ventana.title("Awaker_ Pancho rey 2022")
ventana.geometry("300x150")
ventana.configure(background="Green")




extra_window = tk.Toplevel(ventana)
label2 = tk.Label(extra_window, text="this is extra_window closing this will not affect root")
label2.pack()
extra_window.withdraw()

    
#===========================================================================
#CONFIGURACION DE LA BARRA DE MENUS
#===========================================================================

menubar = Menu(ventana)


#PESTAÑA ARCHIVO
Archivomenu = Menu(menubar, tearoff=0)
Archivomenu.add_command(label="Ejecutar", command=exit_program)
Archivomenu.add_separator()


Archivomenu.add_command(label="Salir", command=ventana.quit)
menubar.add_cascade(label="Archivo", menu=Archivomenu)



ventana.config(menu=menubar)


# FRAME DE LA PARTE DE ARRIBA PARA LOS BOTONES DE IMPORTACION

    #TITULO DEL FRAME DE IMPORTACION
file_frame = tk.LabelFrame(ventana, text="")
    #TAMAÑO DEL FRAME DE IMPORTACION
file_frame.place(height=30, width=40, x=75, y=50)
    #COLORES DEL FRAME DE IMPORTACION
file_frame.config(bg="Orange", fg="white")




    #BOTON DE IMPORTACION DE CATALOGO, ASIGANDO LA FUNCION DE IMPORTARCAT
button1 = tk.Button(file_frame, text="Inicio", command=lambda: inicio()())
    #UBICACION DE BOTON DENTRO DE LA VENTANA PRINCIPAL
button1.place(rely=0, relx=0)


#===========================================================================



def inicio():
    pyautogui.password(text='Favor de introducir contraseña de usuario', title='Contraseña perro', default='Holi', mask='*')
    pyautogui.FAILSAFE = False
    numMin = None
    if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
        numMin = 1
    else:
        numMin = int(sys.argv[1])
    while(True):
        x=0
        while(x<numMin):
            time.sleep(10)
            x+=1
        for i in range(0,20):
            pyautogui.moveTo(50,i*10)
        for i in range(0,1):
            pyautogui.click(x=500, y=10, clicks=1, button='left')
        print("Movement made at {}".format(datetime.now().time()))
    
    
ventana.mainloop()


    
