from customtkinter import *
from PIL import Image   
import os
from tkinter import messagebox
from CTkTable import CTkTable



class UsuCon():
    def cerrar(self):
        
        self.Des=messagebox.askquestion("¿Salir?","¿Quieres salir del programa?")
        if self.Des=="yes":
            self.ventana.quit()
            self.ventana.destroy()

                

    def Abrir(self):
        self.ventana.quit()
        self.ventana.destroy()
        self.Principal=Principal()
    
    def __init__(self):
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes/FaceLink.png"


        
        self.ventana=CTk()
        self.ventana.title("Face-link")
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = 414
        alto_ventana = 511
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana.resizable(0, 0)
        #self.ventana.propagate(0)
        #self.ventana.overrideredirect(True)
        self.ventana._set_appearance_mode("light")
        
        self.almacenador=CTkFrame(master=self.ventana,width=414,height=511,fg_color="#F6F4EB")
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True)
        
        LogoP_data = Image.open(ruta_con_diagonales)
        LogoP=CTkImage(light_image=LogoP_data,size=(180,180))
        
        self.LBLogo=CTkLabel(master=self.almacenador,text="",image=LogoP,bg_color="#F6F4EB").place(x=117,y=47)
        
        self.LBUs=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Usuario",font=("Poppins",20,"bold")).place(x=48,y=259)
        self.TxBoxUs=CTkEntry(master=self.almacenador,width=310,height=35,text_color="#000000",font=("Poppins",20,"bold"),fg_color="#E0E0E0",corner_radius=10).place(x=48,y=286)

        self.LBCon=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Contraseña",font=("Poppins",20,"bold")).place(x=48,y=342)
        self.TxBoxCon=CTkEntry(master=self.almacenador,width=310,height=35,text_color="#000000",font=("Poppins",20,"bold"),show="*",fg_color="#E0E0E0",corner_radius=10).place(x=48,y=372)        
        
        self.botonIngresar = CTkButton(master=self.almacenador ,text="Ingresar", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16),command=self.Abrir).place(x=241, y=447)

        self.botonSalir = CTkButton(master=self.almacenador, text="Salir", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16),command=self.cerrar).place(x=48, y=447)
        
        self.ventana.mainloop()

