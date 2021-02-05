##### Detect floating point number #####
# El programa devuelve True si el input con formato string cumple con las condiciones para ser un float.
## ^[-\+]? indica que el input debe comenzar con un signo - , + o ninguno (cualquier otro signo o símbolo arrojará error)
## [0-9]* indica que el input puede continuar con cualquier dígito entre 0 y 9
## \. indica que el input debe contener un . 
## [0-9]+$ indica que el input debe terminar con al menos un dígito entre 0 y 9

import re

texto = input("Ingrese un string: ")
output= bool(re.search(r"^[-\+]?[0-9]*\.[0-9]+$",texto))
            
if output == True:
    float(texto) # Si el input ingresado es True, se convierte a float.
else:
    print("El input ingresado no se ha detectado como float")
print(output) 




