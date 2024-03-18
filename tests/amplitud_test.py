# [test.py]

import time
from models.agente import agente
from models.tools.world_tools import world_tools
from models.nodo import Nodo

# Mapa
nombre_mundo = "world.txt"
juego_activo = True

env_objects_dic = world_tools.reconocer_objetos()
ambiente = world_tools.generar_mundo(nombre_mundo)

# Agente
rata = agente()
rata.set_coordenadas(world_tools.determinar_posicion(
    ambiente, env_objects_dic['caracter_agente']))
rata.set_ambiente(ambiente, env_objects_dic)
rata.set_meta(world_tools.determinar_posicion(
    ambiente, env_objects_dic['caracter_meta']))

# El ambiente es estático, lo unico que se mueve es el agente
ambiente[rata.coordenadas[0]][rata.coordenadas[1]] = 0

# Representaión de un estado
estado_inicial = (rata, ambiente, None)
estado_actual = estado_inicial

# El problema es un nodo del arbol
problema = Nodo()
problema.set_estado(estado_inicial)
problema.set_padre(None)
problema.set_operador(None)
problema.set_profundidad(0)
problema.set_costo_acumulado(0)


# while juego_activo:

#     juego_activo = not (rata.meta_alcanzada())

#     world_tools.imprimir_juego(
#         env_objects_dic, ambiente, rata.get_coordenadas(), rata.get_meta())
#     time.sleep(1.3)
