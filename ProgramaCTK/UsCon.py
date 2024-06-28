from customtkinter import *
from PIL import Image   
import os
from tkinter import messagebox,filedialog, Toplevel,Button
from tkcalendar import *
from CTkTable import CTkTable
from recon.CapturandoRostros import * 
from Librerias.LibreriaBaseDatos import * 
import ctypes
import datetime
#Ya me quiero dar de baja
class CargaDocs(CTkToplevel):

    def cargarDocs(self):
            archivo_seleccionado = filedialog.askopenfilename(
                title="Seleccionar archivo",
                filetypes=(("Archivo PDF", ".pdf"), ("Todos los archivos", ".*"))) 
            mensaje=messagebox.showinfo("Guardado","El archivo se guardó correctamente")
        
    def Guardado(self): 
        messagebox.showinfo("Guardado","El registro se realizó correctamente")
        print(self.TxBoxNombre.get())

    
    def Actualizado(self):
        messagebox.showinfo("Actualizado","El registro se actualizó correctamente")
        
    def mostrar_calendario(self):
        ventana_calendario = Toplevel(self)
        calendario = Calendar(ventana_calendario, selectmode='day', date_pattern='dd/mm/yyyy')
        calendario.pack()

        def actualizar_fecha():
            fecha_seleccionada = calendario.get_date()
            self.TxBoxFechaN.delete(0, "end")
            self.TxBoxFechaN.insert(0, fecha_seleccionada)

        boton_seleccionar = CTkButton(master=ventana_calendario, text="Seleccionar", command=actualizar_fecha)
        boton_seleccionar.pack()
    
    def iniciar(self):
        print(str(self.TxBoxNombre.get))
        

    def __init__(self,ID = NONE):
        self.ID = ID
        if ID is NONE:
            print("es non")
            ID = ejecutar_consulta("SELECT MAX(IDEmpleados) + 1 AS SiguienteID FROM Empleados")
       
        super().__init__()
        self.title("Face-link")
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        ancho_ventana = 950
        alto_ventana = 459
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.resizable(0, 0)
        #self.ventana.propagate(0)
        #self.ventana.overrideredirect(True)  
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes"
        
        ImgEscane_data=Image.open(ruta_con_diagonales+"/cara.png")
        ImgINE_data=Image.open(ruta_con_diagonales+"/INE.png")
        ImgCartaRec_data=Image.open(ruta_con_diagonales+"/CartaRec.png")
        ImgCURP_data=Image.open(ruta_con_diagonales+"/CURP.png")
        ImgActaNac_data=Image.open(ruta_con_diagonales+"/ActaNac.png")
        ImgPDF_data=Image.open(ruta_con_diagonales+"/pdf.png")
        ImgOjo_data=Image.open(ruta_con_diagonales+"/ojo.png")
        ImgCerrar_data=Image.open(ruta_con_diagonales+"/abierto.png")
        ImgGuardar_data=Image.open(ruta_con_diagonales+"/Guardar.png")
        ImgCalendario_data=Image.open(ruta_con_diagonales+"/calendario.png")
        
        
        ImgCalendario=CTkImage(light_image=ImgCalendario_data,size=(32,32))
        ImgGuardar=CTkImage(light_image=ImgGuardar_data,size=(32,32))
        ImgOjo=CTkImage(light_image=ImgOjo_data,size=(32,32))
        ImgEscane=CTkImage(light_image=ImgEscane_data,size=(32,32))
        ImgIne=CTkImage(light_image=ImgINE_data,size=(32,32))
        ImgCartaRec=CTkImage(light_image=ImgCartaRec_data, size=(32,32))
        ImgCURP=CTkImage(light_image=ImgCURP_data, size=(32,32))
        ImgActaNac=CTkImage(light_image=ImgActaNac_data, size=(32,32))
        ImgPDF=CTkImage(light_image=ImgPDF_data,size=(32,32))
        ImgCerrar=CTkImage(light_image=ImgCerrar_data,size=(32,32))
        
        self.almacenador=CTkFrame(master=self,width=424,height=459,fg_color="#F6F4EB",corner_radius=0)
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True,side="bottom", fill="both")
        
        self.LBFoto = CTkLabel(self.almacenador,bg_color="black",text="",height=114, width=114).place(x=150, y=23)
        self.BTEscanear=CTkButton(master=self.almacenador  ,image=ImgEscane,text="Escanear rostro",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10).place(x=280,y=61)
        self.BTSubirINE=CTkButton(master=self.almacenador  ,image=ImgPDF,text="Subir documento",anchor="", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=self.cargarDocs).place(x=450,y=147)
        self.BTSubirCartaRec=CTkButton(master=self.almacenador  ,image=ImgPDF,text="Subir documento",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=self.cargarDocs).place(x=450,y=201)
        self.BTSubirCURP=CTkButton(master=self.almacenador  ,image=ImgPDF,text="Subir documento",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=self.cargarDocs).place(x=450,y=254)
        self.BTActaNac=CTkButton(master=self.almacenador  ,image=ImgPDF,text="Subir documento",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=self.cargarDocs).place(x=450,y=305)
        #x30
        
        self.LBNombre=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Nombre",font=("Poppins",18,"bold")).place(x=30,y=147)
        self.TxBoxNombre=CTkEntry(master=self.almacenador,text="",width=150,height=35,text_color="#000000",font=("Poppins",18,"bold"),fg_color="#E0E0E0",corner_radius=10)
        self.TxBoxNombre.place(x=30,y=177)
        
        self.LBAP=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Apellido paterno",font=("Poppins",18,"bold")).place(x=30,y=217)
        self.TxBoxAP=CTkEntry(master=self.almacenador,width=150,height=35,text_color="#000000",font=("Poppins",18,"bold"),fg_color="#E0E0E0",corner_radius=10)
        self.TxBoxAP.place(x=30,y=247)

        self.LBAM=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Apellido materno",font=("Poppins",18,"bold")).place(x=30,y=287)
        self.TxBoxAM=CTkEntry(master=self.almacenador,width=150,height=35,text_color="#000000",font=("Poppins",18,"bold"),fg_color="#E0E0E0",corner_radius=10)
        self.TxBoxAM.place(x=30,y=317)

        self.LBFechaN = CTkLabel(master=self.almacenador, text_color="#4682A9", text="Fecha de nacimiento", font=("Poppins", 18, "bold")).place(x=192, y=147)
        self.TxBoxFechaN = CTkEntry(master=self.almacenador, placeholder_text="dd/mm/yyyy", width=120, height=35, text_color="#000000", font=("Poppins", 18, "bold"), fg_color="#E0E0E0", corner_radius=10)
        self.TxBoxFechaN.place(x=192, y=177)
        self.BTCalendario = CTkButton(master=self.almacenador, image=ImgCalendario, text="", anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16, "bold"), corner_radius=10, command=self.mostrar_calendario).place(x=318, y=177)

        
        Turnos = ejecutar_consulta("SELECT TIME_FORMAT(horaEntrada, '%H:%i') AS HoraEntrada, TIME_FORMAT(HoraSalida, '%H:%i') AS HoraSalida FROM Horarios")
        Turnos_str = [str(item) for item in Turnos]
        self.LBTurno=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Turno",font=("Poppins",18,"bold")).place(x=192,y=227)
        self.ComBox=CTkComboBox(master=self, values=Turnos_str,
                        state="readonly",border_color="#5BB0E7", button_color="#3F789D",
                        button_hover_color="#F6F4EB", fg_color="#F6F4EB",
                        dropdown_fg_color="#F6F4EB", dropdown_hover_color="#CCD1D3",
                        text_color="#4682A9", dropdown_text_color="#4682A9",
                        font=("Poppins",16,"bold"), corner_radius=0)
        self.ComBox.place(x=192,y=257)
                
        self.BTVis1=CTkButton(master=self.almacenador  ,image=ImgOjo,text="",anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16,"bold"),corner_radius=10).place(x=390,y=147)
        self.BTVis2=CTkButton(master=self.almacenador  ,image=ImgOjo,text="",anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16,"bold"),corner_radius=10).place(x=390,y=201)
        self.BTVis3=CTkButton(master=self.almacenador  ,image=ImgOjo,text="",anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16,"bold"),corner_radius=10).place(x=390,y=254)
        self.BTVis4=CTkButton(master=self.almacenador  ,image=ImgOjo,text="",anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16,"bold"),corner_radius=10).place(x=390,y=305)


        self.LBINE = CTkLabel(master=self.almacenador, text_color="#4682A9", text="INE", font=("Poppins", 20, "bold")).place(x=700, y=150)
        self.LBImagenINE = CTkLabel(master=self.almacenador, image=ImgIne,text="").place(x=660, y=150)
        
        self.LBCartaRec = CTkLabel(master=self.almacenador, text_color="#4682A9", text="Carta de recomedación", font=("Poppins", 20, "bold")).place(x=700, y=204)
        self.LBImagenCRec = CTkLabel(master=self.almacenador, image=ImgCartaRec,text="").place(x=660, y=204)

        self.LBCURP = CTkLabel(master=self.almacenador, text_color="#4682A9", text="CURP", font=("Poppins", 20, "bold")).place(x=700, y=258)
        self.LBImagenCURP = CTkLabel(master=self.almacenador, image=ImgCURP,text="").place(x=660, y=258)
    
        self.LBDatosActaNac = CTkLabel(master=self.almacenador, text_color="#4682A9", text="Acta de nacimiento", font=("Poppins", 20, "bold")).place(x=700, y=312)
        self.LBImagenANac = CTkLabel(master=self.almacenador, image=ImgActaNac,text="").place(x=660, y=312)
            
        self.botonregresar = CTkButton(master=self.almacenador  ,image=ImgCerrar,text="Regresar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=41, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=self.destroy).place(x=91, y=390)
        self.botonregresar = CTkButton(master=self.almacenador  ,image=ImgGuardar,text="Guardar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=41, width=143, font=("Poppins", 16,"bold"),corner_radius=10).place(x=300, y=390)



class Empleados(CTkToplevel):
    
    def Eliminar(self):
        self.Des=messagebox.askquestion("¿Eliminar?","¿Esta seguro que quieres eliminar a este empleado? Esta acción es irreversible")
        if self.Des=="yes":
            selected_value = self.ComBox.get() 
            lista = eval(selected_value)
            datos = lista[0] 
            resultado = ejecutar_consulta("SELECT e.Nombre, e.ApellidoP,e.ApellidoM,e.FechaNacimiento,h.HoraEntrada,h.HoraSalida,e.FotoRuta,e.IdEmpleados" + 
                                " FROM Empleados e JOIN Horarios h ON e.IDHorario = h.IDHorario " + "WHERE e.IDEmpleados = " 
                                + str(datos))
            r = eval(str(resultado[0]))
            nombre = "Nombre: "+r[0]
            try:
                ejecutar_modificacion("DELETE FROM LOGFechaHora WHERE IDEmpleados = " + str(r[7]))
                ejecutar_modificacion("DELETE FROM Relacion_EmpleadosDocumentos WHERE IDEmpleados = " + str(r[7]))
                ejecutar_modificacion("DELETE FROM Empleados WHERE IDEmpleados = " + str(r[7]))
                mensaje=messagebox.showinfo("Elminiado","Empleado eliminado: " + str(r[1]) + " " + str(r[2]))
                self.ComBox.set("")
                EmpleadosVal = ejecutar_consulta("select idEmpleados,nombre,apellidop from empleados")
                EmpleadosVal_str = [str(item) for item in EmpleadosVal]
                self.ComBox.configure(values=EmpleadosVal_str)
                self.ActualizarLabeles(lista[0]) 
            except Exception as e:
                print("error de: "+ str(e)) 

            


    
    def Abrir(self,ID=None):
        if ID is not None:
            cargarDoc_window=CargaDocs(ID)
            cargarDoc_window.mainloop()
        else:
            print("No se recibió ningún parámetro")
            cargarDoc_window=CargaDocs()
            cargarDoc_window.mainloop()


    def Cerrar(self):
        self.destroy()



    def ActualizarLabeles(self, datos):
        resultado = ejecutar_consulta("SELECT e.Nombre, e.ApellidoP,e.ApellidoM,e.FechaNacimiento,h.HoraEntrada,h.HoraSalida,e.FotoRuta,e.IdEmpleados" + 
                                      " FROM Empleados e JOIN Horarios h ON e.IDHorario = h.IDHorario " + "WHERE e.IDEmpleados = " 
                                      + str(datos))
        r = eval(str(resultado[0]))
        nombre = "Nombre: "+r[0]
        ap = "Apellido Paterno: " + r[1]
        am = "Apellido Materno: " + r[2]
        fn = "Fecha de Nacimiento: " + str(r[3])
        tn = "Turno: " + str(r[4]) + " a "  +str(r[5]) 
        ft = r[6]
        self.LBApPat.configure(text=ap)
        self.LBApMat.configure(text=am)
        self.LBPuesto.configure(text=fn)
        self.LBTurno.configure(text=tn)
        
        Rut =  "C:/Rostros/Caras/"+ str(r[7]) +"/Rostro_20.jpg"
        Rut = Rut
        try:
            self.Foto=Image.open(Rut)
            self.FotoCTK=CTkImage(light_image=self.Foto,size=(114,114))
            self.LBFoto.configure(image=self.FotoCTK)
        except Exception as e:
            ruta_actual = os.getcwd()
            ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes"
            self.Foto=Image.open(ruta_con_diagonales+"/ojo.png")
            self.FotoCTK=CTkImage(light_image=self.Foto,size=(114,114))
            self.LBFoto.configure(image = self.FotoCTK)
        datos=[
            ["ID","Nombre","Apellido Paterno","Apellido Materno","Fecha","Hora de ingreso","Hora de salida"]
            ]
        for fila in ejecutar_procedimiento("InicializarRegistros",()):
            datos.append(fila)
        self.tabla.configure(values=datos)

           # ctypes.windll.user32.MessageBoxW(0,"No se ha logrado cargar la imagen ","FaceLink", 0|32)
    
    def gestionar(self):
        selected_value = self.ComBox.get()
        if selected_value != "":
            print("selected: "+str(selected_value)) 
            lista = eval(selected_value)
            print("lista: "+str(lista))
            self.Abrir(str(lista[0]))
        else:
            messagebox.showinfo("Facelink","No ha seleccionado una opcion valida")                



    def on_combobox_change(self, event):
        selected_value = self.ComBox.get() 
        lista = eval(selected_value)
        self.ActualizarLabeles(lista[0]) 
    def __init__(self):
        super().__init__()
        EmpleadosVal = ()
        EmpleadosVal = ejecutar_consulta("select idEmpleados,nombre,apellidop from empleados")
        EmpleadosVal_str = [str(item) for item in EmpleadosVal]
        
        self.title("Face-link")
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        ancho_ventana = 595
        alto_ventana = 404
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.resizable(0, 0)
        #self.ventana.propagate(0)
        #self.ventana.overrideredirect(True)  
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes"
        
        self.almacenador=CTkFrame(master=self,width=595,height=324,fg_color="#F6F4EB",corner_radius=0)
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True,side="top", fill="both")
        
        self.Foto=Image.open(ruta_con_diagonales+"/ojo.png")
        self.FotoCTK=CTkImage(light_image=self.Foto,size=(114,114))
        self.LBFoto = CTkLabel(self.almacenador,bg_color="black",text="",height=114, width=114, image=self.FotoCTK)
        self.LBFoto.place(x=24, y=44)
        self.LBDatos=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Datos",font=("Poppins",20,"bold"))
        self.LBDatos.place(x=148,y=24)
        self.LBNombre=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Nombre: " ,font=("Poppins",16,"bold"))
        self.LBNombre.place(x=148,y=48)
        self.LBApPat=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Apellido paterno: " ,font=("Poppins",16,"bold"))
        self.LBApPat.place(x=148,y=68)
        self.LBApMat=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Apellido materno: " ,font=("Poppins",16,"bold"))
        self.LBApMat.place(x=148,y=91)
        self.LBPuesto=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Fecha de nacimiento: " ,font=("Poppins",16,"bold"))
        self.LBPuesto.place(x=148,y=111)
        self.LBTurno=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Turno: "  ,font=("Poppins",16,"bold"))
        self.LBTurno.place(x=148,y=131)
    
        self.ComBox=CTkComboBox(master=self, values=EmpleadosVal_str,
                        state="readonly",border_color="#5BB0E7", button_color="#3F789D",
                        button_hover_color="#F6F4EB", fg_color="#F6F4EB",
                        dropdown_fg_color="#F6F4EB", dropdown_hover_color="#CCD1D3",
                        text_color="#4682A9", dropdown_text_color="#4682A9",
                        font=("Poppins",16,"bold"), corner_radius=0,command=self.on_combobox_change)
        self.ComBox.place(x=386,y=48)
        #self.ComBox.bind("<<ComboboxSelected>>", self.on_combobox_change)
        

        datos=[
            ["ID","Nombre","Apellido Paterno","Apellido Materno","Fecha","Hora de ingreso","Hora de salida"]
            ]
        for fila in ejecutar_procedimiento("InicializarRegistros",()):
            datos.append(fila)
        
        self.tablamarco=CTkScrollableFrame(master=self.almacenador,fg_color="transparent")
        self.tablamarco.pack(expand=True, fill="both", padx=20,pady=(170,0))
        self.tabla=CTkTable(master=self.tablamarco, values=datos,colors=["#EEEEEE", "#EEEEEE"],header_color="#4682A9",text_color="#4682A9")
        self.tabla.edit_row(0, text_color="#F6F4EB", hover_color="#2A8C55")
        self.tabla.pack(expand=True)
        
        self.almacenador2=CTkFrame(master=self,width=595,height=80,fg_color="#4682A9",corner_radius=0)
        self.almacenador2.pack_propagate(0)
        self.almacenador2.pack(expand=True,side="bottom", fill="both")
        

        
        ImgEli_data=Image.open(ruta_con_diagonales+"/Eliminar.png")
        ImgCerrar_data=Image.open(ruta_con_diagonales+"/abierto.png")
        ImgCrear_data=Image.open(ruta_con_diagonales+"/Crear.png")
        ImgGes_data=Image.open(ruta_con_diagonales+"/portapapeles.png")
        
        ImgEli=CTkImage(light_image=ImgEli_data,size=(32,32))
        ImgCerrar=CTkImage(light_image=ImgCerrar_data,size=(32,32))
        ImgCrear=CTkImage(light_image=ImgCrear_data, size=(32,32))
        ImgGes=CTkImage(light_image=ImgGes_data, size=(32,32))
        
        self.botonregresar = CTkButton(master=self.almacenador2  ,image=ImgCerrar,text="Cerrar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=114, font=("Poppins", 16,"bold"),corner_radius=0,command=self.Cerrar).pack(side="left")
        self.botoneliminar = CTkButton(master=self.almacenador2,image=ImgEli,text="Eliminar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=114, font=("Poppins", 16,"bold"),corner_radius=0,command=self.Eliminar).pack(side="left")
        self.botongestionar = CTkButton(master=self.almacenador2  ,image=ImgGes,text="Gestionar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=114, font=("Poppins", 16,"bold"),corner_radius=0,command=lambda: self.gestionar()).pack(side="left")
        self.botonnuevo = CTkButton(master=self.almacenador2,image=ImgCrear,text="Nuevo",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=114, font=("Poppins", 16,"bold"),corner_radius=0,command=self.Abrir).pack(side="left")
        
        
  
class UsuCon():
    
    def cerrar(self):
        
        self.Des=messagebox.askquestion("¿Salir?","¿Quieres salir del programa?")
        if self.Des=="yes":
            self.ventana.quit()
            self.ventana.destroy()

                

    def Abrir(self):
        con = self.TxBoxCon.get()
        usuario = self.TxBoxUs.get()
        if con == "PASWORD" and usuario == "Admin" or True:
            self.ventana.quit()
            self.ventana.destroy()
        Principal()
        #empleados_window = Empleados()
#        self.ventana.iconify()
        #empleados_window.lift()
        #empleados_window.mainloop()
    def __init__(self):
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes/FaceLink.png"


        
        self.ventana=CTk()
        self.ventana.title("Face-link")
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = 414
        alto_ventana = 511
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana.resizable(0, 0)
        #self.ventana.propagate(0)
        #self.ventana.overrideredirect(True)
        self.ventana._set_appearance_mode("light")
        
        self.almacenador=CTkFrame(master=self.ventana,width=414,height=511,fg_color="#F6F4EB")
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True)
        
        LogoP_data = Image.open(ruta_con_diagonales)
        LogoP=CTkImage(light_image=LogoP_data,size=(180,180))
        
        self.LBLogo=CTkLabel(master=self.almacenador,text="",image=LogoP,bg_color="#F6F4EB").place(x=117,y=47)
        
        self.LBUs=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Usuario",font=("Poppins",20,"bold")).place(x=48,y=259)
        self.TxBoxUs=CTkEntry(master=self.almacenador,width=310,height=35,text_color="#000000",font=("Poppins",20,"bold"),fg_color="#E0E0E0",corner_radius=10)
        self.TxBoxUs.place(x=48,y=286)

        self.LBCon=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Contraseña",font=("Poppins",20,"bold")).place(x=48,y=342)
        self.TxBoxCon=CTkEntry(master=self.almacenador,width=310,height=35,text_color="#000000",font=("Poppins",20,"bold"),show="*",fg_color="#E0E0E0",corner_radius=10)
        self.TxBoxCon.place(x=48,y=372)        
        
        self.botonIngresar = CTkButton(master=self.almacenador ,text="Ingresar", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16),command=self.Abrir).place(x=241, y=447)

        self.botonSalir = CTkButton(master=self.almacenador, text="Salir", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=117, font=("Poppins", 16),command=self.cerrar).place(x=48, y=447)
        
        self.ventana.mainloop()



class Principal():

    def cerrar(self):    
        self.Des=messagebox.askquestion("¿Salir?","¿Quieres salir del programa?")
        if self.Des=="yes":
            self.ventana.quit()
            self.ventana.destroy()
            UsuCon()
            
    def Abrir(self):
        empleados_window = Empleados()
        self.ventana.iconify()
        empleados_window.lift()
        empleados_window.mainloop()
        
    def __init__(self):

        self.ventana=CTk()
        self.ventana.title("Face-link")
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = 797
        alto_ventana = 473
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana.resizable(0, 0)
        #self.ventana.propagate(0)
        #self.ventana.overrideredirect(True)
        self.ventana._set_appearance_mode("light")
        
        ruta_actual = os.getcwd()
        # Reemplaza las diagonales inversas por diagonales normales
        ruta_con_diagonales = ruta_actual.replace("\\", "/")+"/Imagenes"


        #FramePrincipal
        self.almacenador=CTkFrame(master=self.ventana,width=624,height=512,fg_color="#F6F4EB",corner_radius=0)
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True,side="right")
        
        self.LBRegistros=CTkLabel(master=self.almacenador,text="Registros", bg_color="#F6F4EB",text_color="#4682A9",font=("Poppins",25,"bold")).place(x=15,y=21)
        datos=[
            ["id","Nombre","Apellido Paterno","Apellido Materno","Fecha","Hora de ingreso","Hora de salida"]
            ]
        for fila in ejecutar_procedimiento("InicializarRegistros",()):
            datos.append(fila)
        self.tablamarco=CTkScrollableFrame(master=self.almacenador,fg_color="transparent")
        self.tablamarco.pack(expand=True, fill="both", padx=27, pady=50)
        self.tabla=CTkTable(master=self.tablamarco, values=datos,colors=["#EEEEEE", "#EEEEEE"],header_color="#4682A9",text_color="#4682A9")
        self.tabla.edit_row(0, text_color="#F6F4EB", hover_color="#2A8C55")
        self.tabla.pack(expand=True)
        #FrameLateral
        self.almacenador2=CTkFrame(master=self.ventana,width=176,height=512,fg_color="#4682A9",corner_radius=0)
        self.almacenador2.pack_propagate(0)
        self.almacenador2.pack(expand=True,side="left")     
        LogoP_data = Image.open(ruta_con_diagonales+"/FaceLink.png")
        LogoP=CTkImage(light_image=LogoP_data,size=(64,64))
        
        ImgEmp_data=Image.open(ruta_con_diagonales+"/Empleados.png")
        ImgCerrar_data=Image.open(ruta_con_diagonales+"/abierto.png")
        ImgEmp=CTkImage(light_image=ImgEmp_data,size=(32,32))
        ImgCerrar=CTkImage(light_image=ImgCerrar_data,size=(32,32))
        self.LBLogo=CTkLabel(master=self.almacenador2,text="",image=LogoP,bg_color="#4682A9").pack(pady=(38, 0), anchor="center")
        self.botonEmp = CTkButton(master=self.almacenador2  ,image=ImgEmp,text="Empleados",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=160, font=("Poppins", 16,"bold"),corner_radius=0,command=self.Abrir).pack(anchor="center", ipady=5, pady=(16, 0))
        self.botonCerrar = CTkButton(master=self.almacenador2,image=ImgCerrar,text="Cerrar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=40, width=160, font=("Poppins", 16,"bold"),corner_radius=0,command=self.cerrar).pack(anchor="center", ipady=5, pady=(16, 0))
        
        self.ventana.mainloop()
        
UsuCon()




