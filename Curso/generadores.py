from Menu import Menu
import os

class Generadores(Menu):

    def __init__(self):
        pass

    def menu_generadores(self):
        opcion = self.menu(["1) Generador", "2) Generador Nº 2", "3) Salir"], "*" * 18 + " MENU GENERADORES " + "*" * 18)
        os.system("cls")
        if opcion == '1':
            print("*" * 15 + " GENERADOR " + "*" * 15)
            def generaMultiplos7(limite):
                numero = 1
                listaNumeros = []

                while numero <= limite:
                    listaNumeros.append(numero * 7)
                    numero = numero + 1
                return listaNumeros  # Retorna toda la lista creada.

            print(generaMultiplos7(10))

            def generadorMultiplos7(limite):
                numero = 1

                while numero <= limite:
                    yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
                    numero = numero + 1

            obtieneMultiplos7 = generadorMultiplos7(10)

            """
            # print(obtieneMultiplos7)
            for n in obtieneMultiplos7:
                print(n)
            """

            # next(): Retorna el siguiente elemento de un objeto iterable:

            print(next(obtieneMultiplos7))
            print("Acá hay 300 líneas de código...")
            print(next(obtieneMultiplos7))
            print("Acá hay 1000 líneas de código...")
            print(next(obtieneMultiplos7))

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_generadores()

        elif opcion == '2':
            print("*" * 15 + " GENERADOR Nº 2 " + "*" * 15)
            # def devuelveLenguajes(*lenguajes):
            #     for leng in lenguajes:
            #         yield leng
            def devuelveLenguajes(*lenguajes):
                for leng in lenguajes:
                    yield from leng
            lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
            print(next(lenguajesObtenidos))
            print(next(lenguajesObtenidos))

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_generadores()

        elif opcion == '3':
            pass





