# Self es una convención que se utiliza como nombre para el primer parámetro de un método en una clase. El 
# objetivo de self es hacer referencia al objeto que se está manipulando cuando se llama al método.

# - Crear la clase vehículo con las clases frenar, acelerar y girar.
# - Crear la clase calculadora con las funciones sumar, restar, multiplicar y dividir.
# - Crear la clase computadora con las funciones ver Series, jugar, estudiar, apagar y prender.

# 1)
class Vehiculo:
    def frenar(self):
        print("El vehículo está frenando.")
    def acelerar(self):
        print("El vehículo está acelerando.")
    def girar(self):
        print("El vehículo está girando.")
vehiculo = Vehiculo()
vehiculo.frenar(); vehiculo.acelerar(); vehiculo.girar()

# 2)
class Calculadora:
    def sumar(self,num1,num2):
        print(num1+num2)
    def restar(self,num1,num2):
        print(num1-num2)
    def multiplicar(self,num1,num2):
        print(num1*num2)
    def dividir(self,num1,num2):
        print(num1/num2)
calculadora=Calculadora()
calculadora.sumar(3,2)
calculadora.restar(4,2)
calculadora.multiplicar(5,2)
calculadora.dividir(6,2)

# 3)
class Computadora:
    print("Enciende la computadora, por favor.")
    def estado(self,status):
        self.status = status
        if self.status:
            print("Se está encendiendo la computadora...")
        else:print("Se está apagando la computadora...")

    def ver_series(self):
        if self.status:
            print("Se está viendo series...")
        else:
            print("La computadora está apagada. No se puede ver series, enciéndela.")
 
    def jugar(self):
        if self.status:
            print("Se está jugando...")
        else:
            print("La computadora está apagada. No se puede jugar, enciéndela.")

    def estudiar(self):
        if self.status:
            print("Se está estudiando...")
        else:
            print("La computadora está apagada. No se puede estudiar, enciéndela.")

computadora=Computadora()
computadora.estado(True)
computadora.ver_series()
computadora.jugar()
computadora.estudiar()
computadora.estado(False)
