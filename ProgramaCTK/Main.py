from customtkinter import *
from PIL import Image   
import os
from tkinter import messagebox
from CTkTable import CTkTable


class ToplevelWindow(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes"
        
        
        ImgEli_data=Image.open(ruta_con_diagonales+"/Eliminar.png")
        ImgCerrar_data=Image.open(ruta_con_diagonales+"/abierto.png")
        ImgCrear_data=Image.open(ruta_con_diagonales+"/Crear.png")
        ImgGes_data=Image.open(ruta_con_diagonales+"/portapapeles.png")
        
        ImgEli=CTkImage(light_image=ImgEli_data,size=(32,32))
        ImgCerrar=CTkImage(light_image=ImgCerrar_data,size=(32,32))
        ImgCrear=CTkImage(light_image=ImgCrear_data, size=(32,32))
        ImgGes=CTkImage(light_image=ImgGes_data, size=(32,32))

        self.label = CTkLabel(self,image=ImgEli, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes"
        
        ImgEli_data=Image.open(ruta_con_diagonales+"/Eliminar.png")
        ImgCerrar_data=Image.open(ruta_con_diagonales+"/abierto.png")
        ImgCrear_data=Image.open(ruta_con_diagonales+"/Crear.png")
        ImgGes_data=Image.open(ruta_con_diagonales+"/portapapeles.png")
        
        ImgEli=CTkImage(light_image=ImgEli_data,size=(32,32))
        ImgCerrar=CTkImage(light_image=ImgCerrar_data,size=(32,32))
        ImgCrear=CTkImage(light_image=ImgCrear_data, size=(32,32))
        ImgGes=CTkImage(light_image=ImgGes_data, size=(32,32))

        self.button_1 = CTkButton(self,image=ImgEli, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow()  # crea la ventana si es None o está destruida
        else:
            self.toplevel_window.focus()  # si la ventana existe, enfócala



app = App()
app.mainloop()