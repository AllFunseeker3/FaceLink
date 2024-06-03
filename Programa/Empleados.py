from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
from CTkMessagebox import *

class Empleados:
    def RegresarPrincipal(self):
        try:
            self.ventana.destroy()
            Principal()
            
        except Exception as e:
            print(f"Error al regresar a la ventana principal: {e}")

    def Aviso(self):
        try:
            self.msg = CTkMessagebox(
                title="¿Eliminar?",
                message="Esta accion no es irreversible. ¿Seguro que quiere eliminar a este usuario?",
                icon="question",
                option_1="Eliminar",
                option_2="Cancelar",
                bg_color="#F6F4EB",
                fg_color="#F6F4EB",
                text_color="#4682A9",
                title_color="#4682A9"
            )
            self.Respuesta = self.msg.get()
            if self.Respuesta == "Eliminar":
                CTkMessagebox(title="Acción hecha",
                message="El usuario se eliminó correctamente",
                icon="question",
                bg_color="#F6F4EB",
                fg_color="#F6F4EB",
                text_color="#4682A9",
                title_color="#4682A9")
        except Exception as e:
            print(f"Error al mostrar el mensaje de aviso: {e}")

    def __init__(self):
        try:
            self.ventana = Tk()
            self.ventana.title("Face-link")
            self.ventana.propagate(0)
            ancho_pantalla = self.ventana.winfo_screenwidth()
            alto_pantalla = self.ventana.winfo_screenheight()
            ancho_ventana = 595
            alto_ventana = 404
            x_pos = (ancho_pantalla - ancho_ventana) // 2
            y_pos = (alto_pantalla - alto_ventana) // 2
            self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
            self.ventana.resizable(0, 0)
            self.ventana.overrideredirect(True)

            fondo = "#F6F4EB"
            self.ventana.config(bg=fondo)

            self.LBFoto = Label(self.ventana, bg="Black")
            self.LBFoto.place(x=20, y=10, width=114, height=121)

            self.LBDatos = Label(self.ventana, text="Datos: ", font=("Poppins", 16), anchor="w", bg=fondo)
            self.LBDatos.place(x=140, y=15, width=200, height=20)

            self.LBNombre = Label(self.ventana, text="Nombre: ", font=("Poppins", 16), anchor="w", bg=fondo)
            self.LBNombre.place(x=140, y=45, width=200, height=20)

            self.LBPuesto = Label(self.ventana, text="Puesto: ", font=("Poppins", 16), anchor="w", bg=fondo)
            self.LBPuesto.place(x=140, y=75, width=200, height=20)

            self.LBTurno = Label(self.ventana, text="Turno: ", font=("Poppins", 16), anchor="w", bg=fondo)
            self.LBTurno.place(x=140, y=105, width=200, height=20)

            self.CBEmpleados = ttk.Combobox(self.ventana)
            self.CBEmpleados.place(x=370, y=15, width=200, height=25)

            self.LBRegistros = Label(self.ventana, text="Registros:", font=("Poppins", 16), anchor="w", bg=fondo)
            self.LBRegistros.place(x=20, y=170, width=105, height=20)

            self.Tbregistros = ttk.Treeview(self.ventana, columns=("col1", "col2"))
            self.Tbregistros.column("#0", width=40)
            self.Tbregistros.column("col1", width=40, anchor=CENTER)
            self.Tbregistros.column("col2", width=40, anchor=CENTER)

            self.Tbregistros.heading("#0", text="Fecha", anchor="w")
            self.Tbregistros.heading("col1", text="Hora de ingreso", anchor="w")
            self.Tbregistros.heading("col2", text="Hora de salida", anchor="w")
            self.Tbregistros.place(x=20, y=200, width=550, height=120)

            self.BTRegresar = CTkButton(master=self.ventana, text="Regresar", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16), command=self.RegresarPrincipal)
            self.BTRegresar.place(x=20, y=350)

            self.BTEliminar = CTkButton(master=self.ventana, text="Eliminar", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16), command=self.Aviso)
            self.BTEliminar.place(x=140, y=350)

            self.BTGestionar = CTkButton(master=self.ventana, text="Gestionar", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16))
            self.BTGestionar.place(x=260, y=350)

            self.ventana.mainloop()
        except Exception as e:
            print(f"Error al iniciar la ventana de empleados: {e}")

      
Empleados()
    
    