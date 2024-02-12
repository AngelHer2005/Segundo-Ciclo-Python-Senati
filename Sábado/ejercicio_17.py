veces = int(input("¿Cuántos números desea ingresar?"))
cont = 0
acum = 0
for i in range(veces):
    print(f"---ciclo {str(i + 1)} ---")
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        cont += 1
    else:
        acum += num
print(f"La cantidad de números pares es: {cont}\nLa suma total de los números impares es: {acum}")
