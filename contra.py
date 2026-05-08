import string
import secrets 
def generar_password():
    #utilizando las librerias de numeros, digitos y caracteres
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while true:
        try:
            #Intentamos convertir la entrada a un numero entero
            longitud = int(input("Ingrese el tamaño de la contraseña: "))
            #Validacion logica
            if longitud <= 0:
                print("Por favor, ingresa un numero mayor a 0.")
                continue
            if longitud > 128:
                print("Es muy largo! Por seguridad, intenta algo menor a 128.")
                continue
            #si esta bien se rompe el bucle
            break
        except ValueError:
            #Por si el usuario ingresa texto en vez de numeros
            print("Entrada no valida. Por favor, ingresa solo numeros enteros.")
    #Generamos la contraseña
    contraseña = "".join(secrets.choice(caracteres) for i in range(longitud))
    print("\n---")
    print(f"La contraseña segura es: {contraseña}")
    print("----\n")
  
if __name__ == "__main__":
    generar_password()
