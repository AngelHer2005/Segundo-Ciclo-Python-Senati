class Humano:
    def __init__(self,edad):
        self.edad = edad
    def hablar(self,mensaje):
        print(mensaje)
pedro = Humano(20)
raul = Humano(21)
print(f"Soy Pedro y tengo {pedro.edad} años.\nSoy Raúl y tengo {raul.edad} años.")
pedro.hablar("Hola")
raul.hablar("Hola, Pedro")