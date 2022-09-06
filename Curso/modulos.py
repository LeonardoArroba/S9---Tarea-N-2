"""
Módulo:
Es un archivo con extensión .py o .pyc (Python compilado), que posee su propio espacio de nombres
y que puede contener variables, funciones, clases o incluso otros módulos.

¿Para qué sirven?
Para organizar mejor el código y poder reutilizarlo mejor.
Modularización y reutilización.
"""

# import funciones_matematicas

from Menu import Menu
from funciones_matematicas import Funciones
import os

class Modulo(Menu):

    def __init__(self):
        pass

    def menu_modulo(self):
        opcion = self.menu(["1) Modulos", "2) Salir"], "*" * 18 + " MENU MODULO " + "*" * 18)
        os.system("cls")
        if opcion == '1':
            print("*" * 15 + " MODULO " + "*" * 15)
            print("Suma")
            print(Funciones.sumar(5, 6))
            print("\nMultiplicacion")
            print(Funciones.multiplicar(5, 6))

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_modulo()

        elif opcion == '2':
            pass

