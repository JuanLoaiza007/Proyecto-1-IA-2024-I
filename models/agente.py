# [agente.py]

class agente:
    def __init__(self):
        self.coordenadas = None
        self.coordenadas_meta = None
        self.ambiente = None
        self.env_objects_dic = None

    # Coordenadas del agente
    def set_coordenadas(self, coordenadas):
        self.coordenadas = coordenadas

    def get_coordenadas(self):
        return self.coordenadas

    # Coordenadas de la meta
    def set_meta(self, coordenadas_meta):
        self.coordenadas_meta = coordenadas_meta

    def get_meta(self):
        return self.coordenadas_meta

    # Copia ambiente
    def set_ambiente(self, ambiente, env_objects_dic):
        self.ambiente = ambiente
        # env_objects_dic: Lo que puede reconocer el agente (vacio, muro, enemigo...)
        self.env_objects_dic = env_objects_dic

    # Sensores
    def izquierda(self):
        return [self.coordenadas[0], self.coordenadas[1] - 1]

    def derecha(self):
        return [self.coordenadas[0], self.coordenadas[1] + 1]

    def arriba(self):
        return [self.coordenadas[0] - 1, self.coordenadas[1]]

    def abajo(self):
        return [self.coordenadas[0] + 1, self.coordenadas[1]]

    # Extensiones de sensores
    def es_celda_libre(self, coordenadas):
        fila, columna = coordenadas

        filas = len(self.ambiente)
        columnas = len(self.ambiente[0]) if self.ambiente else 0

        if fila >= 0 and fila < filas and columna >= 0 and columna < columnas:
            if self.ambiente[fila][columna] == self.env_objects_dic['vacio'] or self.ambiente[fila][columna] == self.env_objects_dic['meta']:
                return True
        return False

    def libre_izquierda(self):
        return self.es_celda_libre(self.izquierda())

    def libre_derecha(self):
        return self.es_celda_libre(self.derecha())

    def libre_arriba(self):
        return self.es_celda_libre(self.arriba())

    def libre_abajo(self):
        return self.es_celda_libre(self.abajo())

    # Sensor de meta alcanzada
    def meta_alcanzada(self):
        if self.coordenadas == self.coordenadas_meta:
            return True
        return False
