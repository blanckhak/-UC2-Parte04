login =open("login.txt","rt")
leerLogin=login.read()

password=open("clave.txt","rt")
leerPassword=password.read()

intentos=0
while intentos<2:
    user = input("Ingrese su usuario: ")
    clave = input("Ingrese la clave: ")
    if user==leerLogin and clave==leerPassword:
        print ("Datos de la Persona")
        print("1. Listar las personas")
        print("2. Agregar las personas")
        print("3. Salir")
        intentos+=2
    else:
        print("El usuario y/o clave es incorrecto")
        intentos+=1