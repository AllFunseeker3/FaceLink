from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
from CTkMessagebox import *

class Principal:
    def regresarMain(self):
        try:
            self.ventana.destroy()
            Main()
            
        except Exception as e:
            print(f"Error al regresar a la ventana principal: {e}")

    def AbrirEmpleados(self):
        try:
            self.ventana.destroy()
            Empleados()
            
        except Exception as e:
            print(f"Error al abrir la ventana de empleados: {e}")

    def __init__(self):
        try:
            self.ventana = Tk()
            self.ventana.geometry("657x573")
            self.ventana.title("Face-link")
            fondo = "#F6F4EB"
            self.ventana.config(bg=fondo)
            self.ventana.propagate(0)
            ancho_pantalla = self.ventana.winfo_screenwidth()
            alto_pantalla = self.ventana.winfo_screenheight()
            ancho_ventana = 657
            alto_ventana = 573
            x_pos = (ancho_pantalla - ancho_ventana) // 2
            y_pos = (alto_pantalla - alto_ventana) // 2
            self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
            self.ventana.resizable(0, 0)
            self.ventana.overrideredirect(True)

            self.LBRegis = Label(self.ventana, text="Registros del dia", font=("Poppins", 16), bg=fondo)
            self.LBRegis.place(x=50, y=10, width=200, height=25)

            self.LBFecha = Label(self.ventana, text="Fecha:", font=("Poppins", 16), bg=fondo)
            self.LBFecha.place(x=68, y=50, width=70, height=25)

            self.Tbregistros = ttk.Treeview(self.ventana, columns=("col1", "col2"))
            self.Tbregistros.column("#0", width=80)
            self.Tbregistros.column("col1", width=80, anchor=CENTER)
            self.Tbregistros.column("col2", width=80, anchor=CENTER)

            self.Tbregistros.heading("#0", text="Nombre", anchor=CENTER)
            self.Tbregistros.heading("col1", text="Hora de ingreso", anchor=CENTER)
            self.Tbregistros.heading("col2", text="Hora de salida", anchor=CENTER)
            self.Tbregistros.place(x=68, y=90, width=400, height=200)

            self.LBFecha2 = Label(self.ventana, text="Fecha:", font=("Poppins", 16), bg=fondo)
            self.LBFecha2.place(x=68, y=295, width=70, height=25)

            self.Tbregistros2 = ttk.Treeview(self.ventana, columns=("col1", "col2"))
            self.Tbregistros2.column("#0", width=80)
            self.Tbregistros2.column("col1", width=80, anchor=CENTER)
            self.Tbregistros2.column("col2", width=80, anchor=CENTER)

            self.Tbregistros2.heading("#0", text="Nombre", anchor=CENTER)
            self.Tbregistros2.heading("col1", text="Hora de ingreso", anchor=CENTER)
            self.Tbregistros2.heading("col2", text="Hora de salida", anchor=CENTER)
            self.Tbregistros2.place(x=68, y=325, width=400, height=200)

            self.botonEmpleados = CTkButton(master=self.ventana, text="Empleados", fg_color="#91C8E4", hover_color="#4682A9", height=40, width=117, font=("Poppins", 16), command=self.AbrirEmpleados)
            self.botonEmpleados.place(x=500, y=200)
            self.botonSalir = CTkButton(master=self.ventana, text="Cerrar", fg_color="#91C8E4", hover_color="#4682A9", height=40, width=117, font=("Poppins", 16), command=self.regresarMain)
            self.botonSalir.place(x=500, y=300)

            self.ventana.mainloop()
        except Exception as e:
            print(f"Error al iniciar la ventana principal: {e}")

Principal()