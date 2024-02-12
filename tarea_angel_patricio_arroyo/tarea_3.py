# 3. Hacer un programa que calcule la media de números.

print("Este programa te mostrará la media entre todos los números dentro de un rango de 2 números que tú darás, incluyendo estos.")
while 1:
    try:
        n1 = int(input("Ingresa el primer número: "))
        n2 = int(input("Ingresa el segundo número: "))  
        if n2 > n1: 
            media = [i for i in range(n1,n2+1)]
            print(sum(media)/len(media))
            break
        else:
            print("El segundo número debe ser mayor que el primero.")
    except ValueError:
        print("Ingresa solo números.")