from tkinter import *
from tkinter import ttk

class Principal: 

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
                                    font=("Poppins", 12)
                                    
                                    )
        self.botonSalir.place(x=500, y=240, width=100, height=30)
        
        
        
        mainloop()
Principal()