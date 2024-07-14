import os 
import tkinter as tk

from tkinter import PhotoImage
from PIL import Image, ImageTk
from AI.ai import generar_resumen, generar_texto, tokenize_text
from database import leer_entradas, actualizar_entrada, agregar_entrada, eliminar_entrada
from datetime import datetime


def create_menu():
    while True:
        print("\nNotas Personales")
        print("1. Agregar nueva entrada")
        print("2. Buscar entradas")
        print("3. Actualizar una entrada")
        print("4. Eliminar una entrada")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M')
            titulo = input("Título: ")
            contenido = input("Contenido: ")
            agregar_entrada(fecha_actual, titulo, contenido)
        elif opcion == '2':
            id_entrada= int(input("ID de la entrada a buscar: "))
            entrada= leer_entradas(id_entrada)
            if entrada:
                    print(f"ID: {entrada[0]}")
                    print(f"Fecha: {entrada[1]}")
                    print(f"Título: {entrada[2]}")
                    print(f"Contenido: {entrada[3]}\n")
                    input()
                    while True:
                        print("\n1. Resumirlo\n")
                        print("2. Generar texto aleatorio\n")
                        print("3. Regresar\n")
                        print("4. Volver al menu principal\n")
                        ans= input()
                        if ans == '1':
                            try:
                                token_count= tokenize_text(entrada[3])
                                resumen_generado= generar_resumen(entrada[3], token_count)
                                print(resumen_generado)    
                            except Exception as error:
                                print(f"Error durante la generacion del resumen {error}")
                        elif ans== '2':
                            try:
                                texto_generado= generar_texto(entrada[3])
                                print(texto_generado)    
                            except Exception as error: 
                                print(f"Error durante la generacion de texto {error}")
                        elif ans== '3':
                            break     
                        elif ans == '4':
                            return
        elif opcion == '3':
            id_entrada = int(input("ID de la entrada a actualizar: "))
            nuevo_titulo = input("Nuevo título: ")
            nuevo_contenido = input("Nuevo contenido: ")
            actualizar_entrada(id_entrada, nuevo_titulo, nuevo_contenido)
        elif opcion == '4':
            id_entrada = int(input("ID de la entrada a eliminar: "))
            eliminar_entrada(id_entrada)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            input()
            os.system("cls")


    
create_menu()

def create_ui():
    #resize images 
    def adapt_image(button, image_path):
        def resize_image(event):
            new_width= event.width
            new_height= event.height
            original_image= Image.open(image_path)
            resized_image= original_image.resize((new_height, new_width), Image.LANCZOS)
            photo_image= ImageTk.PhotoImage(resized_image)
            button.config(image=photo_image)
            button.image= photo_image
        button.bind("<Configure>", resize_image) 

    #main window
    window= tk.Tk()
    window.title("NOTEAI")
    window.geometry("500x768")
    window.iconbitmap("images/noteia.ico")
    window.configure(bg="gray5")
    window.configure(bg="gray5")
    window.attributes("-alpha", 0.9)
    window.resizable(False,False)

    #newnote
    """""
    newnote_frame= tk.Frame(window)
    newnote_frame.config(width=500, height= 40, bg="gray12", bd= 5)
    newnote_frame.pack()
    """""
    #search frame
    search_frame= tk.Frame(window)
    search_frame.config(width=480, height= 45, bg="gray24", bd=3)
    search_frame.place(x=10,y=5)

    search_button= tk.Button(search_frame, text= "Búsqueda", anchor="w",  
                            width=55, height=0, bg="gray24", bd=0)
    search_button.place(x=45,y=1)

    config_button= tk.Button(search_frame, width=35, height=35, bg="gray20", bd=0)
    adapt_image(config_button, "images/three-horizontal-lines.png")
    config_button.place(x=1,y=1)

    sort_button= tk.Button(search_frame, 
                            width=35, height=35, bg="gray20", bd=0)
    adapt_image(sort_button, "images/two-horizontal-lines.png")
    sort_button.place(x=435, y=1)

    window.mainloop()
    
    