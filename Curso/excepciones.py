from Menu import Menu
import os

class Excepciones(Menu):

    def __init__(self):
        pass

    def menu_excepciones(self):
        opcion = self.menu(["1) Bloque Try - Except:", "2) Raize", "3) Salir"], "*" * 18 + " MENU EXCEPCIONES " + "*" * 18)
        os.system("cls")
        if opcion == '1':
            print("*" * 15 + " BLOQUE TRY - EXCEPT " + "*" * 15)
            print("Hola mundo")
            # Excepción: Error en tiempo de ejecución (durante la ejecución de un programa).
            numero1 = 20
            numero2 = 2
            print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))
            try:
                resultado = numero1 / numero2
            # except:
            except ZeroDivisionError:
                print("No se puede dividir entre 0...")
            finally:
                print("Yo siempre aparezco.")
            print("Aquí termina mi programa.")

            def evaluarNota(nota):
                if nota < 0:
                    raise ValueError("Valor incorrecto...")
                    # raise ZeroDivisionError("Este mensaje es personalizado.")
                elif nota >= 16:
                    print("Excelente")
                elif nota >= 11:
                    print("Aprobado")
                else:
                    print("Desaprobado")
            evaluarNota(11)
            print("Este es el fin de mi programa.")

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_excepciones()

        elif opcion == '2':
            print("*" * 15 + " RAIZE " + "*" * 15)
            # Raise: Sirve para lanzar (de forma intencional) excepciones en Python.
            def evaluarNota(nota):

                if nota < 0:
                    raise ValueError("Valor incorrecto...")
                    # raise ZeroDivisionError("Este mensaje es personalizado.")
                elif nota >= 16:
                    print("Excelente")
                elif nota >= 11:
                    print("Aprobado")
                else:
                    print("Desaprobado")
            evaluarNota(12)
            # evaluarNota(-7)
            print("Este es el fin de mi programa.")

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_excepciones()

        elif opcion == '3':
            pass








