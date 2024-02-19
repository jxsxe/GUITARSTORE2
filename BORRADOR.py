import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import tkinter.messagebox as messagebox
from tkinter import Scrollbar
import pyodbc
#conexion con la base de datoa
try:
    conect = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=ST-JXSXE;'
                      'DATABASE=GuitarStore;'
                      'Trusted_Connection=yes;')
    print("Conexxion exitosa")

except:
    print  ("error al intentar conectar")
cursorinsert=conect.cursor()
# Ejecutar la instrucción SQL para borrar los datos
try:
    cursorinsert.execute('DELETE FROM Producto')
    cursorinsert.commit()
    print("Datos borrados exitosamente")
except:
    print("Error al borrar datos")

#ventana principal
ventana = tk.Tk()
titulo_centrado = " " * 100+ "GUITARSTORE" + " " * 40
ventana.title(titulo_centrado)
ventana.geometry("800x550")
ventana.resizable(False,False)
ventana.iconbitmap("logo.ico") 

# Contenedor principal para el contenido
principal = tk.Frame(ventana)
principal.pack(fill=tk.BOTH, expand=True)

# fondo de la ventana
ruta_fondo = "fondo1.png"
imagen_fondo = tk.PhotoImage(file=ruta_fondo)

fondo_principal = tk.Label(principal, image=imagen_fondo)
fondo_principal.place(relwidth=1, relheight=1)

