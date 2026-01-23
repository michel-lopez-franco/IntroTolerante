import suma
import resta

import div

print("hola mundo")
print("¡Bienvenido a Python!")


print("La resta de 5 y 3 es:", resta.resta(5, 3))
print("La suma de 5 y 3 es:", suma.suma(5, 3))


print(suma(5, 3))
print(resta(10, 4))
print("Operaciones completadas.")
print("División:", div.div(10, 2))
print("Programa finalizado.")


def potencia(base, exponente):
    return base**exponente


print("La potencia de 2 elevado a 3 es:", potencia(2, 3))
