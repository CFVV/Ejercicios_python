
def MaxProfit(precios_stock):
    """ La función retorna un valor que corresponde al mayor beneficio (profit) posible según el proceso de compra "buy once, sell once".
        input: "precios_stock" ingresar array [] con precios a evaluar. Ejemplo de input [44, 30, 22, 32, 35, 30, 41, 38, 15]
        output: un valor el que corresponde al máximo profit para el input ingresado.
    """
#transformación del input: de lista con string a lista con int
    string = precios_stock
    string_2 = string.replace("[", "")
    string_3 = string_2.replace("]", "")
    string_4 = string_3.split(',')

    lista_int = []
    # Se transforman elementos string a int
    for i in string_4:
        a = int(i)
        lista_int.append(a)

    lista_int

# función de cálculo de profit máximo
    cant_precios = len(lista_int)
    valor_costo = 0 #variable auxiliar se inicializa en 0
    profit_maximo = 0 
    
    if (cant_precios == 0):
        print("No se ha ingresado ninguna lista de precios, intente nuevamente.")
        return 0
    
    valor_minimo = lista_int[0] #la variable "primer_valor" toma el primer valor de la lista de input
    
    for precio in range(cant_precios):
        valor_minimo = min(valor_minimo, lista_int[precio])
        valor_costo = (lista_int[precio] - valor_minimo)
        profit_maximo = max(profit_maximo,valor_costo)
    
    if profit_maximo <= 0: #si no hay profit, retorna -1
        print(-1)
    else:
        return print(profit_maximo) #retorna el profit máximo

texto = input("Ingrese una lista de precios: ")
MaxProfit(texto)
