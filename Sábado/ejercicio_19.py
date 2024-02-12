#creando una clase
class Notas:
    def __init__(self):
        self.alumno,self.nota=[],[]
    def menu(self):
        opcion,bienvenido=0,"BIENVENIDO AL SISTEMA"
        #Hacer mientras la opción sea diferente a 4
        while opcion!=4:
            print(f"""
            {"="*49}
            |{bienvenido:°^47}|
            {"="*49}
            
            [1] Ingreso de Notas...
            [2] Listar Notas...
            [3] Listado de Notas Aprobados...
            [4] Finalizar el Sistema...""")

            #Hacer mientras sea verdadero
            while True:
                try:
                    opcion=int(input("Ingrese una opción: "))
                    break
                except:
                    print("Vuelva a ingresar la opción...!!!\n")
            if opcion==1:
                self.ingreso_notas()
            elif opcion==2:
                print("\nCARGAR NOTAS...!!!\n")
                self.listar_notas()
            elif opcion==3:
                print("\nCARGAR NOTAS...!!!\n")
                self.lista_notas_aprobadas()
        else:print("\nFINALIZANDO EL PROGRAMA...!!!".center(75))
    def ingreso_notas(self):
        try:
            numeros=int(input("¿Cuántos registros desea añadir?\n"))
        except ValueError:
            print("\nLA OPCIÓN INGRESADA NO ES UN NÚMERO...")
        else:
            for x in range(numeros):
                xalumno=input("Ingrese el Nombre y el Apellido del alumno: ").upper()
                self.alumno.append(xalumno)
                try:
                    xnota=int(input("Ingrese la nota:"))
                except ValueError:
                    return True
                else:
                    self.nota.append(xnota)
            print("\nNota agregada correctamente...!!!\n")
            input("Presione ENTER para continuar...!!!\n")
    def listar_notas(self):
        ndatos=len(self.alumno)
        if len(self.alumno)==0 and len(self.nota)==0:
            print("\nNo existen datos aún...!!!\n")
        else:
            for x in range(ndatos):
                print(self.alumno[x],":",self.nota[x])
        input("Presione ENTER para continuar...!!!\n")
    
    def lista_notas_aprobadas(self):
        ndatos=len(self.alumno)
        for x in range(ndatos):
            if self.nota[x]>=13:
                print(f"{self.alumno[x]} : {self.nota[x]} Aprobado")
            else:
                print(f"{self.alumno[x]} : {self.nota[x]} Desaprobado")
        input("Presione ENTER para continuar...!!!\n")
Nota1=Notas()
Nota1.menu()