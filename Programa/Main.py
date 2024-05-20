from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


#-------Clase de Usuario/Contraseña----------
class Main:
    #--------------Funciones------------
    def cerrar(self):
        self.ventana.destroy()

    def AbrirP(self):
        self.ventana.destroy()
        Principal() 
    #-----------------Ventana----------
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
                                font=("Poppins",12),
                                command=self.AbrirP
                                )
        self.botonIngresar.place(x=300,y=118,width=100,height=30)
        
        self.botonSalir=Button(self.frame_inf,
                                text="Salir",
                                width=7,
                                height=0,
                                font=("Poppins",12),
                                command=self.cerrar)
        self.botonSalir.place(x=90,y=118,width=100,height=30)
        
        mainloop()    
    
    
#-------Clase de ventana de inicio----------

class Principal: 
    #-------Funciones--------------
    def regresarMain(self):
        self.ventana.destroy()
        Main()
    #-------------Ventana---------
    def __init__(self):
        self.ventana=Tk()
        self.ventana.geometry("657x573")
        self.ventana.title("Face-link")    
        fondo="#F6F4EB"
        self.ventana.config(bg=fondo)
        
        self.LBRegis=Label(self.ventana,
                           text="Registros del dia",
                           font=("Poppins",16),
                           bg=fondo)
        self.LBRegis.place(x=50,y=10, width=200,height=25)
        #--------------Primer registro-----------
        self.LBFecha=Label(self.ventana,
                           text="Fecha:",
                           font=("Poppins",16),
                           bg=fondo)
        self.LBFecha.place(x=68,y=50, width=70,height=25)
        
        #------Tabla-----------
        self.Tbregistros=ttk.Treeview(self.ventana,
                                      columns=("col1","col2"))
        self.Tbregistros.column("#0",width=80)
        self.Tbregistros.column("col1",width=80,anchor=CENTER)
        self.Tbregistros.column("col2",width=80,anchor=CENTER)
        
        self.Tbregistros.heading("#0",text="Nombre", anchor=CENTER)
        self.Tbregistros.heading("col1",text="Hora de ingreso", anchor=CENTER)
        self.Tbregistros.heading("col2",text="Hora de salida", anchor=CENTER)
        self.Tbregistros.place(x=68,y=90, width=400,height=200)
        
         #--------------Segundo registro-----------
        self.LBFecha2=Label(self.ventana,
                           text="Fecha:",
                           font=("Poppins",16),
                           bg=fondo)
        self.LBFecha2.place(x=68,y=295, width=70,height=25)
        
        #-------------Tabla--------------------
        self.Tbregistros2=ttk.Treeview(self.ventana,
                                      columns=("col1","col2"))
        self.Tbregistros2.column("#0",width=80)
        self.Tbregistros2.column("col1",width=80,anchor=CENTER)
        self.Tbregistros2.column("col2",width=80,anchor=CENTER)
        
        self.Tbregistros2.heading("#0",text="Nombre", anchor=CENTER)
        self.Tbregistros2.heading("col1",text="Hora de ingreso", anchor=CENTER)
        self.Tbregistros2.heading("col2",text="Hora de salida", anchor=CENTER)
        self.Tbregistros2.place(x=68,y=325, width=400,height=200)
        
        
        self.botonEmpleados = Button(self.ventana,
                                     text="Empleados",
                                     width=7,
                                     height=8,
                                     font=("Poppins",12)
                                     )
        self.botonEmpleados.place(x=500,y=200, width=100, height=30)
        self.botonSalir = Button(self.ventana,
                                    text="Salir",
                                    width=7,
                                    height=0,
                                    font=("Poppins", 12),
                                    command=self.regresarMain
                                    )
        self.botonSalir.place(x=500, y=240, width=100, height=30)
        
        mainloop()     
        


Main()
