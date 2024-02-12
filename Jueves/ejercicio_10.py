def tabla_multiplicar(n):
    for i in range(1,11):
        print(n, '*', i, '=', i*n)
tabla_multiplicar(4)

def suma(a,b):
    return a + b
result = suma(40,26)
print("El resultado es", result)

def suma(a,b = 80):
    return a + b
result=suma(1)
print("El resultado es", result)