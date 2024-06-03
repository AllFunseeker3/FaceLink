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
                self.ventana.destroy()
                
        except Exception as e:
            print(f"Error al cerrar la ventana: {e}")

    def AbrirP(self):
        try:
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

            self.img = Image.open("Imagenes/FaceLink.png")
            self.img = self.img.resize((150, 165))
            self.render = ImageTk.PhotoImage(self.img)
            self.fondo = Label(self.frame_sup, image=self.render, bg=fondo)
            self.fondo.pack(expand=True, fill="both", side="top")

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
Main()