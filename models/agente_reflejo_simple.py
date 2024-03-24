# [Agente_reflejo_simple.py]

debug = False


class agente_reflejo_simple():
    def __init__(self, coordenadas):
        self.coordenadas = coordenadas
        self.pasos = []

    # Coordenadas del agente
    def set_coordenadas(self, coordenadas):
        self.coordenadas = coordenadas
        self.pasos.append(self.coordenadas)

    def get_coordenadas(self):
        return self.coordenadas

    def get_x(self):
        return self.coordenadas[0]

    def get_y(self):
        return self.coordenadas[1]

    def tomar_decision(self, acciones_validas):
        for accion in acciones_validas:
            if accion.get_nombre() == "arriba":
                return accion
            elif accion.get_nombre() == "derecha":
                return accion
        return None

    def iniciar_viaje(self):

        en_viaje = True
        resultado = "Estoy perdido"

        while (en_viaje):
            en_viaje = self.tomar_decision()

            # Verificacion de ciclo:
            # for elemento in self.pasos[:-1]:
            #     if elemento == self.coordenadas:
            #         resultado = "Ya paśe por aqui, algo anda mal :("
            #         en_viaje = False

        return self.pasos, resultado