# Crear un LabelFrame para los Instrumentos===========================================
lfi = tk.LabelFrame(principal, width=750, height=250, relief=tk.SUNKEN)#lfi=LabelFrame Instruments
lfi.place(x=20, y=190)
#fondo del labelframe
flf=tk.PhotoImage(file="fondo.png")
fondolabel=tk.Label(lfi,image=flf)
fondolabel.place(x=0,y=-220)
# Crear un Menu de INSTRUMENTOS
def Objetos_de_combobox( ):
    # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
    nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
    nuevo_marco.place(x=0, y=0)
    # Creamos un canvas dentro del frame principal
    canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
    canvas.place(x=0, y=0)
    def scroll(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    def activar_scroll(event):
        canvas.bind_all("<MouseWheel>", scroll)
    def desactivar_scroll(event):
        canvas.unbind_all("<MouseWheel>")
    flf=tk.PhotoImage(file="fondo.png")
    fondolabel=tk.Label(canvas,image=flf)
    fondolabel.image=flf
    fondolabel.place(x=0,y=-220)
    
    # Frame interior para el contenido del canvas
    global frame_interior
    frame_interior = tk.Frame(canvas, width=750, height=250)
    canvas.create_window((0, 0), window=frame_interior, anchor="nw")
    
    flf=tk.PhotoImage(file="fondo.png").zoom(2)
    fondolabel=tk.Label(frame_interior,image=flf)
    fondolabel.image=flf
    fondolabel.place(x=0,y=-220)
    # Configurar el scrollbar
    scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar_vertical.place(x=733,y=0)
    # Configuramos el canvas y el scrollbar para que funcionen juntos
    canvas.config(yscrollcommand=scrollbar_vertical.set)

    # Conectamos el evento de entrada del ratón para activar el scroll
    canvas.bind("<Enter>", activar_scroll)
    canvas.bind("<Leave>", desactivar_scroll)
    # Crear un botón "Regresar"
    boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
    boton_regresar.place(x=10, y=10)

def crear_objetos(imagen, precio, row, column, subsample, toolip, x, y, Prod,cantidad, valor):
    #OBJETOS GENRALES
    decompras=tk.PhotoImage(file="carrito.png")
    decompras2=decompras.subsample(15)
    ic1=tk.PhotoImage(file=imagen)
    Ric1=ic1.subsample(subsample)
    l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1, pady=10)
    l_ic1.image=Ric1
    l_ic1.grid(row=row,column=column,padx=20)
    pic1=tk.Label(frame_interior, text=precio)
    pic1.grid(row=row+1, column=column)
    bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 10), command=lambda: agregar_al_carrito(Prod,cantidad, valor))
    bic1.image=decompras2
    bic1.grid(row=row+2, column=column, pady=10)
    #toolip1
    def mostrar_tooltip1(event):
        tooltip1.place(x=x,y=y)
    def ocultar_tooltip1(event):
        tooltip1.place_forget()
        # Crear una etiqueta para el tooltip
    tooltip1 = tk.Label(frame_interior, text=toolip, bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
    l_ic1.bind("<Enter>", mostrar_tooltip1)
    l_ic1.bind("<Leave>", ocultar_tooltip1)
        
def Intrumentos_cuerda(event):
    seleccion = event.widget.get()
    combobox_values = event.widget.cget("values")
    if seleccion in combobox_values[1]:#GUITARRAS
        # imagen, precio, row, column, subsample, toolip, nombre , precio, stok
        Objetos_de_combobox()
        crear_objetos( "GIBSON LPTR00WSNH1.png", "Precio: 300,00$", 1, 1, 8, "GIBSON LPTR00WSNH1", 10, 35,"GIBSON LPTR00WSNH1",1,300 )
        crear_objetos( "FENDER 011-3940-761 AM PRO II TELE DK NIT.png", "Precio: 400,00$", 1, 2, 8, "FENDER 011-3940-761 AM PRO II TELE DK NIT",10, 35, "FENDER 011-3940-761 AM PRO II TELE DK NIT",1,400)
        crear_objetos( "EPIPHONE EILS5MGNH1 Les Paul Standard 50s.png", "Precio: 500,00$", 1, 3, 5, "EPIPHONE EILS5MGNH1 Les Paul Standard 50s",10, 35, "EPIPHONE EILS5MGNH1 Les Paul Standard 50s",1, 500)
        crear_objetos( "EPIPHONE EILS6EBNH1 Les Paul Standard 60s.png", "Precio: 600,00$", 1, 4, 5, "EPIPHONE EILS6EBNH1 Les Paul Standard 60s",10, 35, "EPIPHONE EILS6EBNH1 Les Paul Standard 60s",1, 600)
        crear_objetos( "EPIPHONE ENL59ADBNH1 1959 LES PAUL.png", "Precio: 800,00$", 1, 5, 5, "EPIPHONE ENL59ADBNH1 1959 LES PAUL",10, 35, "EPIPHONE ENL59ADBNH1 1959 LES PAUL", 1,800)
        crear_objetos( "EPIPHONE IGMTHUMACHGH1 Masterbilt Hummingbird Aged Cherry.png", "Precio: 1000,00$", 4, 1, 5, "EPIPHONE IGMTHUMACHGH1 Masterbilt Hummingbird Aged Cherry",10, 300, "EPIPHONE IGMTHUMACHGH1 Masterbilt Hummingbird Aged Cherry",1, 1000)
        crear_objetos( "EPIPHONE Les Paul Standard 60s Bourbon Burst EILS6BBNH1.png", "Precio: 1200,00$", 4, 2, 5, "EPIPHONE Les Paul Standard 60s Bourbon Burst EILS6BBNH1",10, 300, "EPIPHONE Les Paul Standard 60s Bourbon Burst EILS6BBNH1",1,1200)
        crear_objetos( "FENDER 011-3910-761 AM PRO II STRAT HSS RW DK NIT.png", "Precio: 1300,00$", 4, 3, 5, "FENDER 011-3910-761 AM PRO II STRAT HSS RW DK NIT",10, 300, "FENDER 011-3910-761 AM PRO II STRAT HSS RW DK NIT", 1,1300)
        crear_objetos( "FENDER 011-3942-700 AM PRO II TELE MN 3TS.png", "Precio: 800,00$", 4, 4, 5, "FENDER 011-3942-700 AM PRO II TELE MN 3TS",10, 300, "FENDER 011-3942-700 AM PRO II TELE MN 3TS",1,800)
        crear_objetos( "FENDER 014-4502-506 PLAYER STRAT MN BLK.png", "Precio: 700,00$", 4, 5, 5, "FENDER 014-4502-506 PLAYER STRAT MN BLK",10, 300, "FENDER 014-4502-506 PLAYER STRAT MN BLK",1, 700)
        crear_objetos( "FENDER 097-2512-121 HIGHWAY.png", "Precio: 1000,00$", 7, 1, 5, "FENDER 097-2512-121 HIGHWAY", 10, 500, "FENDER 097-2512-121 HIGHWAY",1, 1000)
        crear_objetos( "GIBSON LPST00KHCH1.png", "Precio: 1300,00$", 7, 2, 5, "GIBSON LPST00KHCH1", 10, 500, "GIBSON LPST00KHCH1", 1,1300)
        crear_objetos( "GIBSON LPTR00FHNH1.png", "Precio: 800,00$", 7, 3, 5, "GIBSON LPTR00FHNH1", 10, 500, "GIBSON LPTR00FHNH1",1, 800)
        crear_objetos( "GIBSON SGTR00AYNH1.png", "Precio: 1500,00$", 10, 1, 5, "GIBSON SGTR00AYNH1", 10, 700, "GIBSON SGTR00AYNH1", 1,1500)
        crear_objetos( "TAYLOR AD17e BLACKTOP.png", "Precio: 500,00$", 10, 2, 5, "TAYLOR AD17e BLACKTOP", 10, 700, "TAYLOR AD17e BLACKTOP",1, 500)
        crear_objetos( "FENDER AMERICAN PERF STRAT HSS RW 3TSB.png", "Precio: 900,00$", 7, 5, 5, "FENDER AMERICAN PERF STRAT HSS RW 3TSB", 10, 500, "FENDER AMERICAN PERF STRAT HSS RW 3TSB", 1,900)
        crear_objetos( "FENDER 014-9122-306 VINT II 70S JAGUAR MN BLK.png", "Precio: 1300,00$", 7, 4, 5, "FENDER 014-9122-306 VINT II 70S JAGUAR MN BLK", 10, 500, "FENDER 014-9122-306 VINT II 70S JAGUAR MN BLK",1, 1300)
    elif seleccion in combobox_values[2]:#BAJOS
        Objetos_de_combobox()
        crear_objetos( "SPECTOR-NSDM5HAUNT-NS-Dimension-5-–.png", "Precio: 550,00$", 1, 1, 5, "SPECTOR-NSDM5HAUNT-NS-Dimension-5", 10, 35, "SPECTOR-NSDM5HAUNT-NS-Dimension-5", 1,550)
        crear_objetos("FENDER 014-7363-323 PP ACTIVE P BASS PF OLP.png", "Precio: 1100,00$", 1, 2, 5, "FENDER 014-7363-323 PP ACTIVE P BASS PF OLP",10, 35, "FENDER 014-7363-323 PP ACTIVE P BASS PF OLP",1, 1100)
        crear_objetos("FENDER 014-7373-300 PP ACTIVE JAZZ BASS PF 3TSB.png", "Precio: 600,00$", 1, 3, 5, "FENDER 014-7373-300 PP ACTIVE JAZZ BASS PF 3TSB",10, 35, "FENDER 014-7373-300 PP ACTIVE JAZZ BASS PF 3TSB", 1,600)
        crear_objetos("FENDER 014-9212-306 VINT II 50S P BASS MN BLK.png", "Precio: 400,50$", 1, 4, 5, "FENDER 014-9212-306 VINT II 50S P BASS MN BLK",10, 35, "FENDER 014-9212-306 VINT II 50S P BASS MN BLK",1, 400.50)
        crear_objetos("SPECTOR NSDM5HAUNT NS Dimension 5 – Haunted Moss Matte.png", "Precio: 600,00$", 7, 1, 5, "SPECTOR NSDM5HAUNT NS Dimension 5 – Haunted Moss Matte",10, 300, "SPECTOR NSDM5HAUNT NS Dimension 5 – Haunted Moss Matte", 1,600)
        crear_objetos("SPECTOR NSDM5SFB NS Dimension 5 – Inferno Red.png", "Precio: 1000,00$", 7, 2, 5, "SPECTOR NSDM5SFB NS Dimension 5 – Inferno Red",10, 300, "SPECTOR NSDM5SFB NS Dimension 5 – Inferno Red", 1,1000)
        crear_objetos("SPECTOR NSPULSE6BSM NS Pulse I – Black Stain Matte.png", "Precio: 1000,00$", 7, 3, 5, "SPECTOR NSPULSE6BSM NS Pulse I – Black Stain Matte",10, 300, "SPECTOR NSPULSE6BSM NS Pulse I – Black Stain Matte",1, 1000)
       
    elif seleccion in combobox_values[3]:#VIOLINES
        Objetos_de_combobox()
        crear_objetos( "PRIMER VIOLIN 1.png", "Precio: 555,00$", 1, 1, 8, "PRIMER VIOLIN 1",10, 35, "PRIMER VIOLIN 1",1, 555)
        crear_objetos( "PRIMER VIOLIN 1-4″.png", "Precio: 700,00$", 1, 2, 8, "PRIMER VIOLIN 1-4″",10, 35, "PRIMER VIOLIN 1-4″",1,700)
        crear_objetos( "PRIMER VIOLIN 1-8″.png", "Precio: 700,00$", 1, 3, 8, "PRIMER VIOLIN 1-8″",10, 35, "PRIMER VIOLIN 1-8″",1, 700)
        crear_objetos( "PRIMER VIOLIN 3.png", "Precio: 1150,00$", 4, 1, 8, "PRIMER VIOLIN 3",10, 200, "PRIMER VIOLIN 3",1, 1150)
        crear_objetos( "PRIMER VIOLIN 4.png", "Precio: 2000,00$", 4, 2, 8, "PRIMER VIOLIN 4",10, 200, "PRIMER VIOLIN 4",1, 2000)
    elif seleccion in combobox_values[4]:#UKELELES
        Objetos_de_combobox()
        crear_objetos( "CORDOBA 28S SOPRANO UKELELE.png", "Precio: 500,00$", 1, 1, 8, "CORDOBA 28S SOPRANO UKELELE", 10, 35, "CORDOBA 28S SOPRANO UKELELE",1, 500)
        crear_objetos( "CORDOBA U1 PROTEGE UKELELE.png", "Precio: 450,00$", 1, 2, 8, "CORDOBA U1 PROTEGE UKELELE", 10, 35,"CORDOBA U1 PROTEGE UKELELE",1, 450)
        crear_objetos( "CORDOBA U1MS Soprano Ukelele.png", "Precio: 300,00$", 1, 3, 8, "CORDOBA U1MS Soprano Ukelele", 10, 35,"CORDOBA U1MS Soprano Ukelele",1,300 )
        crear_objetos( "EPIPHONE EUELNSBH1 Epilani Soprano Ukelele.png", "Precio: 250,00$", 4, 1, 8, "EPIPHONE EUELNSBH1 Epilani Soprano Ukelele", 10, 200, "EPIPHONE EUELNSBH1 Epilani Soprano Ukelele",1, 250)
        crear_objetos( "EPIPHONE EULPHSNH1 LES PAUL AC.png", "Precio: 600,00$", 4, 2, 8, "EPIPHONE EULPHSNH1 LES PAUL AC", 10, 200, "EPIPHONE EULPHSNH1 LES PAUL AC",1, 600)
        crear_objetos( "CORDOBA U1MS Soprano Ukelele.png", "Precio: 180,00$", 4, 3, 8, "CORDOBA U1MS Soprano Ukelele", 10, 200, "CORDOBA U1MS Soprano Ukelele",1, 180)
def Intrumentos_percusion(event):
    seleccion = event.widget.get()
    combobox_values = event.widget.cget("values")
    if seleccion in combobox_values[1]:#BATERIAS ACUSTICAS
        Objetos_de_combobox()
        crear_objetos( "MAPEX Armony LTAR628SFUJG.png", "Precio: 1200,00$", 1, 1, 8, "MAPEX Armony LTAR628SFUJG", 10, 35, "MAPEX Armony LTAR628SFUJG",1, 1200)
        crear_objetos( "MAPEX Armory AR504SET.png", "Precio: 950,00$", 1, 2, 8, "MAPEX Armory AR504SET", 10 ,35, "MAPEX Armory AR504SET",1, 950)
        crear_objetos("MAPEX Armory AR504SVL.png", "Precio: 500,00$", 1, 3, 5, "MAPEX Armory AR504SVL",10, 35, "MAPEX Armory AR504SVL", 1,500)
        crear_objetos("MAPEX Armory AR628SET.png", "Precio: 650,00$", 4, 1, 5, "MAPEX Armory AR628SET",10, 200, "MAPEX Armory AR628SET", 1,650)
        crear_objetos("MAPEX Armory LTAR628SFUCH.png", "Precio: 249,99$", 4, 2, 5, "MAPEX Armory LTAR628SFUCH",10, 200, "MAPEX Armory LTAR628SFUCH",1,249.99 )
        crear_objetos("MAPEX Saturn SR628XRQ.png", "Precio: 249,99$", 4, 3, 5, "MAPEX Saturn SR628XRQ",10, 200, "MAPEX Saturn SR628XRQ",1, 249.99)
    elif seleccion in combobox_values[2]:#BATERIAS ELECTRONICAS
        Objetos_de_combobox()
        crear_objetos("ARTESIA A-30.png", "Precio: 1299,99$", 1, 1, 5, "ARTESIA A-30",10, 35, "ARTESIA A-30",1, 1299.99)
        crear_objetos("ROLAND OCTAPAD SPD-30 BLACK.png", "Precio: 3005$", 1, 2, 5, "ROLAND OCTAPAD SPD-30 BLACK",10, 35, "ROLAND OCTAPAD SPD-30 BLACK",1, 3005)
        crear_objetos("ROLAND OCTAPAD SPD-30.png", "Precio: 4500,00$", 1, 3, 5, "ROLAND OCTAPAD SPD-30",10, 35, "ROLAND OCTAPAD SPD-30",1, 4500)
        crear_objetos("ROLAND TD-02KV.png", "Precio: 1200,00$", 4, 1, 5, "ROLAND TD-02KV",10, 200, "ROLAND TD-02KV",1, 1200)
        crear_objetos("ROLAND TD-17KV+MDS-COM.png", "Precio: 850,00$", 4, 2, 5, "ROLAND TD-17KV+MDS-COM",10, 200, "ROLAND TD-17KV", 1,850)
        crear_objetos("ROLAND TD-17KVX+MDS-COM.png", "Precio: 1000,00$", 4, 3, 5, "ROLAND TD-17KVX+MDS-COM",10, 200, "ROLAND TD-17KVX", 1,1000)
    elif seleccion in combobox_values[3]:#PLATILLOS
        Objetos_de_combobox()
        crear_objetos("ISTANBUL MEHMET SA-SET1.png", "Precio: 250,00$", 1, 1, 5, "ISTANBUL MEHMET SA-SET1",10, 35, "ISTANBUL MEHMET SA-SET1",1, 250)
        crear_objetos("ISTANBUL MEHMET SUL-SET.png", "Precio: 100,00$", 1, 2, 5, "ISTANBUL MEHMET SUL-SET",10, 35, "ISTANBUL MEHMET SUL-SET",1, 100)
        crear_objetos("ISTANBUL MEHMET TR-SET.png", "Precio: 80,00$", 1, 3, 5, "ISTANBUL MEHMET TR-SET",10,35, "ISTANBUL MEHMET TR-SET",1, 80)
        crear_objetos("SABIAN AAX X-plosion Set 2500587XPB.png", "Precio: 100,00$", 4, 1, 5, "SABIAN AAX X-plosion Set 2500587XPB",10, 200, "SABIAN AAX X-plosion Set 2500587XPB", 1,100)
        crear_objetos("SABIAN Sabian 21402XLB 14″.png", "Precio: 300,00$", 4, 2, 5, "SABIAN Sabian 21402XLB 14″",10, 200, "SABIAN Sabian 21402XLB 14",1, 300)
        crear_objetos("SABIAN Sabian XSR Performance Set.png", "Precio: 400,00$", 4, 3, 5, "SABIAN Sabian XSR Performance Set",10, 200, "SABIAN Sabian XSR Performance Set", 1,400)
    elif seleccion in combobox_values[4]:#pPERCUSION LATINA
        Objetos_de_combobox()
        crear_objetos("GON BOPS TP1150N.png", "Precio: 150,00$", 1, 1, 5, "GON BOPS TP1150N",10, 35, "GON BOPS TP1150N",1, 150)
        crear_objetos("LP ASPIRE 13″ AND 14″ TIMBALES LPA256.png", "Precio: 99,99$", 1, 2, 5, "LP ASPIRE 13″ AND 14″ TIMBALES LPA256",10, 35, "LP ASPIRE 13″ AND 14″ TIMBALES LPA256",1, 99.99)
        crear_objetos("LP CONGA SET CITY SERIES 11″+12″ DARK WOOD LP647NY-DW.png", "Precio: 60,00$", 1, 3, 5, "LP CONGA SET CITY SERIES 11″+12″ DARK WOOD LP647NY-DW",10, 35, "LP CONGA SET CITY SERIES 11″+12″ DARK WOOD LP647NY-DW",1, 60)
        crear_objetos("LP CONGA SET CITY SERIES 11″+12″ NATURAL LP647NY-AW.png", "Precio: 45,00$", 4, 1, 5, "LP CONGA SET CITY SERIES 11″+12″ NATURAL LP647NY-AW",10, 200, "LP CONGA SET CITY SERIES 11″+12″ NATURAL LP647NY-AW", 1,45)
        crear_objetos("LP CONGA SET CITY SERIES 11″+12″ VINTAGE SUNBURST LP647NY-VSB.png", "Precio: 100,00$", 4, 2, 5, "LP CONGA SET CITY SERIES 11″+12″ VINTAGE SUNBURST LP647NY-VSB",10, 200, "LP CONGA SET CITY SERIES 11″+12″ VINTAGE SUNBURST LP647NY-VSB", 1,100)
        crear_objetos("LP MATADOR 14″ AND 15″ BARRIO DEEP SHELL TIMBALES M258.png", "Precio: 25,00$", 4, 3, 5, "LP MATADOR 14″ AND 15″ BARRIO DEEP SHELL TIMBALES M258",10, 200, "LP MATADOR 14″ AND 15″ BARRIO DEEP SHELL TIMBALES M258",1, 25 )
    elif seleccion in combobox_values[5]:#MARCHA
        Objetos_de_combobox()
        crear_objetos("GON BOPS CJDR DANIEL DE LOS REYES DIGN CAJON.png", "Precio: 1500,00$", 1, 1, 5, "GON BOPS CJDR DANIEL DE LOS REYES DIGN CAJON",10, 35, "GON BOPS CJDR DANIEL DE LOS REYES DIGN CAJON",1, 1500)
        crear_objetos("LP ASPIRE ACCENTS CAJON DARKWOOD LPA1332-DWSI.png", "Precio: 900,00$", 1, 2, 5, "LP ASPIRE ACCENTS CAJON DARKWOOD LPA1332-DWSI",10, 35,"LP ASPIRE ACCENTS CAJON DARKWOOD LPA1332-DWSI",1, 900 )
        crear_objetos("LP ASPIRE ACCENTS CAJON WHITE STREAK LPA1332-WSI.png", "Precio: 750,00$", 1, 3, 5, "LP ASPIRE ACCENTS CAJON WHITE STREAK LPA1332-WSI",10, 35, "LP ASPIRE ACCENTS CAJON WHITE STREAK LPA1332-WSI", 1,750)
        crear_objetos("LP ASPIRE CAJON HAVANA CAFE LPA1332-HCI.png", "Precio: 1900,00$", 4, 1, 5, "LP ASPIRE CAJON HAVANA CAFE LPA1332-HCI",10, 200, "LP ASPIRE CAJON HAVANA CAFE LPA1332-HCI",1, 1900)
        crear_objetos("LP GROOVE WIRE CAJON LP1427W.png", "Precio: 600,00$", 4, 2, 5, "LP GROOVE WIRE CAJON LP1427W",10, 200, "LP GROOVE WIRE CAJON LP1427W",1, 600)
        crear_objetos("LP MATADOR SERIES WOOD BONGOS NATURAL.png", "Precio: 1700,00$", 4, 3, 5, "LP MATADOR SERIES WOOD BONGOS NATURAL",10, 200, "LP MATADOR SERIES WOOD BONGOS NATURAL",1, 1700)
def TECLADO(event):
    seleccion = event.widget.get()
    combobox_values = event.widget.cget("values")
    if seleccion in combobox_values[1]:#Pianos
        Objetos_de_combobox()
        crear_objetos( "MEDELI MK200.png", "Precio: 2500,00$", 1, 1, 8, "MEDELI MK200", 10, 35, "MEDELI MK200",1, 2500)
        crear_objetos( "ROLAND E-X10 Arranger Keyboard.png", "Precio: 2500,00$", 1, 2, 8, "ROLAND E-X10 Arranger Keyboard", 10 ,35, "ROLAND E-X10 Arranger Keyboard", 1,2500)
        crear_objetos("ROLAND E-X50.png", "Precio: 1500,00$", 1, 3, 5, "ROLAND E-X50",10, 35, "ROLAND E-X50",1, 1500)       
def Intrumentos_viento(event):
    seleccion = event.widget.get()
    combobox_values = event.widget.cget("values")
    if seleccion in combobox_values[1]:#trompetas
        Objetos_de_combobox()
        crear_objetos( "PRIMER TA-NATR-213 TROMPETA NIQUELADA.png", "Precio: 800,00$", 1, 1, 8, "PRIMER TA-NATR-213 TROMPETA NIQUELADA", 10, 35, "PRIMER TA-NATR-213 TROMPETA NIQUELADA", 1,800)
        crear_objetos( "TROMPETA PROEL GR STR500 LACCATA GRASSI WESTUCHE.png", "Precio: 1600,00$", 1, 2, 8, "TROMPETA PROEL GR STR500 LACCATA GRASSI WESTUCHE", 10 ,35, "TROMPETA PROEL GR STR500 LACCATA GRASSI WESTUCHE",1, 1600)
        crear_objetos("TROMPETA PROEL GR TR210AG SILVER PLATED.png", "Precio: 1450,00$", 1, 3, 5, "TROMPETA PROEL GR TR210AG SILVER PLATED",10, 35, "TROMPETA PROEL GR TR210AG SILVER PLATED", 1,1450)  
    elif seleccion in combobox_values[2]:#Saxofon
        Objetos_de_combobox()
        crear_objetos( "DADDARIO Rico Royal Alto Saxophone Reeds SAXO ALTO.png", "Precio: 600,00$", 1, 1, 8, "DADDARIO Rico Royal Alto Saxophone Reeds SAXO ALTO", 10, 35, "DADDARIO Rico Royal Alto Saxophone Reeds SAXO ALTO",1, 600)
        crear_objetos( "DADDARIO RRP05TSX150.png", "Precio: 450,00$", 1, 2, 8, "DADDARIO RRP05TSX150", 10 ,35, "DADDARIO RRP05TSX150",1, 450)
        crear_objetos("PRIMER SA-N.png", "Precio: 325,00$", 1, 3, 5, "PRIMER SA-N",10, 35, "PRIMER SA-N", 1,325)       
def Others(event):
    seleccion = event.widget.get()
    combobox_values = event.widget.cget("values")
    if seleccion in combobox_values[1]:#Cuerdas
        Objetos_de_combobox()
        crear_objetos( "DADDARIO EPS170-5SL XL ProSteels Round Wound.png", "Precio: 100,00$", 1, 1, 8, "DADDARIO EPS170-5SL XL ProSteels Round Wound", 10, 35, "DADDARIO EPS170-5SL XL ProSteels Round Wound", 1,100)
        crear_objetos( "DADDARIO J610 34M PRELUDE BASS SET 34M.png", "Precio: 80,00$", 1, 2, 8, "DADDARIO J610 34M PRELUDE BASS SET 34M", 10 ,35, "DADDARIO J610 34M PRELUDE BASS SET 34M", 1,80)
        crear_objetos("DADDARIO K610 34M KAPLAN BASS SET 34 MED.png", "Precio: 75,00$", 1, 3, 5, "DADDARIO K610 34M KAPLAN BASS SET 34 MED",10, 35, "DADDARIO K610 34M KAPLAN BASS SET 34 MED",1, 75)
    elif seleccion in combobox_values[2]:#Pedales
        Objetos_de_combobox()
        crear_objetos("ERNIE BALL EXPRESSION TREMOLO PEDAL P06188.png", "Precio: 80,00$", 1, 1, 5, "ERNIE BALL EXPRESSION TREMOLO PEDAL P06188",10, 35, "ERNIE BALL EXPRESSION TREMOLO PEDAL P06188",1, 80)
        crear_objetos("ERNIE BALL P06167 25K STEREO VOLUME PEDAL.png", "Precio: 45,00$", 1, 2, 5, "ERNIE BALL P06167 25K STEREO VOLUME PEDAL",10, 35, "ERNIE BALL P06167 25K STEREO VOLUME PEDAL",1, 45)
        crear_objetos("ERNIE BALL P06183 EXPRESSION OVERDRIVE.png", "Precio: 30,00$", 1, 3, 5, "ERNIE BALL P06183 EXPRESSION OVERDRIVE",10, 35, "ERNIE BALL P06183 EXPRESSION OVERDRIVE", 1,30)


Guitarras_bajos=["Instrimentos de Cuerda","Guitarras",
                  "Bajos", "Violines", "Ukeleles"]
Baterias=["Percucion","Baterias Acusticas", "Baterias Electronicas",
           "Platillos","Percusion Latina", "Cajas Percucion"]
Teclado=["Teclados", "Pianos"]
Viento=["Instrumentos de Aire","Trompetas",
         "Saxofon"]
Cuerda=["Otros","Cuerdas", "Pedales"]
Instrumentos = ttk.Combobox(lfi, values=Guitarras_bajos)
Instrumentos.set(Guitarras_bajos[0])
Instrumentos.place(x=10,y=0)

Instrumentos2=ttk.Combobox(lfi,values=Baterias)
Instrumentos2.set(Baterias[0])
Instrumentos2.place(x=155,y=0)

Instrumentos3=ttk.Combobox(lfi,values=Teclado)
Instrumentos3.set(Teclado[0])
Instrumentos3.place(x=300,y=0)

Instrumentos4=ttk.Combobox(lfi,values=Viento)
Instrumentos4.set(Viento[0])
Instrumentos4.place(x=445,y=0)

Instrumentos5=ttk.Combobox(lfi,values=Cuerda)
Instrumentos5.set(Cuerda[0])
Instrumentos5.place(x=590,y=0)

# Vincular la selección de combobox a la función crear_marco
Instrumentos.bind("<<ComboboxSelected>>", Intrumentos_cuerda)
Instrumentos2.bind("<<ComboboxSelected>>", Intrumentos_percusion)
Instrumentos3.bind("<<ComboboxSelected>>", TECLADO)
Instrumentos4.bind("<<ComboboxSelected>>", Intrumentos_viento)
Instrumentos5.bind("<<ComboboxSelected>>", Others)
#OFERTAS QUE VAN EN lfi============================================================0
                    #========================================================= 
    #OBJETOS GENRALES
carro=tk.PhotoImage(file="carrito.png")
carro2=carro.subsample(15)

ofertitas=ttk.Treeview( ventana, columns=('Id', 'Nombre', 'stok', 'Precio'), show="headings")
ofertitas.heading('Id', text="#")
ofertitas.column('Id', width=10)
ofertitas.heading('Nombre', text='Instrumento')
ofertitas.column('Nombre',width=100)
ofertitas.heading('Precio', text='Valor unitario')
ofertitas.column('Precio', width=10)
ofertitas.heading('stok', text='Cantidad')
ofertitas.column('stok', width=50)
#ofertitas.place(x=0,y=10)
def agregar_al_carrito( nombre,cantidad, precio):
    for item in ofertitas.get_children():
        if ofertitas.item(item, 'values')[1] == nombre:#verifica si el nombre de repite
            # Si el producto ya está en la tabla, actualiza la cantidad y el precio
            cantidad_actual = int(ofertitas.item(item, 'values')[2])
            nueva_cantidad=0
            nueva_cantidad = cantidad_actual + cantidad
            nuevo_precio = float(ofertitas.item(item, 'values')[3].replace('$', '')) + (cantidad * float(precio))
            nuevo_precio_con_signo = f"${nuevo_precio:.2f}"  # Agregar el signo de dólar al nuevo precio
            ofertitas.item(item, values=(ofertitas.item(item, 'values')[0], nombre, nueva_cantidad, nuevo_precio_con_signo))
            # Actualizar la cantidad y el precio en la base de datos
            cursorinsert.execute("UPDATE Producto SET stock = ?, precio = ? WHERE Cod_Producto = ?", (nueva_cantidad, nuevo_precio_con_signo, ofertitas.item(item, 'values')[0]))
            cursorinsert.commit()
            print("Dato actualizados exitosamente")
            messagebox.showinfo("Éxito", f"Producto agregado al carrito {nueva_cantidad} veces") 
            return
    global id_contador# Variable global para mantener el contador de ID
    id_contador = id_contador+1  # Incrementa el contador de ID
    nuevo_id = id_contador  
    ofertitas.insert('', 'end', values=(nuevo_id, nombre, cantidad,f"{cantidad*float(precio)}$" ))
    print(ofertitas)
    cursorinsert.execute("INSERT INTO Producto (Cod_Producto, nombre_producto, stock, precio) VALUES (?, ?, ?, ?)", (nuevo_id, nombre, cantidad, f"{cantidad*float(precio)}$"))
    cursorinsert.commit()
    print("datos ingresados exitosamente")
    messagebox.showinfo("Éxito", "Producto agregado al carrito")        
        
id_contador=0

#OBJETO 1
of1=tk.PhotoImage(file="GIBSON LPTR00FHNH1.png")
r_of1=of1.subsample(8)
l_of1=tk.Label(lfi,width=110, height=130, image=r_of1, bg="white", relief=tk.SOLID, borderwidth=1)
l_of1.place(x=20,y=35)
bof1=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8), command=lambda: agregar_al_carrito("GIBSON LPTR00FHNH1",1, 1000))
bof1.place(x=20, y=190)
Lof1=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof1.place(x=80,y=30)
pof1=tk.Label(lfi, text="Precio: 1000,00$")
pof1.place(x=30,y=170)
#OBJETO 2
of2=tk.PhotoImage(file="FENDER 014-7373-300 PP ACTIVE JAZZ BASS PF 3TSB.png")
r_of2=of2.subsample(9)
l_of2=tk.Label(lfi,width=110, height=130, image=r_of2, bg="white", relief=tk.SOLID, borderwidth=1)
l_of2.place(x=155,y=35)
bof2=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8), command=lambda: agregar_al_carrito("FENDER 014-7373-300 PP ACTIVE JAZZ BASS PF 3TSB",1, 500))
bof2.place(x=155, y=190)
Lof2=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof2.place(x=200,y=30)
pof2=tk.Label(lfi, text="Precio: 500,00$")
pof2.place(x=155,y=170)
#OBJETO3
of3=tk.PhotoImage(file="LP CONGA SET CITY SERIES 11″+12″ DARK WOOD LP647NY-DW.png")
r_of3=of3.subsample(9)
l_of3=tk.Label(lfi,width=110, height=130, image=r_of3, bg="white", relief=tk.SOLID, borderwidth=1)
l_of3.place(x=310,y=35)
bof3=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8), command=lambda:agregar_al_carrito("LP CONGA SET CITY SERIES 11″+12″ DARK WOOD LP647NY-DW",1, 199.99 ))
bof3.place(x=310, y=190)
Lof3=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof3.place(x=370,y=30)
pof3=tk.Label(lfi, text="Precio: 199,99$")
pof3.place(x=310,y=170)
#OBJETO4
of4=tk.PhotoImage(file="ERNIE BALL EXPRESSION TREMOLO PEDAL P06188.png")
r_of4=of4.subsample(10)
l_of4=tk.Label(lfi,width=110, height=130, image=r_of4, bg="white", relief=tk.SOLID, borderwidth=1)
l_of4.place(x=465,y=35)
bof4=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8), command=lambda: agregar_al_carrito("ERNIE BALL EXPRESSION TREMOLO PEDAL P06188",1,90))
bof4.place(x=465, y=190)
Lof4=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof4.place(x=530,y=30)
pof4=tk.Label(lfi, text="Precio: 90,00$")
pof4.place(x=465,y=170)
#OBJETO5
of5=tk.PhotoImage(file="MAPEX Armony LTAR628SFUJG.png")
r_of5=of5.subsample(8)
l_of5=tk.Label(lfi,width=110, height=130, image=r_of5, bg="white", relief=tk.SOLID, borderwidth=1)
l_of5.place(x=620,y=35)
bof5=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8), command=lambda: agregar_al_carrito("MAPEX Armony LTAR628SFUJG",1, 500))
bof5.place(x=620, y=190)
Lof5=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof5.place(x=680,y=30)
pof5=tk.Label(lfi, text="Precio: 500,00$")
pof5.place(x=610,y=170)
#toolip1
def mostrar_tooltip1(event):
    tooltip1.place(x=20,y=35)
