# [world_tools.py]

import os


class world_tools:
    def generar_mundo(nombre_archivo):
        matriz = []
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                fila = [str(x) for x in linea.strip().split(',')]
                matriz.append(fila)
        return matriz

    def determinar_posicion(matriz, numero):
        for y, fila in enumerate(matriz):
            for x, elemento in enumerate(fila):
                if elemento == numero:
                    return [y, x]
        return None

    def imprimir_juego(env_objects_dic, ambiente, coordenadas_agente, coordenadas_meta):
        os.system('clear')
        for i, fila in enumerate(ambiente):
            fila_impresa = ""
            for j, elemento in enumerate(fila):
                if [i, j] == coordenadas_agente:
                    fila_impresa += env_objects_dic['caracter_agente'] + "\t"
                elif [i, j] == coordenadas_meta:
                    fila_impresa += env_objects_dic['caracter_meta'] + "\t"
                else:
                    fila_impresa += str(elemento) + "\t"
            print(fila_impresa)
        print()
