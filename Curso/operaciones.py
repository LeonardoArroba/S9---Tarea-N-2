from Menu import Menu
import os

class Operaciones(Menu):

    def __init__(self):
        pass

    def menu_operaciones(self):
        opcion = self.menu(["1) Presentar Mensaje", "2) Variables", "3) Conversiones", "4) Numeros y Operaciones", "5) Concatenaciones", "6) Salir"], "*" * 18 + " MENU OPERACIONES " + "*" * 18)
        os.system("cls")
        if opcion == '1':
            print("*" * 15 + " PRESENTA UN MENSAJE " + "*" * 15)
            print("Hola mundo")

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_operaciones()

        elif opcion == '2':
            print("*" * 20 + " VARIABLES " + "*" * 20)
            nombre = "Leonardo Arroba"
            print(nombre)

            edad = 20
            print(edad)

            edad = True
            print(edad)

            sueldo = 250.50
            print(sueldo)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_operaciones()

        elif opcion == '3':
            print("*" * 19 + " CONVERSIONES " + "*" * 19)
            numero1 = "49"
            numero2 = "186"
            print(numero1 + numero2)

            num1 = int(numero1)
            num2 = int(numero2)
            print(num1 + num2)

            sueldo = 1983.50
            sueldoEntero = int(sueldo)
            print((sueldoEntero))

            valor = "7860.68"
            valorDecimal = float(valor)
            print(valorDecimal * 3)

            edad = 60
            print(len(str(edad)))

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_operaciones()

        elif opcion == '4':
            print("*" * 14 + " NUMEROS Y OPERACIONES " + "*" * 14)
            entero = 48
            decimal = 93.5
            complejo = 35 + 6j
            booleano = True
            print(entero)
            print(decimal)
            print(complejo)
            print(booleano)

            num1 = 25
            num2 = 6
            print("Suma:", num1 + num2)
            print("Resta:", num1 - num2)
            print("Multiplicacion:", num1 * num2)
            print("Division:", num1 / num2)
            print("Divicion Exacta:", num1 // num2)
            print("Potencia:", num1 ** num2)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_operaciones()

        elif opcion == '5':
            print("*" * 18 + " CONCATENACION " + "*" * 18)
            texto1 = "Hola"
            texto2 = "Mundo"
            textoFinal = texto1 + " " + texto2
            print(textoFinal)
            print("El saludo es: %s %s" % (texto1,texto2))
            saludoFinal = "Saludo: {} {}".format(texto1,texto2)
            print(saludoFinal)
            saludoFinal2 = "Saludo: {x} {y}".format(x=texto1,y=texto2)
            print(saludoFinal2)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_operaciones()

        elif opcion == '6':
            pass

