from Menu import Menu
from operaciones import Operaciones
from secuencias import Secuencias
from sentencias import Sentencias
from bucle import Bucles
from generadores import Generadores
from excepciones import Excepciones
from modulos import Modulo
from pruebaPaquete import Paquete
from POO import POO
import os

class Main(Menu):

    def __init__(self):
        pass

    def menu_main(self):
        opcion = self.menu(["1) Operaciones", "2) Secuencias", "3) Sentencias", "4) Bucles", "5) Generadores", "6) Excepciones", "7) Modulos", "8) Paquetes", "9) POO", "10) Salir"], "*" * 18 + " MENU PRINCIPAL " + "*" * 18)
        os.system("cls")
        if opcion == '1':
            operaciones = Operaciones()
            if operaciones.menu_operaciones() != '6':
                os.system("cls"), self.menu_main()

        elif opcion == '2':
            secuencia = Secuencias()
            if secuencia.menu_secuencias() != '5':
                os.system("cls"), self.menu_main()

        elif opcion == '3':
            sentencia = Sentencias()
            if sentencia.menu_sentencias() != '7':
                os.system("cls"), self.menu_main()

        elif opcion == '4':
            bucle = Bucles()
            if bucle.menu_bucles() != '6':
                os.system("cls"), self.menu_main()

        elif opcion == '5':
            generador = Generadores()
            if generador.menu_generadores() != '3':
                os.system("cls"), self.menu_main()

        elif opcion == '6':
            excepcion = Excepciones()
            if excepcion.menu_excepciones() != '3':
                os.system("cls"), self.menu_main()

        elif opcion == '7':
            mod = Modulo()
            if mod.menu_modulo() != '2':
                os.system("cls"), self.menu_main()

        elif opcion == '8':
            paquete = Paquete()
            if paquete.menu_paquete() != '5':
                os.system("cls"), self.menu_main()

        elif opcion == '9':
            poo = POO()
            if poo.menu_poo() != '8':
                os.system("cls"), self.menu_main()

        elif opcion == '10':
            print("*" * 15 + " FINALIZACION DEL PROGRAMA " + "*" * 15)

opc = Main()
opc.menu_main()
