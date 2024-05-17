from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
class Inicio:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.geometry("500x600")
        self.ventana.title("Inicio")
        
        fondo="#F6F4EB"
        
        self.frame_sup=Frame(self.ventana)
        self.frame_sup.configure(bg=fondo)
        self.frame_sup.pack(fill="both", expand=True)
        
        self.frame_inf=Frame(self.ventana)
        self.frame_inf.configure(bg=fondo)
        self.frame_inf.pack(fill="both", expand=True)
        
        #------------------#
        self.titulo=Label(self.frame_sup,
                        text="Ingreso",
                        font=("Poppins",20,"bold"),
                        bg=fondo)
        self.titulo.pack(side="top",pady=20)
        
        
        self.img = Image.open("Imagenes/FaceLink.png")
        self.img=self.img.resize((150,165))
        self.render=ImageTk.PhotoImage(self.img)
        self.fondo=Label(self.frame_sup, image=self.render, bg=fondo)
        self.fondo.pack(expand=True, fill="both", side="top")
        
        
        self.label_usuario = Label(self.frame_inf,
                                text="Usuario",
                                font=("Poppins", 14, "bold"),
                                bg=fondo,
                                fg="black")
        self.label_usuario.place(x=90,y=6,width=70,height=19)
        
        self.BoxUsuario=Entry(self.frame_inf,
                            bd=0,
                            width=25,
                            font=("Poppins", 15))
        self.BoxUsuario.place(x=90,y=25,width=310,height=35)
        
        
        self.label_contrasena = Label(self.frame_inf,
                                   text="Contraseña",
                                   font=("Poppins", 14, "bold"),
                                   bg=fondo,
                                   fg="black")
        self.label_contrasena.place(x=90,y=60,width=110,height=19)
        
        self.Boxcontrasena=Entry(self.frame_inf,
                              bd=0,
                              width=25,
                              font=("Poppins", 15),
                              show="*")
        self.Boxcontrasena.place(x=90,y=79,width=310,height=35)
        
        self.botonIngresar=Button(self.frame_inf,
                                  text="Ingresar",
                                  width=7,
                                  height=0,
                                  font=("Poppins",12))
        self.botonIngresar.place(x=300,y=118,width=100,height=30)
        
        self.botonSalir=Button(self.frame_inf,
                                  text="Salir",
                                  width=7,
                                  height=0,
                                  font=("Poppins",12))
        self.botonSalir.place(x=90,y=118,width=100,height=30)
        
        
        mainloop()






Inicio()