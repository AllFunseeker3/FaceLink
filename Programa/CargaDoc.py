from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
from CTkMessagebox import *

class Buscador:
    #--------Funciones-----------
    
    def AbrirA(self):
        archivo_seleccionado = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=(("Archivo PDF", ".pdf"), ("Todos los archivos", ".*")))
        
        self.msg = CTkMessagebox(
        title="Guardado",
        message="El documento se cargó correctamente",
        icon="check",
        option_1="Regresar",
        bg_color="#F6F4EB",
        fg_color="#F6F4EB",
        text_color="#4682A9",
        title_color="#4682A9"
        )    
                            
        if archivo_seleccionado:
            with open(archivo_seleccionado, 'r') as archivo:
                contenido = archivo.read()
                print(contenido)

                
    def Aviso1(self):
        self.msg3 = CTkMessagebox(
                title="Error",
                message="Faltan los siguientes documentos: CURP, Carta de recomendación, Acta de nacimiento",
                icon="cancel",
                option_1="Regresar",
                bg_color="#F6F4EB",
                fg_color="#F6F4EB",
                text_color="#4682A9",
                title_color="#4682A9"
            )
    def Aviso2(self):
        self.msg1 = CTkMessagebox(
                title="Guardado", 
                message="Los biometricos faciales fueron guardados correctamente",
                icon="check",
                option_1="Regresar",
                bg_color="#F6F4EB",
                fg_color="#F6F4EB",
                text_color="#4682A9",
                title_color="#4682A9"
            )

    
    #--------Interfaz--------
    def __init__(self):
            self.ventana = Tk()
            self.ventana.title("Inicio")
            self.ventana.propagate(0)
            ancho_pantalla = self.ventana.winfo_screenwidth()
            alto_pantalla = self.ventana.winfo_screenheight()
            ancho_ventana = 417
            alto_ventana = 513
            x_pos = (ancho_pantalla - ancho_ventana) // 2
            y_pos = (alto_pantalla - alto_ventana) // 2
            self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
            self.ventana.resizable(0, 0)
            self.ventana.overrideredirect(True)
            
            fondo = "#F6F4EB"
            self.ventana.config(bg=fondo)
            
            self.LBFoto = Label(self.ventana, bg="Black")
            self.LBFoto.place(x=36, y=44, width=100, height=100)
            
            self.CCara = CTkButton(master=self.ventana, 
                                        text="Escanear cara", 
                                        fg_color="#4682A9", 
                                        hover_color="#91C8E4", 
                                        height=41,
                                        width=163,
                                        font=("Poppins", 16),
                                        command=self.Aviso2)
            self.CCara.place(x=159, y=103)
            
            self.CINE = CTkButton(master=self.ventana,
                                        text="Subir documento",
                                        fg_color="#4682A9",
                                        hover_color="#91C8E4",
                                        height=37,
                                        width=143,
                                        font=("Poppins", 16),
                                        command=self.AbrirA)
            self.CINE.place(x=36, y=172)
            
            self.LBINE = Label(self.ventana, text="INE: ", font=("Poppins", 20), anchor="w", bg=fondo)
            self.LBINE.place(x=194, y=180, width=41, height=29)
            
            
            self.CCReco = CTkButton(master=self.ventana,
                                        text="Subir documento",
                                        fg_color="#4682A9",
                                        hover_color="#91C8E4",
                                        height=36,
                                        width=143,
                                        font=("Poppins", 16),
                                        command=self.AbrirA)
            self.CCReco.place(x=36, y=226)
            
            self.LBCReco = Label(self.ventana, text="Carta de recomendación", font=("Poppins", 14), anchor="w", bg=fondo)
            self.LBCReco.place(x=194, y=234, width=215, height=29)
            
            self.CCURP = CTkButton(master=self.ventana,
                                        text="Subir documento",
                                        fg_color="#4682A9",
                                        hover_color="#91C8E4",
                                        height=36,
                                        width=143,
                                        font=("Poppins", 16),
                                        command=self.AbrirA)
            self.CCURP.place(x=36, y=284)
            
            self.LBCURP = Label(self.ventana, text="CURP", font=("Poppins", 20), anchor="w", bg=fondo)
            self.LBCURP.place(x=194, y=301, width=62, height=29)
            
            self.CAN = CTkButton(master=self.ventana,
                                        text="Subir documento",
                                        fg_color="#4682A9",
                                        hover_color="#91C8E4",
                                        height=36,
                                        width=143,
                                        font=("Poppins", 16),
                                        command=self.AbrirA)
            self.CAN.place(x=36, y=346)
            
            self.LBAN = Label(self.ventana, text="Acta de nacimiento", font=("Poppins", 16), anchor="w", bg=fondo)
            self.LBAN.place(x=194, y=354, width=183, height=29)
            
            self.BTRegresar = CTkButton(master=self.ventana,
                                        text="Regresar",
                                        fg_color="#4682A9",
                                        hover_color="#91C8E4",
                                        height=41,
                                        width=143,
                                        font=("Poppins", 16))
            self.BTRegresar.place(x=36, y=418)
            
            self.TBGuardar = CTkButton(master=self.ventana,
                                        text="Guardar",
                                        fg_color="#4682A9",
                                        hover_color="#91C8E4",
                                        height=41,
                                        width=143,
                                        font=("Poppins", 16),
                                        command=self.Aviso1)
            self.TBGuardar.place(x=213, y=418)
            
            self.ventana.mainloop()


Buscador()