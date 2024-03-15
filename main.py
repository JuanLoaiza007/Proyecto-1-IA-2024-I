# [main.py]

# Nota: Esta implementación esta diseñada para ambientes estáticos,
# de hecho, se aprovecha esta caracteristica para que el agente
# tenga una copia del ambiente aunque solo la podrá explorar
# a traves de los sensores
import time
# from agente_reflejo_simple import agente_reflejo_simple as agente
from models.agente_reflejo_simple import agente_reflejo_simple as agente
from models.world_tools import world_tools

# Mapa
nombre_mundo = "world.txt"
juego_activo = True

env_objects_dic = world_tools.reconocer_objetos()
ambiente = world_tools.generar_mundo(nombre_mundo)

rata = agente()
rata.set_coordenadas(world_tools.determinar_posicion(
    ambiente, env_objects_dic['caracter_agente']))
rata.set_ambiente(ambiente, env_objects_dic)
rata.set_meta(world_tools.determinar_posicion(
    ambiente, env_objects_dic['caracter_meta']))

# El ambiente es estático, lo unico que se mueve es el agente
ambiente[rata.coordenadas[0]][rata.coordenadas[1]] = 0

while juego_activo:

    juego_activo = not (rata.meta_alcanzada())

    world_tools.imprimir_juego(
        env_objects_dic, ambiente, rata.get_coordenadas(), rata.get_meta())
    juego_activo = rata.tomar_decision()
    time.sleep(1.3)
