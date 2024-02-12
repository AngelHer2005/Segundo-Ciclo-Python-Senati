# 1. Hacer un programa que haga un menú del tipo "desea salir (S/N)" y el programa no termine hasta que el usuario teclee "S".

while 1:
    salida = input("¿Desea salir? (S/N)")
    if salida.lower() == "s":
        break