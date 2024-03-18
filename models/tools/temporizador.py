from PyQt5.QtCore import QTimer, QEventLoop


class Temporizador:
    @staticmethod
    def iniciar(tiempo_segundos):
        loop = QEventLoop()
        timer = QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(loop.quit)
        tiempo_ms = tiempo_segundos * 1000
        timer.start(tiempo_ms)
        loop.exec_()
