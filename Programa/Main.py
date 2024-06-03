from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
from CTkMessagebox import *

class Main:
    def cerrar(self):
        try:
            self.msg = CTkMessagebox(
                title="¿Salir?", 
                message="Esta accion cerrara la aplicación ¿Seguro que quiere continuar?",
                icon="question",
                option_1="Cancelar",
                option_2="Salir",
                bg_color="#F6F4EB",
                fg_color="#F6F4EB",
                text_color="#4682A9",
                title_color="#4682A9"
            )
            self.Respuesta = self.msg.get()
            if self.Respuesta == "Salir":
                self.ventana.quit()
                self.ventana.destroy()
                
        except Exception as e:
            print(f"Error al cerrar la ventana: {e}")

    def AbrirP(self):
        try:
            self.ventana.quit()
            self.ventana.destroy()
            Principal()
            
        except Exception as e:
            print(f"Error al abrir la ventana principal: {e}")

    def __init__(self):
        try:
            self.ventana = Tk()
            self.ventana.title("Inicio")
            self.ventana.propagate(0)
            ancho_pantalla = self.ventana.winfo_screenwidth()
            alto_pantalla = self.ventana.winfo_screenheight()
            ancho_ventana = 500
            alto_ventana = 600
            x_pos = (ancho_pantalla - ancho_ventana) // 2
            y_pos = (alto_pantalla - alto_ventana) // 2
            self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
            self.ventana.resizable(0, 0)
            self.ventana.overrideredirect(True)

            fondo = "#F6F4EB"

            self.frame_sup = Frame(self.ventana, bg=fondo)
            self.frame_sup.pack(fill="both", expand=True)

            self.frame_inf = Frame(self.ventana, bg=fondo)
            self.frame_inf.pack(fill="both", expand=True)

            self.titulo = Label(self.frame_sup, text="Ingreso", font=("Poppins", 20, "bold"), bg=fondo)
            self.titulo.pack(side="top", pady=20)

          #  self.img = Image.open("Imagenes/FaceLink.png")
           # self.img = self.img.resize((150, 165))
        #    self.render = ImageTk.PhotoImage(self.img)
         #   self.fondo = Label(self.frame_sup, image=self.render, bg=fondo)
          #  self.fondo.pack(expand=True, fill="both", side="top")

            self.label_usuario = Label(self.frame_inf, text="Usuario", font=("Poppins", 14, "bold"), bg=fondo, fg="black")
            self.label_usuario.place(x=90, y=0, width=70, height=19)

            self.BoxUsuario = Entry(self.frame_inf, bd=0, width=25, font=("Poppins", 15))
            self.BoxUsuario.place(x=90, y=20, width=310, height=35)

            self.label_contrasena = Label(self.frame_inf, text="Contraseña", font=("Poppins", 14, "bold"), bg=fondo, fg="black")
            self.label_contrasena.place(x=90, y=60, width=110, height=19)

            self.Boxcontrasena = Entry(self.frame_inf, bd=0, width=25, font=("Poppins", 15), show="*")
            self.Boxcontrasena.place(x=90, y=79, width=310, height=35)

            self.botonIngresar = CTkButton(master=self.frame_inf, text="Ingresar", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16), command=self.AbrirP)
            self.botonIngresar.place(x=300, y=118)

            self.botonSalir = CTkButton(master=self.frame_inf, text="Salir", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16), command=self.cerrar)
            self.botonSalir.place(x=90, y=118)

            self.ventana.mainloop()
        except Exception as e:
            print(f"Error al iniciar la aplicación: {e}")


class Principal:
    def regresarMain(self):
        try:
            self.ventana.quit()
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
                message="Esta accion no es reversible ¿Seguro que quiere eliminar ese usaurio?",
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
                CTkMessagebox(title="Info", message="This is a CTkMessagebox!")
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


if __name__ == "__main__":
    Main()
