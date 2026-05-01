import string
import random
# primero el usuario genera la contraseña de x caracteres
longitud = int(input("ingrese el tamaño de la contraseña: "))
#utilizando las librerias de numeros, digitos y caracteres
caracteres = string.ascii_letters + string.digits + string.punctuation
#concatenamos todo las veces que se haya especificado en longitud
contraseña = "".join(random.choice(caracteres)for i in range(longitud))

print("La contraseña segura es: " + contraseña)