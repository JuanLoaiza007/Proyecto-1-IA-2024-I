# [CommonTreeUtils.py]

from models.shared.Estructuras_datos import *
import time


class CommonTreeUtils:
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
    def detectar_nave(nodo: Nodo):
        coordenadas = None
        while (nodo != None):
            if (nodo.problema.estado_inicial.en_nave):
                coordenadas = str(nodo.problema.estado_inicial)

        return coordenadas

    @staticmethod
    def generar_reporte(nodos_expandidos, profundidad, tiempo_inicio, nodo_act: Nodo):
        tiempo_computo = round(time.time() - tiempo_inicio, 6)
        return "Cantidad de nodos expandidos: {}\nProfundidad del arbol: {}\nTiempo de computo: {} s\nCosto: {}".format(
            str(nodos_expandidos), str(profundidad), str(tiempo_computo), str(nodo_act.get_costo_acumulado()))
