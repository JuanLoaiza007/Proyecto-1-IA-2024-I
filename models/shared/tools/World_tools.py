# [World_tools.py]

import json


class World_tools:
    def reconocer_objetos():
        try:
            with open("./data/characters.json", 'r') as archivo_json:
                return json.load(archivo_json)
        except json.JSONDecodeError:
            print(
                "Error: El archivo characters.json no se puede convertir a un diccionario.")
            return {}

    def reconocer_assets():
        try:
            with open("./data/assets.json", 'r') as archivo_json:
                return json.load(archivo_json)
        except json.JSONDecodeError:
            print(
                "Error: El archivo characters.json no se puede convertir a un diccionario.")
            return {}

    def generar_mundo(ruta_archivo):
        matriz = []

        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                fila = [str(x) for x in linea.strip().split(' ')]
                matriz.append(fila)

        return matriz

    def determinar_posicion(matriz, numero):
        for y, fila in enumerate(matriz):
            for x, elemento in enumerate(fila):
                if elemento == numero:
                    return [y, x]
        return None

    def imprimir_juego(env_objects_dic, ambiente, coordenadas_agente, coordenadas_meta):
        print("world_tools.py in (func)imprimir_juego: coordenadas_agente: {} coordenadas_meta: {}".format(
            str(coordenadas_agente), str(coordenadas_meta)))

        for i, fila in enumerate(ambiente):
            fila_impresa = ""
            for j, elemento in enumerate(fila):
                if [i, j] == coordenadas_agente:
                    # fila_impresa += env_objects_dic['caracter_agente'] + "\t"
                    fila_impresa += "2" + "\t"
                elif [i, j] == coordenadas_meta:
                    # fila_impresa += env_objects_dic['caracter_meta'] + "\t"
                    fila_impresa += "5" + "\t"
                else:
                    fila_impresa += str(elemento) + "\t"
            print(fila_impresa)
        print()

    def comprobar_mundo(archivo):
        mundo = World_tools.generar_mundo(archivo)
        objetos = World_tools.reconocer_objetos()

        agente = World_tools.determinar_posicion(
            mundo, objetos['agente'])
        meta = World_tools.determinar_posicion(
            mundo, objetos['meta'])

        elemento_fuera_de_rango = False
        try:
            for fila in mundo:
                for elemento in fila:
                    if not (0 <= int(elemento) <= 5):
                        elemento_fuera_de_rango = True
                        break
                if elemento_fuera_de_rango:
                    break
        except ValueError:
            elemento_fuera_de_rango = True

        errores = []
        if agente == None:
            errores.append("Falta un agente (Numero {})".format(
                str(objetos['agente'])))
        if meta == None:
            errores.append("Falta una meta (Numero {})".format(
                str(objetos['meta'])))
        if elemento_fuera_de_rango:
            errores.append(
                "El archivo debe usar solo numeros del 0 al 5")

        return errores
