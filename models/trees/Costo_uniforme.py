# [Costo_uniforme.py]

from models.shared.Estructuras_datos import *
import time
from queue import PriorityQueue

evitar_devolverse = True
evitar_ciclo = True

debug = True

class Costo_uniforme:
    def busqueda_por_costo_uniforme(problema: Problema):
        nodos_expandidos = 0
        profundidad = 0
        reporte = "Generando..."   
        
        tiempo_inicio = time.time()
        # cola_prioridad = []
        cola_prioridad = PriorityQueue()
        cola_prioridad.put((0, Nodo(problema)))
        visitados = set()
        # print(cola_prioridad.get())
        
        # while not len(cola_prioridad) == 0:
        while not cola_prioridad.empty():
            print(f"La cola de prioridad actual es {cola_prioridad}")
            costo_acumulado, nodo = cola_prioridad.get()  # Saca un nodo de la cola
            print(costo_acumulado)
            print(nodo)       
            print((costo_acumulado, nodo))
            
            if nodo.es_meta():
                camino = Costo_uniforme.reconstruir_camino(nodo)
                reporte = Costo_uniforme.generar_reporte(
                    nodos_expandidos, profundidad, tiempo_inicio, nodo)

                return camino, 'Encontré a grogu', reporte
            
            if nodo.get_estado in visitados:
                continue
            
            visitados.add(nodo.get_estado)
            
            # Expande el nodo y obtiene sus hijos
            hijos: "list[Nodo]" = nodo.expandir()

            # Actualiza cantidad de nodos expandidos
            nodos_expandidos += 1   
            
            for hijo in hijos:
                print(f"El hijo actual es {hijo}")
                # Actualiza profundidad
                if profundidad < hijo.get_profundidad():
                    profundidad = hijo.get_profundidad()

                if evitar_devolverse and Costo_uniforme.se_ha_devuelto(hijo):
                    print_debug("paso, queria ir a {} pero hace dos pasos estuve en {}".format(
                        str(hijo.get_estado()), str(nodo.get_padre().get_estado())))
                    continue

                if evitar_ciclo and Costo_uniforme.cayo_en_ciclo(hijo):
                    print_debug("paso, hace un tiempo estuve en {}, evitare entrar en ciclo".format(
                        str(hijo.get_estado())))
                    continue
                                
                cola_prioridad.put((hijo.get_costo_acumulado(), hijo))  # Agrega los hijos a la cola
                print(hijo.get_costo_acumulado())
                print(hijo)
                print((hijo.get_costo_acumulado(), hijo))
                print(cola_prioridad)
                # cola_prioridad.sort(reverse=False)
                # print(f"El contenido de la cola es{cola_prioridad.get()}")
            
            # while not cola_prioridad.empty(): print(f"Los nuevos hijos son: {cola_prioridad.get()}")
            
        camino = Costo_uniforme.reconstruir_camino(nodo)
        reporte = Costo_uniforme.generar_reporte(
            nodos_expandidos, profundidad, tiempo_inicio, nodo)

        return camino, 'Me perdí', reporte

    @staticmethod
    def reconstruir_camino(nodo: Nodo):
        # Reconstruir el camino desde el nodo solución hasta el nodo raíz
        camino = []
        while nodo is not None:
            estado = nodo.get_estado()
            camino.append(estado.get_coordenadas())
            nodo = nodo.get_padre()
        # Revertir el camino para que esté en orden desde el nodo raíz hasta la solución
        return camino[::-1]

    @staticmethod
    def se_ha_devuelto(nodo: Nodo):
        # El nodo no tiene padre o abuelo
        if nodo.get_profundidad() <= 1:
            return False

        abuelo = nodo.get_padre().get_padre()
        nodo = nodo

        # El nodo es igual a su abuelo, se esta devolviendo
        if ((str(nodo.get_estado()) == str(abuelo.get_estado()))):
            return True

        return False

    @staticmethod
    def cayo_en_ciclo(nodo: Nodo):
        # El nodo no tiene padre o abuelo
        if nodo.get_profundidad() <= 1:
            return False

        antecesor = nodo.get_padre().get_padre()
        nodo = nodo

        while (antecesor != None):
            # El nodo es igual a un antecesor, cayo a un ciclo
            if ((str(nodo.get_estado()) == str(antecesor.get_estado()))):
                return True
            antecesor = antecesor.get_padre()

        return False

    @staticmethod
    def generar_reporte(nodos_expandidos, profundidad, tiempo_inicio, nodo_act: Nodo):
        tiempo_computo = round(time.time() - tiempo_inicio, 6)
        return "Cantidad de nodos expandidos: {}\nProfundidad del arbol: {}\nTiempo de computo: {} s\nCosto: {}".format(
            str(nodos_expandidos), str(profundidad), str(tiempo_computo), str(nodo_act.get_costo_acumulado()))                                  

class Test():
    @staticmethod
    def start():
        from models.shared.tools.World_tools import World_tools as wtools
        from models.shared.tools.File_selector import File_selector

        env_objects_dic = wtools.reconocer_objetos()

        # Cargar archivo de mundo
        file_selector = File_selector()
        archivo = file_selector.select("data/worlds")

        ambiente = wtools.generar_mundo(archivo)

        # Inicializar estado inicial y estado objetivo
        x_ini, y_ini = wtools.determinar_posicion(
            ambiente, env_objects_dic['agente'])
        x_meta, y_meta = wtools.determinar_posicion(
            ambiente, env_objects_dic['meta'])

        # Inicializar estados
        estado_inicial = Estado(x_ini, y_ini)
        estado_objetivo = Estado(x_meta, y_meta)

        # Eliminar el self.estado_inicial del ambiente
        ambiente[x_ini][y_ini] = "0"

        problema = Problema(estado_inicial, estado_objetivo, ambiente)

        print(Costo_uniforme.busqueda_por_costo_uniforme(problema))