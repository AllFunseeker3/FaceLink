from tkinter import *
from tkinter import ttk
from tkinter.tix import *

class Empleados:
    #-------Funciones--------
    
    
    #---------Ventana-----------
    
     def __init__(self):
         self.ventana= Tk()
         self.ventana.geometry("595x404")
         self.ventana.title("Face-link")
         fondo="#F6F4EB"
         self.ventana.config(bg=fondo)
         
         #self.ScrollB=Scrollbar(self.ventana)
         #self.c=Canvas(self.ventana,
                       #background="pink", 
                       #yscrollcommand=self.ScrollB.set)
         #self.ScrollB.config(command=self.c.yview)
         #self.ScrollB.pack(side=RIGHT, fill=Y)
         
         
         self.LBFoto=Label(self.ventana,
                           bg="Black")
         self.LBFoto.place(x=20,y=10, width=114,height=121)
         
         self.LBDatos=Label(self.ventana,
                           text="Datos: ",
                           font=("Poppins", 16),
                           anchor="w",
                           bg=fondo)
         self.LBDatos.place(x=140,y=15, width=200,height=20)
         
         
         self.LBNombre=Label(self.ventana,
                           text="Nombre: ",
                           font=("Poppins", 16),
                           anchor="w",
                           bg=fondo)
         self.LBNombre.place(x=140,y=45, width=200,height=20)
         
         self.LBPuesto=Label(self.ventana,
                           text="Puesto: ",
                           font=("Poppins", 16),
                           anchor="w",
                           bg=fondo)
         self.LBPuesto.place(x=140,y=75, width=200,height=20)
         
         self.LBTurno=Label(self.ventana,
                           text="Turno: ",
                           font=("Poppins", 16),
                           anchor="w",
                           bg=fondo)
         self.LBTurno.place(x=140,y=105, width=200,height=20)
         
         self.CBEmpleados=ttk.Combobox(self.ventana)
         self.CBEmpleados.place(x=370, y=15, width=200,height=25)
         
         self.LBRegistros=Label(self.ventana,
                                text="Registros:",
                                font=("Poppins",16),
                                anchor="w",
                                bg=fondo)
         self.LBRegistros.place(x=20,y=170,width=105, height=20)
         
         
         
         self.Tbregistros=ttk.Treeview(self.ventana,
                                      columns=("col1","col2"))
         self.Tbregistros.column("#0",width=40)
         self.Tbregistros.column("col1",width=40,anchor=CENTER)
         self.Tbregistros.column("col2",width=40,anchor=CENTER)
        
         self.Tbregistros.heading("#0",text="Fecha", anchor="w")
         self.Tbregistros.heading("col1",text="Hora de ingreso", anchor="w")
         self.Tbregistros.heading("col2",text="Hora de salida", anchor="w")
         self.Tbregistros.place(x=20,y=200, width=550,height=120)
         
         self.BTRegresar=Button(self.ventana,
                                text="Regresar",
                                width=7,
                                height=8,
                                font=("Poppins",12)
                                )
         self.BTRegresar.place(x=20, y= 350,width=100 , height=30)
         
         self.BTEliminar=Button(self.ventana,
                                text="Eliminar",
                                width=7,
                                height=8,
                                font=("Poppins",12)
                                )
         self.BTEliminar.place(x=130, y= 350,width=100 , height=30)
         
         self.BTGestionar=Button(self.ventana,
                                text="Gestionar",
                                width=7,
                                height=8,
                                font=("Poppins",12)
                                )
         self.BTGestionar.place(x=240, y= 350,width=100 , height=30)
         mainloop()
         
Empleados()
    
    