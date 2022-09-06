from Menu import Menu
import os

class Sentencias(Menu):

    def __init__(self):
        pass

    def menu_sentencias(self):
        opcion = self.menu(["1) Ingreso de Datos", "2) If - Elif - Else", "3) Funciones", "4) Operadores Logicos", "5) Operador Ternario", "6) If - In", "7) Salir"], "*" * 18 + " MENU SENTENCIAS " + "*" * 18)
        os.system("cls")
        if opcion == '1':
            print("*" * 17 + " INGRESO DE DATOS " + "*" * 17)
            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            sueldo = float(input("Ingrese su sueldo: "))
            print("Hola, " + nombre)
            edadFutura = edad + 20
            print("Tu edad es: ", edad)
            print("Tu edad (dentro de 20 años) sera: {}".format(edadFutura))
            print("Tu sueldo es: ", sueldo)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_sentencias()

        elif opcion == '2':
            print("*" * 16 + " IF - ELIF - ELSE " + "*" * 16)
            print("¿Determinar si la persona es mayor de edad?")

            edad = int(input("Ingrese su edad: "))

            if edad > 18:
                print("Eres mayor de edad.")
            elif edad == 18:
                print("Tienes 18 años")
            else:
                print("No eres mayor de edad.")

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_sentencias()

        elif opcion == '3':
            print("*" * 21 + " FUNCIONES " + "*" * 21)
            def saludar():
                print("Leonardo")
                print("Arroba")
                print("Zancorw")
                return "Hola"
            print(saludar())

            def evalurSueldoMinimo(sueldo):
                if sueldo >= 425:
                    print("Cumples con el sueldo")
                else:
                    print("Ganas menos que el sueldo minimo")
            evalurSueldoMinimo(200)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_sentencias()

        elif opcion == '4':
            print("*" * 18 + " OPERADOR LOGICO " + "*" * 17)
            distancia = 400
            nomeroHermanos = 3
            sueldoPadres = 3000
            tieneBeneficio = False

            if (distancia > 1000 and nomeroHermanos > 2) or sueldoPadres < 2000:
                tieneBeneficio = True
            print(not tieneBeneficio)

            if (7 > 4) and (6 < 12):
                print("Verdad")
            else:
                print("Es mentira...")

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_sentencias()

        elif opcion == '5':
            print("*" * 17 + " OPERADOR TERNARIO " + "*" * 17)
            """
            String sexo;
            sexo = (10 > 20) ? "Masculino" : "Femenino"
            """
            sexos = ("Hombre", "Mujer")
            posicion = True

            sexo = sexos[posicion] #Mujer
            print(sexo)

            sexo = sexos[not posicion] #Hombre
            print(sexo)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_sentencias()

        elif opcion == '6':
            print("*" * 22 + " IF - IN " + "*" * 22)
            print("-- Cursos --")
            print("Matematicas - Biologia - Lenguaje- Ciencias")
            curso = input("Ingrese el curso deseado: ")
            if curso in ("Matematicas", "Biologia", "Lenguaje", "Ciencias"):
                print("Curso {} seleccionado".format(curso))
            else:
                print("No existe curso...")

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_sentencias()

        elif opcion == '7':
            pass