def ocultar_tooltip1(event):
    tooltip1.place_forget()
    # Crear una etiqueta para el tooltip
tooltip1 = tk.Label(lfi, text="GIBSON LPTR00FHNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of1.bind("<Enter>", mostrar_tooltip1)
l_of1.bind("<Leave>", ocultar_tooltip1)
#toolip2
def mostrar_tooltip2(event):
    tooltip2.place(x=145,y=35)
def ocultar_tooltip2(event):
    tooltip2.place_forget()
    # Crear una etiqueta para el tooltip
tooltip2 = tk.Label(lfi, text="FENDER 014-7373-300 PP ACTIVE JAZZ BASS PF 3TSB", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of2.bind("<Enter>", mostrar_tooltip2)
l_of2.bind("<Leave>", ocultar_tooltip2)
#toolip3
def mostrar_tooltip3(event):
    tooltip3.place(x=300,y=35)
def ocultar_tooltip3(event):
    tooltip3.place_forget()
    # Crear una etiqueta para el tooltip
tooltip3 = tk.Label(lfi, text="LP CONGA SET CITY SERIES 11″+12″ DARK WOOD LP647NY-DW", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of3.bind("<Enter>", mostrar_tooltip3)
l_of3.bind("<Leave>", ocultar_tooltip3)
#toolip4
def mostrar_tooltip4(event):
    tooltip4.place(x=455,y=35)
def ocultar_tooltip4(event):
    tooltip4.place_forget()
    # Crear una etiqueta para el tooltip
tooltip4 = tk.Label(lfi, text="ERNIE BALL EXPRESSION TREMOLO PEDAL P06188", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of4.bind("<Enter>", mostrar_tooltip4)
l_of4.bind("<Leave>", ocultar_tooltip4)
#toolip5
def mostrar_tooltip5(event):
    tooltip5.place(x=600,y=200)
def ocultar_tooltip5(event):
    tooltip5.place_forget()
    # Crear una etiqueta para el tooltip
tooltip5 = tk.Label(ventana, text="MAPEX Armony LTAR628SFUJG", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of5.bind("<Enter>", mostrar_tooltip5)
l_of5.bind("<Leave>", ocultar_tooltip5) 

                    #==================================================000
#===============================================================================
global Factura
# Crear boton para registrarse==================================================
datos_registro = {}

def iniciar_sesion():
    # Ventana para iniciar sesión
    ventana_inicio_sesion = tk.Toplevel()
    ventana_inicio_sesion.title("Iniciar Sesión")
    ventana_inicio_sesion.geometry("300x200")
    ventana_inicio_sesion.resizable(False, False)

    # Función para verificar el inicio de sesión
    def verificar_inicio_sesion():
        correo = correo_entry.get()
        contrasena = contrasena_entry.get()
        if correo in datos_registro and datos_registro[correo] == contrasena:
            tk.messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            ventana_inicio_sesion.destroy()  # Cierra la ventana de inicio de sesión
        else:
            tk.messagebox.showerror("Error", "Correo o contraseña incorrectos")
    
    # Campos del formulario de inicio de sesión
    tk.Label(ventana_inicio_sesion, text="Correo electrónico:").pack()
    correo_entry = tk.Entry(ventana_inicio_sesion)
    correo_entry.pack()
    
    tk.Label(ventana_inicio_sesion, text="Contraseña:").pack()
    contrasena_entry = tk.Entry(ventana_inicio_sesion, show="*")
    contrasena_entry.pack()

    # Botón para iniciar sesión
    tk.Button(ventana_inicio_sesion, text="Iniciar Sesión", command=verificar_inicio_sesion).pack()

def registrarse():
    ventana_de_registro = tk.Toplevel()
    ventana_de_registro.title("REGISTRARSE")
    ventana_de_registro.geometry("300x200")
    ventana_de_registro.resizable(False, False)
    
    def registrar_usuario():
        correo = correo_entry.get()
        contrasena = contrasena_entry.get()
        datos_registro[correo] = contrasena
        tk.messagebox.showinfo("Éxito", "Registro exitoso")
        ventana_de_registro.destroy()
    
    tk.Label(ventana_de_registro, text="Correo electrónico:").pack()
    correo_entry = tk.Entry(ventana_de_registro)
    correo_entry.pack()
    
    tk.Label(ventana_de_registro, text="Contraseña:").pack()
    contrasena_entry = tk.Entry(ventana_de_registro, show="*")
    contrasena_entry.pack()

    tk.Button(ventana_de_registro, text="Registrarse", command=registrar_usuario).pack()

# Función que crea la ventana principal
def Ventana_De_Account():
    ventanaRL=tk.Toplevel(ventana)
    ventanaRL.title("INICIAR SESIÓN")
    ventanaRL.geometry("500x550")
    ventanaRL.resizable(False,False)
    ventanaRL.iconbitmap("logo.ico")
    label = tk.Label(ventanaRL, text="Ventana Opción " )
    label.pack(pady=20)

    # Botón de inicio de sesión
    boton_inicio_sesion = tk.Button(ventanaRL, text="Iniciar Sesión", command=iniciar_sesion)
    boton_inicio_sesion.pack(pady=20)

    # Botón de registro
    boton_registro = tk.Button(ventanaRL, text="Registrarse", command=registrarse)
    boton_registro.pack(pady=20)

    #BOTON DE REGRESAR 
    boton_volver = tk.Button(ventanaRL, text="Volver a la ventana principal", command=ventanaRL.destroy)
    boton_volver.pack()


registro_imagen=tk.PhotoImage(file="singup.png")
sing_up=registro_imagen.subsample(15)
boton_inicio=tk.Button(principal, image=sing_up,bd=10, highlightthickness=1, padx=2, compound="left", command=Ventana_De_Account)
boton_inicio.place(x=550,y=10)
boton_inicio.config(bg="white")
def mostrar_tooltip(event):
    tooltip.place(x=550,y=70)
def ocultar_tooltip(event):
    tooltip.place_forget()
# Crear una etiqueta para el tooltip
tooltip = tk.Label(ventana, text="Mi Cuenta", bg="white", relief=tk.SOLID, borderwidth=1, font=("norwester",10))
boton_inicio.bind("<Enter>", mostrar_tooltip)
boton_inicio.bind("<Leave>", ocultar_tooltip)
#crear boton para ir a comprar====================================================================================================================================================================

def ir_a_comprar():
    def agregar():
        # Obtener el item seleccionado en el Treeview
        selected_item = tabla.focus()
        if selected_item:
            # Obtener los valores del item seleccionado
            values = tabla.item(selected_item, 'values')
            nuevo_precio = (float(values[3].replace('$', '')) / int(values[2]))
            # Obtener el nuevo valor de la cantidad
            nueva_cantidad = int(values[2]) + 1
            # Actualizar el valor de la cantidad en el Treeview
            tabla.item(selected_item, values=(values[0], values[1], nueva_cantidad, values[3]))
            # Obtener el nuevo precio
            nuevo_precio = nueva_cantidad * nuevo_precio
            # Actualizar el precio en el Treeview
            tabla.item(selected_item, values=(values[0], values[1], nueva_cantidad, f"${nuevo_precio:.2f}"))
            # Actualizar la base de datos
            cursorinsert.execute("UPDATE Producto SET stock = ?, precio = ? WHERE Cod_Producto = ?",
                                (nueva_cantidad, f"${nuevo_precio:.2f}", values[0]))
            cursorinsert.commit()
        else:
            messagebox.showwarning("Advertencia", "Selecciona un producto antes de aumentar la cantidad")
    def disminuir():
                # Obtener el item seleccionado en el Treeview
        selected_item = tabla.focus()

        if selected_item:
            # Obtener los valores del item seleccionado
            values = tabla.item(selected_item, 'values')
            nuevo_precio = (float(values[3].replace('$', '')) / int(values[2]))
            # Obtener el nuevo valor de la cantidad
            nueva_cantidad = int(values[2]) - 1
            if nueva_cantidad<1:
                messagebox.showwarning("Error", "No puedes llevar 0 productos")
            else:
                # Actualizar el valor de la cantidad en el Treeview
                tabla.item(selected_item, values=(values[0], values[1], nueva_cantidad, values[3]))
                # Obtener el nuevo precio
                nuevo_precio = nuevo_precio*nueva_cantidad
                # Actualizar el precio en el Treeview
                tabla.item(selected_item, values=(values[0], values[1], nueva_cantidad, f"${nuevo_precio:.2f}"))
                
                # Actualizar la base de datos
                cursorinsert.execute("UPDATE Producto SET stock = ?, precio = ? WHERE Cod_Producto = ?",
                                    (nueva_cantidad, f"${nuevo_precio:.2f}", values[0]))
                cursorinsert.commit()
        else:
            messagebox.showwarning("Advertencia", "Selecciona un producto antes de disminuir la cantidad")
    
    def eliminar():
        selected_item = tabla.selection()

        if selected_item:
            tabla.item(selected_item, 'values')
            ID_pr2=int(values[0])
            print(ID_pr2)
            
            try:
                tabla.delete(selected_item)
                print("producto eliminado")
                # Actualizar los identificadores en 'ofertitas' y el contador global
                global id_contador
                id_contador -= 1  # Reducir el contador global en 1
                # Actualizar los identificadores en 'ofertitas'
                # Actualizar los índices de las filas restantes
                for item in tabla.get_children():
                    current_index = int(tabla.index(item))
                    if current_index > ID_pr2:
                        tabla.item(item, text=str(current_index - 1))
            # Ejecutar la instrucción SQL para eliminar el registro
                cursorinsert.execute("DELETE FROM Producto WHERE cod_producto = ?", (ID_pr2))
                # Confirmar la transacción
                cursorinsert.commit()
                print("Registro eliminado con éxito de la BD.")

                
            except:
                # Si ocurre algún error, deshacer la transacción
                cursorinsert.rollback()
                print("Error al eliminar el registro:")

    def cerrar_ver_carrito():
        ofertitas.delete(*ofertitas.get_children())
        for item in tabla.get_children():
            values = tabla.item(item, 'values')
            ofertitas.insert('', 'end', values=values)
            print("sse ha actualizado ambas tablas con los mismos valores")
        ventana_opcion.destroy()
    ventana_opcion = tk.Toplevel(ventana)
    ventana_opcion.title("Carrito")
    ventana_opcion.geometry("890x540")
    ventana_opcion.config(bg="gray")
    ventana_opcion.resizable(False,False)
    ventana_opcion.iconbitmap("logo.ico")

    global Factura
    Factura=tk.LabelFrame(ventana_opcion, width=920, height=450, bd=5, bg="gray")
    Factura.grid(padx=40, row=1, column=1, pady=25, sticky="nsew")
    global tabla
    tabla=ttk.Treeview(Factura, columns=('Id', 'Nombre', 'stok', 'Precio'), show="headings",height=20)
    tabla.heading('Id', text="#")
    tabla.column('Id', width=10)
    tabla.heading('Nombre', text='Instrumento')
    tabla.column('Nombre',width=400)
    tabla.heading('Precio', text='Costo')
    tabla.column('Precio', width=150)
    tabla.heading('stok', text='Cantidad')
    tabla.column('stok', width=100)
    tabla.grid(row=0, column=0, sticky="nsew")
            
    for item in ofertitas.get_children():
        values = ofertitas.item(item, 'values')
        tabla.insert('', 'end',text=0+1,  values=values)
    
    label = tk.Label(ventana_opcion, text="CARRITO DE COMPRAS", bg="gray", font=("norwester", 10))
    label.place(x=325,y=10)
    
    boton_volver = tk.Button(ventana_opcion, text="Regresar", command=cerrar_ver_carrito)
    boton_volver.place(x=15,y=500)

    boton_Agregar=tk.Button(ventana_opcion, text="Agregar cantidad en +1", command=agregar)
    boton_Agregar.place(x=720, y=40)

    boton_dismiuir=tk.Button(ventana_opcion, text="Disminuir cantidad en -1", command= disminuir)
    boton_dismiuir.place(x=720, y=70)

    boton_eliminar=tk.Button(ventana_opcion, text="Eliminar producto sleccionado", command=eliminar)
    boton_eliminar.place(x=720,y=100)

fondo_carrito=tk.PhotoImage(file="carrito.png")
carrito_redimensiondao=fondo_carrito.subsample(15)
boton_comprar=tk.Button(principal, text="   Ver carrito  ", image=carrito_redimensiondao, compound=tk.RIGHT, command=ir_a_comprar, bd=10, highlightthickness=0, padx=2, font=("norwester", 10))
boton_comprar.place(x=650,y=10)
boton_comprar.config(bg="white")
#=================================================================================================================================================================================================
#cursorinsert.close()
ventana.mainloop()