class Principal:
    def cerrar(self):
        
        self.Des=messagebox.askquestion("Cerrar sesión?","¿Quíeres cerrar tu sesión?")
        if self.Des=="yes":
            self.ventana.quit()
            self.ventana.destroy()
            UsuCon()
    
    def Abrir(self):
        self.ventana.quit()
        self.ventana.destroy()
        Empleados()
        
    def __init__(self):
        self.ventana=CTk()
        self.ventana.title("Face-link")
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = 797
        alto_ventana = 473
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana.resizable(0, 0)
        #self.ventana.propagate(0)
        #self.ventana.overrideredirect(True)
        self.ventana._set_appearance_mode("light")
        
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes"


        #FramePrincipal
        self.almacenador=CTkFrame(master=self.ventana,width=624,height=512,fg_color="#F6F4EB",corner_radius=0)
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True,side="right")
        
        self.LBRegistros=CTkLabel(master=self.almacenador,text="Registros", bg_color="#F6F4EB",text_color="#4682A9",font=("Poppins",25,"bold")).place(x=15,y=21)
       
        datos=[
            ["Nombre","Apellido Paterno","Apellido Materno","Fecha","Hora de ingreso","Hora de salida"],
            ["Juan","Jose","Jose","1/8/2024","1:00PM","7:00PM"]
            ]
        self.tablamarco=CTkScrollableFrame(master=self.almacenador,fg_color="transparent")
        self.tablamarco.pack(expand=True, fill="both", padx=27, pady=50)
        self.tabla=CTkTable(master=self.tablamarco, values=datos,colors=["#F6F4EB", "#EEEEEE"],header_color="#4682A9")
        self.tabla.edit_row(0, text_color="#F6F4EB", hover_color="#2A8C55")
        self.tabla.pack(expand=True)
        #FrameLateral
        self.almacenador2=CTkFrame(master=self.ventana,width=176,height=512,fg_color="#4682A9",corner_radius=0)
        self.almacenador2.pack_propagate(0)
        self.almacenador2.pack(expand=True,side="left")     
        LogoP_data = Image.open(ruta_con_diagonales+"/FaceLink.png")
        LogoP=CTkImage(light_image=LogoP_data,size=(64,64))
        
        ImgEmp_data=Image.open(ruta_con_diagonales+"/Empleados.png")
        ImgCerrar_data=Image.open(ruta_con_diagonales+"/abierto.png")
        ImgEmp=CTkImage(light_image=ImgEmp_data,size=(32,32))
        ImgCerrar=CTkImage(light_image=ImgCerrar_data,size=(32,32))
        self.LBLogo=CTkLabel(master=self.almacenador2,text="",image=LogoP,bg_color="#4682A9").pack(pady=(38, 0), anchor="center")
        self.botonEmp = CTkButton(master=self.almacenador2  ,image=ImgEmp,text="Empleados",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=160, font=("Poppins", 16,"bold"),corner_radius=0,command=self.Abrir).pack(anchor="center", ipady=5, pady=(16, 0))
        self.botonCerrar = CTkButton(master=self.almacenador2,image=ImgCerrar,text="Cerrar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=160, font=("Poppins", 16,"bold"),corner_radius=0,command=self.cerrar).pack(anchor="center", ipady=5, pady=(16, 0))
        
        self.ventana.mainloop()
        
class Empleados():
    def Cerrar(self):
        self.ventana2.quit()
        self.ventana2.destroy()
    def __init__(self):
        self.ventana2=CTk()
        self.ventana2.title("Face-link")
        ancho_pantalla = self.ventana2.winfo_screenwidth()
        alto_pantalla = self.ventana2.winfo_screenheight()
        ancho_ventana = 595
        alto_ventana = 404
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.ventana2.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana2.resizable(0, 0)
        #self.ventana.propagate(0)
        #self.ventana.overrideredirect(True)
        self.ventana2._set_appearance_mode("light")
        
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes"
        
        self.almacenador=CTkFrame(master=self.ventana2,width=595,height=324,fg_color="#F6F4EB",corner_radius=0)
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True,side="top", fill="both")
        
        self.almacenador2=CTkFrame(master=self.ventana2,width=595,height=80,fg_color="#4682A9",corner_radius=0)
        self.almacenador2.pack_propagate(0)
        self.almacenador2.pack(expand=True,side="bottom", fill="both")
        
        ImgEmp_data=Image.open(ruta_con_diagonales+"/Empleados.png")
        ImgCerrar_data=Image.open(ruta_con_diagonales+"/abierto.png")
        ImgEmp=CTkImage(light_image=ImgEmp_data,size=(32,32))
        ImgCerrar=CTkImage(light_image=ImgCerrar_data,size=(32,32))
        
        self.botonregresar = CTkButton(master=self.almacenador2  ,image=ImgEmp,text="Cerrar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=114, font=("Poppins", 16,"bold"),corner_radius=0,command=self.Cerrar).pack(side="left")
        self.botoneliminar = CTkButton(master=self.almacenador2,image=ImgCerrar,text="Eliminar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=114, font=("Poppins", 16,"bold"),corner_radius=0).pack(side="left")
        self.botongestionar = CTkButton(master=self.almacenador2  ,image=ImgEmp,text="Gestionar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=114, font=("Poppins", 16,"bold"),corner_radius=0).pack(side="left")
        self.botonnuevo = CTkButton(master=self.almacenador2,image=ImgCerrar,text="Nuevo",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=114, font=("Poppins", 16,"bold"),corner_radius=0).pack(side="left")
        
        
        
        self.ventana2.mainloop()

        
    
UsuCon()