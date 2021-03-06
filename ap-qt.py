# ******************************************************************************
#  (c) 2019-2021. Nurul GC                                                     *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicaçoes                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from PyQt5.Qt import *
from sys import argv
from time import sleep
from random import randint

__nome__ = "Jogo Adivinha Palavra"
__version__ = "0.5-032021"
__copyright__ = "© 2019-2021 Nurul-GC"
__trademark__ = "™ ArtesGC"


class J3A7P6:
    def __init__(self):
        self.gc = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle("Adivinha Palavra")
        self.ferramentas.setWindowIcon(QIcon("img/adivinhapalavra-ico2.png"))
        self.ferramentas.setFixedSize(600, 500)

        # criando abas para melhor organização
        self.tab = QTabWidget(self.ferramentas)
        self.tab.setFixedSize(600, 480)
        self.tab.move(0, 25)

        self.janelaPrincipal()

    def janelaPrincipal(self):
        self.ferramentas.setPalette(QPalette(QColor('black')))
        janela01 = QWidget()
        layout = QVBoxLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/adivinhapalavra-ico2.png").scaled(QSize(350, 350)))
        labelImagem.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelImagem)

        barraProgresso = QProgressBar()
        barraProgresso.setGeometry(200, 100, 200, 30)
        barraProgresso.setAlignment(Qt.AlignHCenter)
        barraProgresso.setStyleSheet("""
        QProgressBar{
        border: 1px solid green
        }""")
        layout.addWidget(barraProgresso)

        def processar():
            if botaoIniciar.isChecked():
                pass
            else:
                n = randint(1, 5)
                for i in range(0, 101, n):
                    sleep(0.5)
                    barraProgresso.setValue(i)
                self.tab.removeTab(0)
                self.iniciarJogo()

        botaoIniciar = QPushButton("Iniciar Jogo")
        botaoIniciar.setChecked(True)
        botaoIniciar.setDefault(True)
        botaoIniciar.clicked.connect(processar)
        layout.addWidget(botaoIniciar)
        janela01.setLayout(layout)
        self.tab.addTab(janela01, "Bem-Vindo")
        self.tab.setCurrentWidget(janela01)

    def iniciarJogo(self):
        QMessageBox.information(self.ferramentas, "Atenção", "Para uma melhor experiência de jogo leia as instruções que se encontram no menu de opções..\nObrigado pelo apoio! - ArtesGC")
        self.ferramentas.setPalette(QPalette(QColor('cadetblue')))
        janela02 = QWidget()
        layout = QFormLayout()
        layout.setVerticalSpacing(5)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/03.png"))
        labelImagem.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelImagem)

        nomeJogador = QLineEdit()
        layout.addRow("<b>&Nome do Jogador: *</b>", nomeJogador)

        def jogo():
            # self.tab.removeTab(0)
            self.jogo()

        niveis = ['1', '2', '3']
        nivel = QComboBox()
        nivel.addItems(niveis)
        nivel.activated.connect(jogo)
        layout.addRow("<b>Selecione o &nível: *</b>", nivel)



        janela02.setLayout(layout)
        self.tab.addTab(janela02, "Jogador")
        self.tab.setCurrentWidget(janela02)

    def jogo(self):
        pass


if __name__ == '__main__':
    app = J3A7P6()
    app.ferramentas.show()
    app.gc.exec_()
