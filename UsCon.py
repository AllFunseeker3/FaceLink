from tkinter import *
from tkinter import ttk

class Inicio:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.geometry("400x500")
        self.ventana.title("Inicio")
        
        fondo="#FFF7F1"
        
        self.frame_sup=Frame(self.ventana)
        self.frame_sup.configure(bg=fondo)
        self.frame_sup.pack(fill="both", expand=True)
        
        self.frame_inf=Frame(self.ventana)
        self.frame_inf.configure(bg=fondo)
        self.frame_inf.pack(fill="both", expand=True)
        
        self.frame_inf.columnconfigure(0, weight=1)
        self.frame_inf.columnconfigure(1, weight=1)
        
        #------------------#
        self.titulo=Label(self.frame_sup,
                          text="Ingreso",
                          font=("Poppins",20,"bold"),
                          bg=fondo)
        self.titulo.pack(side="top",pady=20)
        
        self.label_usuario = Label(self.frame_inf,
                                   text="Usuario",
                                   font=("Poppins", 10, "bold"),
                                   bg=fondo,
                                   fg="black")
        self.label_usuario.grid(row=0, column=0,padx=1, sticky="e")
        
        self.BoxUsuario=Entry(self.frame_inf,
                              bd=0,
                              width=25,
                              font=("Poppins", 10))
        self.BoxUsuario.grid(row=1, column=0,columnspan=3,padx=10, sticky="s")
        
        
        self.label_contrasena = Label(self.frame_inf,
                                   text="Contraseña",
                                   font=("Poppins", 10, "bold"),
                                   bg=fondo,
                                   fg="black")
        self.label_contrasena.grid(row=4, column=0,pady=1, sticky="e")
        
        self.Boxcontrasena=Entry(self.frame_inf,
                              bd=0,
                              width=25,
                              font=("Poppins", 10),
                              show="*")
        self.Boxcontrasena.grid(row=5, column=0,columnspan=3,padx=10, sticky="s")
        
        self.botonIngresar=Button(self.frame_inf,
                                  text="Ingresar",
                                  width=7,
                                  height=0,
                                  font=("Poppins",12))
        self.botonIngresar.grid(row=6, column=1,columnspan=2, pady=30, sticky="n")
        
        self.botonSalir=Button(self.frame_inf,
                                  text="Salir",
                                  width=7,
                                  height=0,
                                  font=("Poppins",12))
        self.botonSalir.grid(row=6, column=0,columnspan=2, pady=30, sticky="n")
        
        
        mainloop()

        

Inicio()