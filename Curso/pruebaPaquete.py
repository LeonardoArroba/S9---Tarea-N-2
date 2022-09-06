from funcionCadena import contar_letras
from funcionNumerica import *
from Menu import Menu
import os

class Paquete(Menu):

    def __init__(self):
        pass

    def menu_paquete(self):
        opcion = self.menu(["1) Paquete",  "2) Salir"], "*" * 18 + " MENU PAQUETE " + "*" * 18)
        os.system("cls")
        if opcion == '1':
            print("*" * 15 + " PAQUETE " + "*" * 15)
            print("Multiplicacion")
            print(multiplicar(5, 6))
            print("\nLa longitud de la palabra es:")
            print(contar_letras("UskoKruM2010"))

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_paquete()

