# Hacer un programa que pida 2 números y sume todos los números que van desde el primero al segundo. Se debe controlar que los valores son correctos.
print("Este programa te mostrará la suma entre todos los números dentro de un rango de 2 números que tú darás, incluyendo estos.")
while 1:
    try:
        n1 = int(input("Ingresa el primer número: "))
        n2 = int(input("Ingresa el segundo número: "))  
        if n2 > n1: 
            # Primera opción:
            suma = 0
            for i in range(n1, n2+1):
                suma += i
            print(suma)
            # Segunda opción:
            suma2 = sum([i for i in range(n1, n2+1)])
            print(suma2)
            break
        else:
            print("El segundo número debe ser mayor que el primero.")
    except ValueError:
        print("Ingresa solo números.")