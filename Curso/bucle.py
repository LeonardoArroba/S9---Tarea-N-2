from Menu import Menu
import os

class Bucles(Menu):

    def __init__(self):
        pass

    def menu_bucles(self):
        opcion = self.menu(["1) Range", "2) Bucle For", "3) Factorial", "4) Bucle While", "5) Sentencias Break - Continue - Pass", "6) Salir"], "*" * 18 + " MENU BUCLE " + "*" * 18)
        os.system('cls')
        if opcion == '1':
            print("*" * 17 + " RANGE " + "*" * 17)
            # range(): Crea una lista inmutable de numeros enteros en sucesion aritmetica.
            numeros = range(5)  # [0, 1, 2, 3, 4]
            print(numeros[1])
            numeros1 = range(4, 10) #[4, 5, 6, 7, 8, 9]
            print(numeros1[2])
            numeros2 = range(10, 100, 8) #[10, 18, 26, 34, 42]
            print(numeros2[4])

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_bucles()

        elif opcion == '2':
            print("*" * 17 + " BUCLE FOR " + "*" * 17)
            # Bucles: Son estructuras de control de flujo que repiten 1 o varias lineas de codigo.
            for num in range(0, 20, 2):
                print("Valor actual: {}".format(num))
            print("")
            for i in range(1,13):
                print("{} x {} = {}".format(i, i, (i * i)))
            print("")
            for nom in ["Maria", "Ernesto", "Pablo", "Steven"]:
                print("Cantidad de letras de {} es: {}".format(nom, len(nom)))

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_bucles()

        elif opcion == '3':
            print("*" * 17 + " FACTORIAL " + "*" * 17)
            # Factorial: Es el producto de todos los numeros positivos enteros compredidos entre 1 y un determinado numero.
            # Factorial de 5 = 1 * 2 * 3 * 4 * 5 = 120
            # Factorial de 4 = 1 * 2 * 3 * 4 = 24

            numero  = int(input("Ingrese un numero: "))
            factorial = 1

            for n in range(1, (numero+1)):
                factorial *= n
            print("El factorial de {} es: {}".format(numero, factorial))

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_bucles()

        elif opcion == '4':
            print("*" * 17 + " BUCLE WHILE " + "*" * 17)
            # While: Esctrutura repetitiva que nos permite realizar multiples iteracion
            # basandonos en el resultado de una explresion logica que puede
            # tener como resultado un valor True o False.

            indice = 1
            while indice < 10:
                print("Valor actual: {}".format(indice))
                indice += 1
            print("Hemos terminado el bucle while\n")
            # Continue el programa

            indice = 2
            while indice <= 100:
                print("Numero par: {}".format(indice))
                indice += 2
            print("Hemos terminado el bucle while")

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_bucles()

        elif opcion == '5':
            print("*" * 17 + " SENTENCIAS BREAK - CONTINUE - PASS " + "*" * 17)
            print("BREAK")
            # Break: Permite salir de un bucle cuando se cumple una condicion.
            for numero in range(1, 6):
                if numero == 3:
                    break
                print("El numero es: {}".format(numero))
            print("Bucle terminado")

            print("\nCONTINUE")
            # Continue: Omite una parte del bucle cuando se cumple una condicion y continua con el resto.
            for numero in range(1, 6):
                if numero == 3:
                    continue
                print("El numero es: {}".format(numero))
            print("Bucle terminado")

            print("\nPASS")
            # Pass: Permite continuar con una sentencia o funcion que ya no tiene o aun no tiene un bloque de codigo util.
            for numero in range(1, 6):
                if numero <= 3:
                    pass
                else:
                    print("El siguiente valor es mayor a 3:")
                print("El numero es: {}".format(numero))
            print("Bucle terminado")

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_bucles()

        elif opcion == '6':
            pass




