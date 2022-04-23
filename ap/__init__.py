import os
from random import randint
from sys import argv
from time import sleep

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from ap.func import debugpath
from ap.history import criar_tabela_jogo
from ap.jogo import J3A7P6


class JAP:
    def __init__(self):
        # instancia principal da aplicação
        self.gc = QApplication(argv)

        img = QPixmap("./ap-icons/init-favicon.png")
        self.align = int(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignAbsolute)
        self.janela = QSplashScreen(img)
        self.janela.setStyleSheet(theme)
        self.janela.show()
        self.iniciar()

    def iniciar(self):
        load = 0
        while load < 100:
            self.janela.showMessage(f"Carregando o Pacote do Jogo: {load}%", self.align, Qt.GlobalColor.black)
            sleep(0.5)
            load += randint(5, 10)
        self.janela.close()
        return J3A7P6().ferramentas.show()


if __name__ == '__main__':
    os.makedirs(debugpath(), exist_ok=True)
    criar_tabela_jogo()
    theme = open("./ap-themes/ap.qss").read().strip()
    gcApp = JAP()
    gcApp.gc.exec()
