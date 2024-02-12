# 4. Hacer un programa que calcule la media de X números, se dejarán de solicitar números hasta que se introduzca el 0. (Propuesto)
lista = []
print("\nIngresarás los números que desees, si quieres acabar con la iteración, escribe 0.")

while 1:                
    try:
        cantidad = int(input("Ingresa un número para calcular la media: "))
        if cantidad == 0: break
        else: lista.append(cantidad)
    except ValueError: print("No es un número válido. Ingresa de nuevo.")
    
resultado = sum(lista)/len(lista)
print(f"La media de los números introducidos es: {sum(lista)/len(lista)}")