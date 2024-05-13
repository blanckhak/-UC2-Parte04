login =open("login.txt","rt")
leerLogin=login.read()

password=open("clave.txt","rt")
leerPassword=password.read()

def menu():
    print("Datos Persona")
    print("1. Listar personas")
    print("2. Agregar Personas")
    print("3. Salir")


def agregar_personas():
    print("-- Agregando DNI al Archivo --")
    dni = "dni.txt"
    dnicontenido = input("Dni: ")
    archivo = open(dni,"at")
    archivo.write("\n" + dnicontenido )
    archivo.close()
    
    
    print("-- Agregando NOMBRE al Archivo --")
    nombre = "nombre.txt"
    nombrecontenido = input("Nombre: ")
    archivo = open(nombre,"at")
    archivo.write("\n" + nombrecontenido)
    archivo.close()
    
    
    print("-- Agregando APELLIDO al Archivo --")
    apellido = "apellido.txt"
    apellidocontenido = input("Apellido: ")
    archivo = open(apellido,"at")
    archivo.write("\n" + apellidocontenido )
    archivo.close()


def listar_personas():
    with open("dni.txt", "r") as dnis, open("nombre.txt", "r") as nombres, open("apellido.txt", "r") as apellidos:
        for dni, nombre, apellido in zip(dnis, nombres, apellidos):
            print(f"DNI: {dni.strip()} - Nombre: {nombre.strip()} - Apellido: {apellido.strip()}")


def salir():
    print("Gracias, vuelva pronto")

def error():
    print("Opción incorrecta")

intentos=0
while intentos<2:
    user = input("Ingrese su usuario: ")
    clave = input("Ingrese la clave: ")
    if user==leerLogin and clave==leerPassword:
       menu()
       opcion = 1
       while opcion!=3:
            opcion = int(input("opcion: "))
            if opcion == 1:
                listar_personas()
                menu()
            elif opcion == 2:
                agregar_personas()
                menu()
            elif opcion == 3:
                salir()
            else:
                error()
                menu()
                
       intentos+=2
    else:
        print("El usuario y/o clave es incorrecto")
        intentos+=1
        