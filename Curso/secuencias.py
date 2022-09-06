from Menu import Menu
import os

class Secuencias(Menu):

    def __init__(self):
        pass

    def menu_secuencias(self):
        opcion = self.menu(["1) Cadenas", "2) Tuplas", "3) Listas", "4) Diccionarios", "5)Salir"], "*" * 18 + " MENU SECUENCIAS " + "*" * 18)
        os.system("cls")
        if opcion == '1':
            print("*" * 21 + " CADENAS " + "*" * 21)
            texto = "Bienvenidos a Himalaya!!, ¿Helado?"
            print(texto)
            print(texto.lower())
            print(texto.upper())
            print(texto.title())
            print(texto.find("a"))
            print(texto.count("e"))
            textoFinal = texto.replace("e", "3")
            print(textoFinal)
            valor = texto.isnumeric()
            print(valor)
            cadenaSeparada = texto.split(" ")
            print(cadenaSeparada)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_secuencias()

        elif opcion == '2':
            print("*" * 21 + " TUPLAS " + "*" * 21)
            tupla = (1, 2, 3)
            print(tupla)

            tupla2 = (7, "Andres", True, 689.25, 25 + 4j, 20, "Felicidad", False)
            print(tupla2)

            tupla3 = (6, 4, (8, 2, 7))
            print(tupla3)
            print(tupla2[1])
            # tupla2[1] = "Leonardo"
            #print(tupla2)
            print(tupla2[0:4])
            print(tupla2[-2])

            a, b, c = tupla
            print(a)
            print(b)
            print(c)

            tutplaFinal = tupla + tupla3
            print(tutplaFinal)
            print(tutplaFinal.count(21))
            print(tutplaFinal.index(2))

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_secuencias()

        elif opcion == '3':
            print("*" * 22 + " LISTAS " + "*" * 22)
            lista1 = ["Juan", 36, 72.35, True, "Alfredo", 94.18]
            print(lista1)
            print(lista1[:])
            print(lista1[3])
            print(lista1[-1])
            print(lista1[0:3])
            print(lista1[:2])
            print(lista1[3:])
            lista1.append("Leonardo")
            print(lista1)
            lista1.insert(3, "Ronal")
            print(lista1)
            lista1.extend(["Jose", 258, False])
            print(lista1)
            print(lista1.index("Leonardo"))
            lista1.remove(94.18)
            print(lista1)
            lista1.pop()
            print(lista1)

            lista2 = ["Anthony", "Javier"]
            lista3 = lista1 + lista2
            print(lista3)
            print(lista2 * 4)
            print("Leonado16" in lista1)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_secuencias()

        elif opcion == '4':
            print("*" * 21 + " DICCIONARIOS " + "*" * 21)
            miDiccionario = {"Ecuador":"Quito", "España":"Andorra", "Peru":"Lima", "Estados Unidos":"Chicago"}
            print(miDiccionario["Peru"])
            print(miDiccionario)

            miDiccionario["Venezuela"] = "Caracas"
            print(miDiccionario)

            miDiccionario["Ecuador"] = "Guayaquil"
            print(miDiccionario)

            del miDiccionario["Ecuador"]
            print(miDiccionario)

            dic2 = {"Arroba":"Leonardo", 20:True, "Carrera":"Ingenieria en Software"}
            print(dic2[20])

            llaves = ("España","Francia","Inglaterra")
            dic3 = {llaves[0]:"Madrid", llaves[1]:"Paris", llaves[2]:"Londres"}
            print(dic3)

            datosPersonales = {"Ape":"Arroba", "Anios":{1:2019, 2:2020, 3:2021, 4:2022}}
            print(datosPersonales)
            print(datosPersonales["Anios"])
            print(datosPersonales.keys())

            valores = tuple(datosPersonales.values())
            print(valores)

            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_secuencias()

        elif opcion == '5':
            pass




