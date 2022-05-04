
def val_int(capital: float, t: int):
    intereses = (capital * 0.03 * t) / 12
    
    return intereses

def val_per(capital: float):
    perder = capital * 0.02

    return perder

def CDT(usuario: str, capital: float, t: int):

    if t >= 3:
        v_total = capital + val_int(capital, t)
        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario, capital, t, v_total)
    
    else:
        v_total = capital - val_per(capital)
        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario, capital, t, v_total)

#SCRIPT PARA HACER PRUEBAS

#usuario = input("Digite su usuario: ")
#capital = float(input("Digite el monto de su capital inicial: "))
#t = int(input("Digite el tiempo en meses que lleva su CDT: "))

#CDT(usuario, capital, t)
