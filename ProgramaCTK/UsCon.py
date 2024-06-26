import shutil
from customtkinter import *
from PIL import Image   
import os
from tkinter import messagebox,filedialog, Toplevel,Button
from tkcalendar import *
from CTkTable import CTkTable
from recon.CapturandoRostros import * 
from recon.ReconocimeintoFacial import *
from Librerias.LibreriaBaseDatos import * 
import ctypes
import datetime
import webbrowser

#Ya me quiero dar de baja
class CargaDocs(Toplevel):
    Previo = True

    def cargarDocs(self,tipo):
        ID = self.ID
        # Obtener el nombre de usuario
        username = os.getlogin()
        
        # Crear la ruta de la carpeta destino
        datos = ejecutar_consulta(f"select nombre,apellidop from empleados where idEmpleados = {str(ID)}")
        destino_carpeta = f"C:/Users/{username}/Documents/Documentos Empleados/{ID} " + str(datos[0][0]) + " " + str(datos[0][1])
        
        # Crear la carpeta si no existe
        if not os.path.exists(destino_carpeta):
            os.makedirs(destino_carpeta)
            
        # Pedir al usuario que seleccione un archivo
        archivo_seleccionado = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=(("Archivo PDF", ".pdf"), ("Todos los archivos", ".*")))
        
        # Verificar si se seleccionó un archivo
        if archivo_seleccionado:
            # Copiar el archivo seleccionado a la carpeta destino
            archivo_nombre = os.path.basename(archivo_seleccionado)
            #destino_archivo = os.path.join(destino_carpeta, archivo_nombre)
            destino_archivo = os.path.join(destino_carpeta, tipo + ".pdf")
            try:
                shutil.copy2(archivo_seleccionado, destino_archivo)
                ruta = (str(destino_archivo))
                ruta = ruta.replace("\\", "/")
                print(ruta)
                messagebox.showinfo("Guardado", "El archivo se guardó correctamente")
                ejecutar_modificacion(f"INSERT INTO Documentos (Tipo, Ruta) VALUES ('{tipo}','{ruta}')")
                iddocumentos = str(ejecutar_consulta("SELECT max(IDDocumentos) from documentos")[0][0])
                print("IDdoc " + str(iddocumentos))
                ejecutar_modificacion(f"INSERT INTO Relacion_EmpleadosDocumentos (IDDocumentos, IDEmpleados) VALUES ({str(iddocumentos)},{self.ID})")
            except Exception as e:
                messagebox.showinfo("Facelink Error:","Error: " + str(e))
            
            # Mostrar mensaje de confirmación
           
        else:  
            messagebox.showinfo("No Guardado", "No se ha guardado ningun archivo")
    


    def Guardado(self): 
        messagebox.showinfo("Guardado","El registro se realizó correctamente")

    
    def Actualizado(self):
        messagebox.showinfo("Actualizado","El registro se actualizó correctamente")
        
    def mostrar_calendario(self):
        self.TxBoxFechaN.configure(state='normal')
        ventana_calendario = Toplevel(self)
        calendario = Calendar(ventana_calendario, selectmode='day', date_pattern='yyyy-mm-dd')
        calendario.pack()

        def actualizar_fecha():
            fecha_seleccionada = calendario.get_date()
            self.TxBoxFechaN.delete(0, "end")
            self.TxBoxFechaN.insert(0, fecha_seleccionada)
            self.TxBoxFechaN.configure(state="disabled")

        boton_seleccionar = CTkButton(master=ventana_calendario, text="Seleccionar", command=actualizar_fecha)
        boton_seleccionar.pack()
    
    def saberHorario(self):
        r = ""
        h = str(self.ComBox.get())
        if h == "['08:00', '14:00']":
            r = "1"
        elif h == "['14:00', '21:00']":
            r = "2"
        elif h == "['08:00', '21:00']":
            r = "3"
        print("IDHORARIOR:" + r + ":")
        return r
        

    def guardar(self):
        id = str(self.ID)
        nombre = str(self.TxBoxNombre.get())
        ap = str(self.TxBoxAP.get())
        am = str(self.TxBoxAM.get())
        fn = str(self.TxBoxFechaN.get())
        h = self.saberHorario()
        Rut =  "C:/Rostros/Caras/"+ str(self.ID)
        ft = Rut +"/Rostro_20.jpg" 
        if id and nombre and ap and am and fn and h and ft:
            if self.Previo:
                #si se le dio un ID (osease si estas editando un usuario)
                n = (str(ejecutar_modificacion(f"UPDATE Empleados SET Nombre = '{nombre}',ApellidoP = '{ap}',ApellidoM = '{am}',FechaNacimiento = '{fn}',IDHorario = {h} ,FotoRuta = '{ft}' WHERE IDEmpleados = {id}")))
                if str(n) == "1":

                    messagebox.showinfo("FaceLink dice:","Guardado con exito!")
                    self.destroy()
                     
                else:
                     messagebox.showinfo("FaceLink dice:","Error, no se ha guardado nada!")
            else:
                #si es nuevo user
                Rut =  "C:/Rostros/Caras/"+ str(ejecutar_consulta("select Auto_increment from information_schema.Tables where table_name = 'empleados'")[0][0])
                if os.path.isdir(Rut):
                    n = (str(ejecutar_modificacion(f"INSERT INTO Empleados (Nombre, ApellidoP, ApellidoM, FechaNacimiento, IDHorario,fotoruta) VALUES ('{nombre}', '{ap}', '{am}', '{fn}', {h} , '{ft}')")))
                    if str(n) == "1":
                        messagebox.showinfo("FaceLink dice:","Guardado con exito!")
                        self.destroy()
                    else:
                        messagebox.showinfo("FaceLink dice:","Error, no se ha guardado nada!")
                else: 
                    Des=messagebox.askquestion("Sin Foto:","No hay registro de rostro ¿Desea guardar asi?")
                    if Des == "yes":
                        n = (str(ejecutar_modificacion(f"INSERT INTO Empleados (Nombre, ApellidoP, ApellidoM, FechaNacimiento, IDHorario,fotoruta) VALUES ('{nombre}', '{ap}', '{am}', '{fn}', {h} , '{ft}')")))
                        if str(n) == "1":
                            messagebox.showinfo("FaceLink dice:","Guardado con exito!")
                            self.destroy()
                    else:
                        self.Escanear()
                        n = (str(ejecutar_modificacion(f"INSERT INTO Empleados (Nombre, ApellidoP, ApellidoM, FechaNacimiento, IDHorario,fotoruta) VALUES ('{nombre}', '{ap}', '{am}', '{fn}', {h} , '{ft}')")))
                        if str(n) == "1":
                            messagebox.showinfo("FaceLink dice:","Guardado con exito!")
                            self.destroy()

       
        else:
            messagebox.showinfo("FaceLink dice:","Falta alguno de los datos!")
        

    def iniciar(self):
        Turnos = ejecutar_consulta("SELECT TIME_FORMAT(horaEntrada, '%H:%i') AS HoraEntrada, TIME_FORMAT(HoraSalida, '%H:%i') AS HoraSalida FROM Horarios")
        Turnos_str = [str(item) for item in Turnos]
        if self.Previo == True:
            resultado = ejecutar_consulta("SELECT e.Nombre, e.ApellidoP,e.ApellidoM,e.FechaNacimiento,e.idHorario,e.FotoRuta" + 
                                    " FROM Empleados e JOIN Horarios h ON e.IDHorario = h.IDHorario " + "WHERE e.IDEmpleados = " 
                                    + self.ID)
            r = eval(str(resultado[0]))
            nombre =r[0]
            ap = r[1]
            am = r[2]
            fn = r[3]
            h = r[4]
            if h == 1:
                self.ComBox.set(Turnos_str[0])
            elif h == 2:
                self.ComBox.set(Turnos_str[1])
            elif h == 3:
                self.ComBox.set(Turnos_str[2])

            ft = r[5]
            self.TxBoxNombre.insert(0,nombre)
            self.TxBoxAP.insert(0,ap)
            self.TxBoxAM.insert(0,am)
            self.TxBoxFechaN.configure(state='normal')
            self.TxBoxFechaN.insert(0,fn)
            self.TxBoxFechaN.configure(state='disabled')
                    
            Rut =  "C:/Rostros/Caras/"+ self.ID +"/Rostro_20.jpg"
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

    def Escanear(self):
        if self.Previo:
            id = self.ID
            Capturar(id)
        else:
            Capturar(str(ejecutar_consulta("select Auto_increment from information_schema.Tables where table_name = 'empleados'")[0][0]))
        
        
    def open_folder(path):
    # Asegúrate de que la ruta sea absoluta
        path = os.path.abspath(path)
        
        if os.name == 'nt':  # Windows
            os.startfile(path)
        elif os.name == 'posix':
            try:
                subprocess.Popen(['xdg-open', path])  # Linux
            except FileNotFoundError:
                subprocess.Popen(['open', path])  # macOS
        else:
            raise NotImplementedError(f'Unsupported OS: {os.name}')

    def __init__(self,ID = NONE):
        self.ID = ID
        if ID is NONE:
            self.Previo = False
            self.ID = str(ejecutar_consulta("select Auto_increment from information_schema.Tables where table_name = 'empleados'")[0][0])

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
        
        self.LBFoto = CTkLabel(self.almacenador,image="",bg_color="black",text="",height=114, width=114)
        self.LBFoto.place(x=150, y=23)
        self.BTEscanear=CTkButton(master=self.almacenador  ,image=ImgEscane,text="Escanear rostro",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command= lambda: self.Escanear()).place(x=280,y=61)
        self.BTSubirINE=CTkButton(master=self.almacenador  ,image=ImgPDF,text="Subir documento",anchor="", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=lambda: self.cargarDocs("INE")).place(x=450,y=147)
        self.BTSubirCartaRec=CTkButton(master=self.almacenador  ,image=ImgPDF,text="Subir documento",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=lambda: self.cargarDocs("carta de recomendacion")).place(x=450,y=201)
        self.BTSubirCURP=CTkButton(master=self.almacenador  ,image=ImgPDF,text="Subir documento",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=lambda: self.cargarDocs("CURP")).place(x=450,y=254)
        self.BTActaNac=CTkButton(master=self.almacenador  ,image=ImgPDF,text="Subir documento",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=36, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=lambda: self.cargarDocs("Acta de nacimiento")).place(x=450,y=305)
        #x30
        
        self.LBNombre=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Nombre",font=("Poppins",18,"bold")).place(x=30,y=147)
        self.TxBoxNombre=CTkEntry(master=self.almacenador,width=150,height=35,text_color="#000000",font=("Poppins",18,"bold"),fg_color="#E0E0E0",corner_radius=10)
        self.TxBoxNombre.place(x=30,y=177)
        
        self.LBAP=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Apellido paterno",font=("Poppins",18,"bold")).place(x=30,y=217)
        self.TxBoxAP=CTkEntry(master=self.almacenador,width=150,height=35,text_color="#000000",font=("Poppins",18,"bold"),fg_color="#E0E0E0",corner_radius=10)
        self.TxBoxAP.place(x=30,y=247)

        self.LBAM=CTkLabel(master=self.almacenador,text_color="#4682A9",text="Apellido materno",font=("Poppins",18,"bold")).place(x=30,y=287)
        self.TxBoxAM=CTkEntry(master=self.almacenador,width=150,height=35,text_color="#000000",font=("Poppins",18,"bold"),fg_color="#E0E0E0",corner_radius=10)
        self.TxBoxAM.place(x=30,y=317)

        self.LBFechaN = CTkLabel(master=self.almacenador, text_color="#4682A9", text="Fecha de nacimiento", font=("Poppins", 18, "bold")).place(x=192, y=147)
        self.TxBoxFechaN = CTkEntry(master=self.almacenador,state='disabled', placeholder_text="yy-mm-yyyy", width=120, height=35, text_color="#000000", font=("Poppins", 18, "bold"), fg_color="#E0E0E0", corner_radius=10)
        self.TxBoxFechaN.place(x=192, y=177)
        self.BTCalendario = CTkButton(master=self.almacenador, image=ImgCalendario, text="", anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16, "bold"), corner_radius=10,command=self.mostrar_calendario)
        self.BTCalendario.place(x=318, y=177)

        
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
        #print("documento: "+str(ejecutar_consulta(f"SELECT d.Ruta FROM Empleados e JOIN Relacion_EmpleadosDocumentos re ON e.IDEmpleados = re.IDEmpleados JOIN Documentos d ON re.IDDocumentos = d.IDDocumentos WHERE e.IDEmpleados = {ID} AND d.Tipo = 'INE' ")[0][0]))   
        self.BTVis1=CTkButton(master=self.almacenador  ,image=ImgOjo,text="",anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16,"bold"),corner_radius=10,command= lambda: webbrowser.open(str(ejecutar_consulta(f"SELECT d.Ruta FROM Empleados e JOIN Relacion_EmpleadosDocumentos re ON e.IDEmpleados = re.IDEmpleados JOIN Documentos d ON re.IDDocumentos = d.IDDocumentos WHERE e.IDEmpleados = {ID} AND d.Tipo = 'INE' ")[0][0]))).place(x=390,y=147)
        self.BTVis2=CTkButton(master=self.almacenador  ,image=ImgOjo,text="",anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16,"bold"),corner_radius=10,command= lambda: webbrowser.open(str(ejecutar_consulta(f"SELECT d.Ruta FROM Empleados e JOIN Relacion_EmpleadosDocumentos re ON e.IDEmpleados = re.IDEmpleados JOIN Documentos d ON re.IDDocumentos = d.IDDocumentos WHERE e.IDEmpleados = {ID} AND d.Tipo = 'Carta de recomendacion' ")[0][0]))).place(x=390,y=201)
        self.BTVis3=CTkButton(master=self.almacenador  ,image=ImgOjo,text="",anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16,"bold"),corner_radius=10,command= lambda: webbrowser.open(str(ejecutar_consulta(f"SELECT d.Ruta FROM Empleados e JOIN Relacion_EmpleadosDocumentos re ON e.IDEmpleados = re.IDEmpleados JOIN Documentos d ON re.IDDocumentos = d.IDDocumentos WHERE e.IDEmpleados = {ID} AND d.Tipo = 'Curp' ")[0][0]))).place(x=390,y=254)
        self.BTVis4=CTkButton(master=self.almacenador  ,image=ImgOjo,text="",anchor="e", fg_color="transparent", hover_color="#91C8E4", height=32, width=24, font=("Poppins", 16,"bold"),corner_radius=10,command= lambda: webbrowser.open(str(ejecutar_consulta(f"SELECT d.Ruta FROM Empleados e JOIN Relacion_EmpleadosDocumentos re ON e.IDEmpleados = re.IDEmpleados JOIN Documentos d ON re.IDDocumentos = d.IDDocumentos WHERE e.IDEmpleados = {ID} AND d.Tipo = 'Acta de nacimiento' ")[0][0]))).place(x=390,y=305)


        self.LBINE = CTkLabel(master=self.almacenador, text_color="#4682A9", text="INE", font=("Poppins", 20, "bold")).place(x=700, y=150)
        self.LBImagenINE = CTkLabel(master=self.almacenador, image=ImgIne,text="").place(x=660, y=150)
        
        self.LBCartaRec = CTkLabel(master=self.almacenador, text_color="#4682A9", text="Carta de recomedación", font=("Poppins", 20, "bold")).place(x=700, y=204)
        self.LBImagenCRec = CTkLabel(master=self.almacenador, image=ImgCartaRec,text="").place(x=660, y=204)

        self.LBCURP = CTkLabel(master=self.almacenador, text_color="#4682A9", text="CURP", font=("Poppins", 20, "bold")).place(x=700, y=258)
        self.LBImagenCURP = CTkLabel(master=self.almacenador, image=ImgCURP,text="").place(x=660, y=258)
    
        self.LBDatosActaNac = CTkLabel(master=self.almacenador, text_color="#4682A9", text="Acta de nacimiento", font=("Poppins", 20, "bold")).place(x=700, y=312)
        self.LBImagenANac = CTkLabel(master=self.almacenador, image=ImgActaNac,text="").place(x=660, y=312)
            
        self.botonregresar = CTkButton(master=self.almacenador  ,image=ImgCerrar,text="Regresar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=41, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command=self.destroy).place(x=91, y=390)
        self.botonregresar = CTkButton(master=self.almacenador  ,image=ImgGuardar,text="Guardar",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=41, width=143, font=("Poppins", 16,"bold"),corner_radius=10,command= lambda: self.guardar()).place(x=300, y=390)
        self.iniciar()


class Empleados(Toplevel):
    
    def Eliminar(self):
        def borrar_carpeta(ruta):
            if os.path.isdir(ruta):
                shutil.rmtree(ruta)
            else:
                print(f"La carpeta '{ruta}' no existe.")
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
                # ID = str(r[7])
                # username = os.getlogin()
                # datos = ejecutar_consulta(f"select nombre,apellidop from empleados where idEmpleados = {str(ID)}")
                # destino_carpeta = f"C:/Users/{username}/Documents/Documentos Empleados/{ID} " + str(datos[0][0]) + " " + str(datos[0][1])
                
                ejecutar_modificacion("DELETE FROM LOGFechaHora WHERE IDEmpleados = " + str(r[7]))
                ejecutar_modificacion("DELETE FROM Relacion_EmpleadosDocumentos WHERE IDEmpleados = " + str(r[7]))
                ejecutar_modificacion("DELETE FROM Empleados WHERE IDEmpleados = " + str(r[7]))
                ejecutar_modificacion("DELETE FROM Documentos WHERE IDDocumentos NOT IN (SELECT IDDocumentos FROM Relacion_EmpleadosDocumentos)")
                ruta = "C:/Rostros/Caras/" + str(r[7])
                borrar_carpeta(ruta)
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
            cargarDoc_window=CargaDocs()
            cargarDoc_window.mainloop()


    def Cerrar(self):
        self.destroy()



    def ActualizarLabeles(self, datos):
        id = str(datos)
        resultado = ejecutar_consulta("SELECT e.Nombre, e.ApellidoP,e.ApellidoM,e.FechaNacimiento,h.HoraEntrada,h.HoraSalida,e.FotoRuta,e.IdEmpleados" + 
                                    " FROM Empleados e JOIN Horarios h ON e.IDHorario = h.IDHorario " + "WHERE e.IDEmpleados = " 
                                    + str(datos))
        r = eval(str(resultado[0]))
        nombre = "Nombre: "+ r[0]
        ap = "Apellido Paterno: " + r[1]
        am = "Apellido Materno: " + r[2]
        fn = "Fecha de Nacimiento: " + str(r[3])
        tn = "Turno: " + str(r[4]) + " a "  +str(r[5]) 
        ft = r[6]
        self.LBNombre.configure(text=nombre)
        self.LBApPat.configure(text=ap)
        self.LBApMat.configure(text=am)
        self.LBPuesto.configure(text=fn)
        self.LBTurno.configure(text=tn)
        self.tabla.configure(values=self.iniciartabla(id))
        
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
        

    def iniciartabla(self,id = None):
        print(id)
        if id == None:
            datos=[["Fecha","Hora de ingreso","Hora de salida","Retardo"],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
            return datos
        else:
            datos=[["Fecha","Hora de ingreso","Hora de salida","Retardo"]]
           # for fila in ejecutar_consulta(f"SELECT l.Fecha, l.Hora AS HoraIngreso, (SELECT Hora FROM LOGFechaHora l2 WHERE l2.IDEmpleados = l.IDEmpleados AND l2.Fecha = l.Fecha AND l2.Entrada = 0 LIMIT 1) AS HoraSalida, CASE WHEN TIMESTAMPDIFF(MINUTE, h.HoraEntrada, l.Hora) > 15 THEN 'Retardo' ELSE 'A tiempo' END AS Estado FROM LOGFechaHora l JOIN Empleados e ON l.IDEmpleados = e.IDEmpleados JOIN Horarios h ON e.IDHorario = h.IDHorario WHERE l.IDEmpleados = {id}"):
            #    datos.append(fila)
            datos = datos + ejecutar_consulta(f"SELECT l.Fecha, l.Hora AS HoraIngreso, (SELECT Hora FROM LOGFechaHora l2 WHERE l2.IDEmpleados = l.IDEmpleados AND l2.Fecha = l.Fecha AND l2.Entrada = 0 LIMIT 1) AS HoraSalida, CASE WHEN TIMESTAMPDIFF(MINUTE, h.HoraEntrada, l.Hora) > 15 THEN 'Retardo' ELSE 'A tiempo' END AS Estado FROM LOGFechaHora l JOIN Empleados e ON l.IDEmpleados = e.IDEmpleados JOIN Horarios h ON e.IDHorario = h.IDHorario WHERE l.IDEmpleados = {str(id)}")
            print(datos)
            return datos
        

           # ctypes.windll.user32.MessageBoxW(0,"No se ha logrado cargar la imagen ","FaceLink", 0|32)
    
    def gestionar(self):
        selected_value = self.ComBox.get()
        if selected_value != "":
            lista = eval(selected_value)
            self.Abrir(str(lista[0]))
        else:
            messagebox.showinfo("Facelink","No ha seleccionado una opcion valida")                



    def on_combobox_change(self, event):
        selected_value = self.ComBox.get() 
        lista = eval(selected_value)
        self.ActualizarLabeles(lista[0])
        EmpleadosVal = ()
        EmpleadosVal = ejecutar_consulta("select idEmpleados,nombre,apellidop from empleados")
        EmpleadosVal_str = [str(item) for item in EmpleadosVal]
        self.ComBox.configure(values = EmpleadosVal_str)




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
        ruta_actual = os.getcwd()
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

        self.tablamarco=CTkScrollableFrame(master=self.almacenador,fg_color="transparent")
        self.tablamarco.pack(expand=True, fill="both", padx=20,pady=(170,0))
        self.tabla=CTkTable(master=self.tablamarco, values=self.iniciartabla(),colors=["#EEEEEE", "#EEEEEE"],header_color="#4682A9",text_color="#4682A9")
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
    
    
    
    def LogEntrada(self):
        print("Log inicio")
        ide = Reconocer()
        messagebox.showinfo("Facelink","Ingresado usuario: " + str(ejecutar_consulta(f"select nombre from empleados where idempleados = {ide}")[0][0]))
        ejecutar_procedimiento("insertLOGfechahora",(ide,))


                

    def Abrir(self):
        con = self.TxBoxCon.get()
        usuario = self.TxBoxUs.get()
        if con == "PASSWORD" and usuario == "Admin" or True:
            self.ventana.quit()
            self.ventana.destroy()
            Principal()
        else: 
            messagebox.showinfo("Facelink","Error en los datos!")
        
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
        
        self.botonInfo = CTkButton(master=self.almacenador,text="?",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=32, width=32, font=("Poppins", 32,"bold"),corner_radius=10,command= lambda: webbrowser.open("https://online.publuu.com/570262/1280320"))
        self.botonInfo.place(x=1,y=1)



        self.botonEscanear = CTkButton(master=self.almacenador,text="Escanear Entrada",anchor="e", fg_color="#4682A9", hover_color="#91C8E4", height=32, width=32, font=("Poppins", 32,"bold"),corner_radius=10,command= lambda: self.LogEntrada())
        self.botonEscanear.place(x=80,y=1)
        
        
        
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




