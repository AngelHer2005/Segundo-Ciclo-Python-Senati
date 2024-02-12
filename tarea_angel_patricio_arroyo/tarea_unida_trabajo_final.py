# Hacer un programa que pida 2 números y sume todos los números que van desde el primero al segundo. Se debe controlar que los valores son correctos.

# Tarea:
# 1. Hacer un programa que haga un menú del tipo "desea salir (S/N" y el programa no termine hasta que el usuario teclee "S".
# 2. Hacer un programa que calcule la suma de los cuadrados de los primeros 100 números. (Propuesto)
# 3. Hacer un programa que calcule la media de números.
# 4. Hacer un programa que calcule la media de X números, se dejarán de solicitar números hasta que se introduzca el 0. (Propuesto)

# Primero cramos las variables.
lista, suma, validor = [], 0, True
print("TAREA".center(100))
#Creo un bucle while con argumento validor = True porque habrán otros bucles dentro que me impedirán usar break, por eso haré uso de banderas.
while validor:
    # Hago uso de excepciones para evitar errores y que no interrumpa la ejecución.
    try:
        while 1:
            # Dividiré las opciones con condicionales y en cada condicional haré la operación necesaria para cada ejercicio. 
            opcion, validor2 = input("""
a) Hacer un programa que pida 2 números y sume todos los números que van desde el primero al segundo. Se debe    
   controlar que los valores son correctos.
b) Hacer un programa que calcule la suma de los cuadrados de los primeros 100 números. (Propuesto)
c) Hacer un programa que calcule la media de números.
d) Hacer un programa que calcule la media de X números, se dejarán de solicitar números hasta que se introduzca el 0. (Propuesto)
Ingresa que ejercicio quieres realizar: """).lower(), True
            if "a" <= opcion <= "d":
                break
            else:print("Coloca una opción válida.")
        # Aprovecharé para colocar 2 operaciones (a y b), ya que son similares.
        if  "a" <= opcion <= "c":
            while validor2:
                    while 1:
                        try:
                            inicio = int(input("\nIngresa un número que será el punto de inicio: "))
                            final = int(input("Ingresa un segundo número que será el punto final: "))
                            if final > inicio:
                                lista = [i for i in range(inicio,final+1)]
                                if opcion.lower() == "a":
                                    print(f"La suma de los números entre {inicio} y {final} es: {sum(lista)}");validor2=False;break
                                else:
                                    print(f"La media de los números entre {inicio} y {final} es: {sum(lista)/len(lista)}");validor2=False;break
                            else:
                                print("Ingresa correctamente los 2 números. El primero debe ser mayor al segundo.")

                        except ValueError:print("No es un número válido. Ingresa de nuevo.")

        elif opcion == "b":
            for i in range(101):
                suma+=i**2
            print(f"La suma de los cuadrados de los primeros 100 números es: {suma}");suma=0
        else:
            print("\nIngresarás los números que desees, si quieres acabar con la iteración, escribe 0.")
            while 1:                
                try:
                    cantidad=int(input("Ingresa un número para calcular la media: "))
                    if cantidad==0:break
                    else: lista.append(cantidad)
                except ValueError: print("No es un número válido. Ingresa de nuevo.")
            resultado = sum(lista)/len(lista)
            print(f"La media de los números introducidos es: {sum(lista)/len(lista)}")
        while 1:
            salida,lista = input("\n¿Desea salir? (S/N) ").lower(), []
            if salida == "s" or salida == "n":
                if salida == "s":
                    validor=False
                    break
                else: break
            else:
                print("Ingresa una respuesta válida, por favor.")           
                
    except ValueError:
        print("No es un número válido. Ingresa de nuevo.")
        
print("PROGRAMA FINALIZADO...".center(50))