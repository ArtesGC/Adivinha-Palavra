import os
import webbrowser
from random import randint
from sys import argv, exit
from time import sleep

from PyQt5.Qt import *

from history import add_dados, ver_dados, criar_tabela_jogo, apagar_historico
from words import Palavras

__nome__ = "Jogo Adivinha Palavra"
__trademark__ = "™ ArtesGC"
theme = open('themes/ap.qss').read().strip()


class J3A7P6:
    # contantes globais
    NUMERO_TENTATIVA = 0
    PONTOS = 0
    JOGADA = 0
    PALAVRAS = Palavras().listadas()

    def __init__(self):
        # instancia principal da aplicacao
        self.gc = QApplication(argv)

        # ferramenta principal da aplicacao
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle("Adivinha Palavra")
        self.ferramentas.setStyleSheet(theme)
        self.ferramentas.setWindowIcon(QIcon("img/logo.png"))
        self.ferramentas.setFixedSize(700, 550)

        # ******* criando abas para melhor organização *******
        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 30, 700, 520)
        self.tab.setDocumentMode(True)
        self.tab.setTabBarAutoHide(True)
        self.tab.tabBarDoubleClicked.connect(self._remTab)

        # ******* variáveis globais *******
        self.janelaDadosJogador = None
        self.janelaPalavraSecretas = None
        self.janelaHistoricoJogadores = None
        self.nomeJogador = None
        self.nivel = None
        self.letraJogador = None

        # ******* menu *******
        menuFerramentas = QMenuBar(self.ferramentas)
        self.reiniciarJogo = menuFerramentas.addAction("Reiniciar")
        self.reiniciarJogo.setEnabled(False)
        self.reiniciarJogo.triggered.connect(self._reiniciarJogo)

        opcoes = menuFerramentas.addMenu("Opções")

        instr = opcoes.addAction("Instruções")
        instr.triggered.connect(self._instr)
        opcoes.addSeparator()

        palavraSecretas = opcoes.addAction("Palavras Secretas")
        palavraSecretas.triggered.connect(self._palavrasSecretas)
        opcoes.addSeparator()

        histor = opcoes.addAction("Historico de Jogadores")
        histor.triggered.connect(self._historico)
        opcoes.addSeparator()

        sair = opcoes.addAction("Sair")
        sair.triggered.connect(self._sair)

        sobre = menuFerramentas.addAction("Sobre")
        sobre.triggered.connect(self._sobre)

        # inicializacao do programa
        self.janelaPrincipal()

    # funcao especial (ler doc da funcao)
    def _remTab(self):
        """
        remove a aba dando dois cliques na barra contendo o nome
        ***EGG***
        """
        if self.tab.currentIndex() == 0:
            pass
        else:
            self.tab.removeTab(self.tab.currentIndex())

    # otimizacao para abertura das janelas
    def _historico(self):
        """
        abrir a janela do historico de jogadores sem duplicacoes
        ou retorno de valores nulos
        """
        if self.janelaHistoricoJogadores is None:
            return self.historicoJogadores()
        else:
            try:
                self.tab.addTab(self.janelaHistoricoJogadores, 'Historico')
                self.tab.setCurrentWidget(self.janelaHistoricoJogadores)
            except Exception:
                self.tab.removeTab(1)
                return self.historicoJogadores()

    def _reiniciarJogo(self):
        """
        reiniciar o jogo, ie, apartir da janela de introducao de dados
        """
        if self.janelaDadosJogador is None:
            return self.dadosJogador()
        else:
            try:
                self.tab.removeTab(0)
                self.tab.addTab(self.janelaDadosJogador, 'Jogador')
                self.tab.setCurrentWidget(self.janelaDadosJogador)
            except Exception as e:
                self.tab.removeTab(0)
                return self.dadosJogador()

    def _palavrasSecretas(self):
        """
        abrir a janela com as possiveis palavras secretas sem duplicacoes
        ou retorno de valores nulos
        """
        if self.janelaPalavraSecretas is None:
            return self.palavrasSecretas()
        else:
            try:
                self.tab.addTab(self.janelaPalavraSecretas, 'Palavras Secretas')
                self.tab.setCurrentWidget(self.janelaPalavraSecretas)
            except Exception as e:
                self.tab.removeTab(1)
                return self.palavrasSecretas()

    # funcoes do menu
    def _instr(self):
        janelainfo = QDialog(self.ferramentas)
        janelainfo.setWindowTitle('Instruções')

        layout = QVBoxLayout()
        layout.setSpacing(20)

        infoProg = QLabel("""
Olá Que a Paz e Bençãos de Deus Estejam Sobre Ti e Toda Tua Família..<br>
Este Jogo Consiste em Ganhar o Máximo de Pontos Possiveis em Poucas Tentativas,<br>
acertando Que Palavra Foi Definida (LETRA POR LETRA)..
<br><br>
Para uma melhor experiência de jogo:<br><b>
- Conte quantas letras tem a suposta palavra<br>
- identificada pelos simbolos '_' (referem-se as letras da palavra)<br>
- e use a lista de palavras que estão escondidas no menu de opções (Palavras Secretas)<br>
- Use as como referência para as suas tentativas!</b>
<br><br>
Que Deus Te Ilumine Nessa Aventura!
<br><br>
Dica:<br>
Qualidades e Códigos de Honra;
<br><br>
Muito Obrigado pelo apoio!<br>
<a href="https://artesgc.home.blog" style="text-decoration:none;">&trade; ArtesGC Inc</a>""")
        infoProg.setStyleSheet("border-style:solid;"
                               "border-color:black;"
                               "border-width:1px;"
                               "border-radius:3px;"
                               "background-color:white;"
                               "padding:5px;")
        layout.addWidget(infoProg)

        def fechar():
            janelainfo.close()

        botaoFechar = QPushButton("Fechar")
        botaoFechar.setStyleSheet('background-color:red;')
        botaoFechar.clicked.connect(fechar)
        layout.addWidget(botaoFechar)

        janelainfo.setLayout(layout)
        janelainfo.show()

    def _sobre(self):
        janelainfo = QDialog(self.ferramentas)
        janelainfo.setWindowTitle('Sobre')

        layout = QVBoxLayout()
        layout.setSpacing(20)

        infoProg = QLabel("""
Nome: <b>Jogo Adivinha Palavra</b><br>
Versão: <b>0.7-072021</b><br>
Designers e Programadores: 
<a href="https://github.com/Nurul-GC" style="text-decoration:none;">Nurul GC</a>, 
<a href="https://github.com/Paulo-Lopes-Estevao" style="text-decoration:none;">Paulo Lopes Estevao</a><br>
Empresa: <a href="https://artesgc.home.blog" style="text-decoration:none;">&trade; ArtesGC Inc</a>""")
        infoProg.setStyleSheet("border-style:solid;"
                               "border-color:black;"
                               "border-width:1px;"
                               "border-radius:3px;"
                               "background-color:white;"
                               "padding:5px;")
        layout.addWidget(infoProg)

        def fechar():
            janelainfo.close()

        botaoFechar = QPushButton("Fechar")
        botaoFechar.setStyleSheet('background-color:red;')
        botaoFechar.clicked.connect(fechar)
        layout.addWidget(botaoFechar)

        janelainfo.setLayout(layout)
        janelainfo.show()

    def _sair(self):
        sair = QMessageBox.question(
            self.ferramentas, "Sair", "Tem mesmo a certeza que deseja sair?")
        if sair == QMessageBox.Yes:
            exit(0)
        else:
            pass

    # janelas do programa
    def janelaPrincipal(self):
        janela01 = QWidget()
        layout = QVBoxLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/icon.png").scaled(QSize(570, 400)))
        labelImagem.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelImagem)

        barraProgresso = QProgressBar()
        barraProgresso.setGeometry(200, 100, 200, 30)
        barraProgresso.setAlignment(Qt.AlignHCenter)
        layout.addWidget(barraProgresso)

        def processar():
            n = randint(1, 5)
            sec = 0.2
            for i in range(0, 101, n):
                sleep(sec)
                barraProgresso.setValue(i)
            self.tab.removeTab(0)
            self.dadosJogador()

        botaoIniciar = QPushButton("Iniciar Jogo")
        botaoIniciar.setStyleSheet("background-color:#D1C399;")
        botaoIniciar.clicked.connect(processar)
        layout.addWidget(botaoIniciar)

        janela01.setLayout(layout)
        self.tab.addTab(janela01, "Bem-Vindo")
        self.tab.setCurrentWidget(janela01)

    def historicoJogadores(self):
        def inciarModel(_model):
            _model.setTable('tb_jogo')
            _model.select()
            _model.setHeaderData(0, Qt.Horizontal, "id")
            _model.setHeaderData(1, Qt.Horizontal, "nome")
            _model.setHeaderData(2, Qt.Horizontal, "pontos")
            _model.setHeaderData(3, Qt.Horizontal, "jogada")
            _model.setHeaderData(4, Qt.Horizontal, "nivel")

        def zerar():
            apagar_historico()
            self._historico()

        self.janelaHistoricoJogadores = QWidget()
        layout = QVBoxLayout()

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('historico/ap.db')
        db.open()

        model = QSqlTableModel()
        inciarModel(model)

        labelIntro = QLabel("<b>" + ".  . " * 5 + "HISTORICO" + 5 * " .  ." + "</b>")
        labelIntro.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelIntro)

        view = QTableView()
        view.setFixedWidth(515)
        view.setUpdatesEnabled(True)
        view.setAlternatingRowColors(True)
        view.setModel(model)
        layout.addWidget(view, alignment=Qt.AlignHCenter)

        botaoZerar = QPushButton("Zerar Historico")
        botaoZerar.setStyleSheet('background-color:cyan;')
        botaoZerar.clicked.connect(zerar)
        layout.addWidget(botaoZerar)

        def fechar():
            self.tab.removeTab(self.tab.currentIndex())

        botaoFechar = QPushButton("Fechar")
        botaoFechar.setStyleSheet('background-color:red;')
        botaoFechar.clicked.connect(fechar)
        layout.addWidget(botaoFechar)

        self.janelaHistoricoJogadores.setLayout(layout)
        self.tab.addTab(self.janelaHistoricoJogadores, 'Historico')
        self.tab.setCurrentWidget(self.janelaHistoricoJogadores)

    def dadosJogador(self):
        # activar a opção de reiniciar jogo
        self.reiniciarJogo.setEnabled(True)

        def validar_dados_jogador():
            if self.nomeJogador.text() == "" or self.nomeJogador.text().isspace() or self.nomeJogador.text() is None:
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Nome do jogador não definido..')
            else:
                if self.nivel.currentText() == '3':
                    self.NUMERO_TENTATIVA = 15
                    self.PONTOS = 0
                    self.tab.removeTab(0)
                    self.janelaJogo()
                elif self.nivel.currentText() == '2':
                    self.NUMERO_TENTATIVA = 20
                    self.PONTOS = 0
                    self.tab.removeTab(0)
                    self.janelaJogo()
                elif self.nivel.currentText() == '1':
                    self.NUMERO_TENTATIVA = 25
                    self.PONTOS = 0
                    self.tab.removeTab(0)
                    self.janelaJogo()
                else:
                    QMessageBox.warning(self.ferramentas, 'Aviso', 'Nível não definido..')

        QMessageBox.information(self.ferramentas, "Atenção", "Para uma melhor experiência de jogo leia as instruções que se encontram na barra de menu.."
                                                             "\nObrigado pelo apoio! - ArtesGC")
        self.janelaDadosJogador = QWidget()
        layout = QFormLayout()
        layout.setVerticalSpacing(20)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/01.png"))
        labelImagem.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelImagem)

        labelExtra = QLabel("<b>" + ".  . " * 5 + "DADOS DO JOGADOR" + " .  ." * 5 + "</b>")
        labelExtra.setAlignment(Qt.AlignCenter)
        layout.addRow(labelExtra)

        self.nomeJogador = QLineEdit()
        self.nomeJogador.setPlaceholderText("Digite o seu nome..")
        layout.addRow(self.nomeJogador)

        niveis = ['1', '2', '3']
        self.nivel = QComboBox()
        self.nivel.addItems(niveis)
        self.nivel.setToolTip('Nível 1 - 25 tentativas\nNível 2 - 20 tentativas\nNível 3 - 15 tentativas')
        layout.addRow("<b>Selecione o &Nível:</b>", self.nivel)

        botaoJogar = QPushButton("Jogar")
        botaoJogar.setDefault(True)
        botaoJogar.setStyleSheet("background-color:green;")
        botaoJogar.clicked.connect(validar_dados_jogador)
        layout.addRow(botaoJogar)

        def browser(p):
            return webbrowser.open('https://artesgc.home.blog')

        labelCopyright = QLabel(
            "<a href='#' style='text-decoration:none;'>&trade;ArtesGC Inc.</a>")
        labelCopyright.setAlignment(Qt.AlignRight)
        labelCopyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        labelCopyright.linkActivated.connect(browser)
        layout.addWidget(labelCopyright)

        self.janelaDadosJogador.setLayout(layout)
        self.tab.addTab(self.janelaDadosJogador, 'Jogador')
        self.tab.setCurrentWidget(self.janelaDadosJogador)

    def janelaJogo(self):
        tamanhoListaPalavras = len(self.PALAVRAS)
        selecionaPalavraAleatoria = self.PALAVRAS[randint(0, tamanhoListaPalavras - 1)]
        agrupaLetrasPalavra = ['_' for letra in selecionaPalavraAleatoria]

        def validaJogada():
            if self.letraJogador.text() == "" or self.letraJogador.text().isspace() or None:
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Letra para tentativa não atribuida..')
            elif not self.letraJogador.text().isalpha():
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Letra para tentativa não atribuida..')
            else:
                def novoJogo():
                    self.JOGADA = 0
                    self.tab.removeTab(0)
                    self.janelaJogo()

                self.JOGADA += 1
                posicao = 0
                completou = '_' not in agrupaLetrasPalavra

                if completou:
                    add_dados(self.nomeJogador.text(), self.PONTOS, self.JOGADA, self.nivel.currentText())
                    labelJogo.setText(f"""(^3^) Parabéns {self.nomeJogador.text()}
VOCÊ GANHOU..

{agrupaLetrasPalavra}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
Pontos: {self.PONTOS}""")
                    labelJogo.setStyleSheet("background-color:white; color:green; border-radius: 3px; border: 2px solid; padding:50px;")
                    botaoValida.setText('Novo Jogo')
                    botaoValida.clicked.connect(novoJogo)
                elif self.JOGADA == self.NUMERO_TENTATIVA:
                    add_dados(self.nomeJogador.text(), self.PONTOS, self.JOGADA, self.nivel.currentText())
                    labelJogo.setText(f"""(T.T) Lamento {self.nomeJogador.text()}
VOCÊ ESGOTOU TODAS AS SUAS TENTATIVAS..

Palavra Secreta: {selecionaPalavraAleatoria}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
Pontos: {self.PONTOS}""")
                    labelJogo.setStyleSheet("background-color:white; color:red; border-radius: 3px; border: 2px solid; padding:50px;")
                    botaoValida.setText('Novo Jogo')
                    botaoValida.clicked.connect(novoJogo)
                elif self.letraJogador.text().upper() in selecionaPalavraAleatoria:
                    for letra in selecionaPalavraAleatoria:
                        if self.letraJogador.text().upper() == letra:
                            self.PONTOS += randint(50, 200)
                            agrupaLetrasPalavra[posicao] = self.letraJogador.text().upper()
                            labelJogo.setText(f"""Nível: {self.nivel.currentText()} - Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}

(^.^) Obaa..
VOCÊ ACERTOU {self.nomeJogador.text()}!

{agrupaLetrasPalavra}

Pontos {self.PONTOS}""")
                            labelJogo.setStyleSheet("background-color:white; "
                                                    "color:blue; "
                                                    "border-radius: 3px; "
                                                    "border: 2px solid; "
                                                    "padding:50px;")
                        posicao += 1
                    if completou:
                        add_dados(self.nomeJogador.text(), self.PONTOS, self.JOGADA, self.nivel.currentText())
                        labelJogo.setText(f"""(^3^) Parabéns {self.nomeJogador.text()}
VOCÊ GANHOU..

{agrupaLetrasPalavra}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
Pontos: {self.PONTOS}""")
                        labelJogo.setStyleSheet("background-color:white; "
                                                "color:green; "
                                                "border-radius: 3px; "
                                                "border: 2px solid; "
                                                "padding:50px;")
                        botaoValida.setText('Novo Jogo')
                        botaoValida.clicked.connect(novoJogo)
                else:
                    self.PONTOS -= randint(10, 50)
                    labelJogo.setText(f"""Nível: {self.nivel.currentText()} - Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}

(O_O) Upss..
VOCÊ ERROU {self.nomeJogador.text()}!

Pontos {self.PONTOS}""")
                    labelJogo.setStyleSheet("background-color:white; "
                                            "color:red; "
                                            "border-radius: 3px; "
                                            "border: 2px solid; "
                                            "padding:50px;")

        janela03 = QWidget()
        layout = QFormLayout()
        layout.setVerticalSpacing(20)

        labelInfo = QLabel(f"<h3>Bem-Vindo <i>{self.nomeJogador.text()}</i><br>"
                           f"Tente Adivinhar Qual é a Palavra Secreta..</h3><br>"
                           f"<i>{agrupaLetrasPalavra}</i>")
        labelInfo.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelInfo)

        labelJogo = QLabel('.  .  .  .  .')
        labelJogo.setStyleSheet("background-color: white; "
                                "border-radius: 3px; "
                                "border: 2px solid; "
                                "padding:100px;")
        labelJogo.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelJogo)

        labelExtra = QLabel("<b>" + ".  . " * 5 + "JOGANDO" + " .  ." * 5 + "</b>")
        labelExtra.setAlignment(Qt.AlignCenter)
        layout.addRow(labelExtra)

        self.letraJogador = QLineEdit()
        self.letraJogador.setMaxLength(1)
        self.letraJogador.setPlaceholderText("Digite a letra e pressione ENTER..")
        self.letraJogador.returnPressed.connect(validaJogada)
        layout.addRow(self.letraJogador)

        botaoValida = QPushButton('Validar Jogada')
        botaoValida.setDefault(True)
        botaoValida.clicked.connect(validaJogada)
        botaoValida.setStyleSheet('background-color: cyan;')

        botaoFimJogo = QPushButton('Terminar o Jogo')
        botaoFimJogo.clicked.connect(self._sair)
        botaoFimJogo.setStyleSheet('background-color:red;')
        layout.addRow(botaoValida, botaoFimJogo)

        janela03.setLayout(layout)
        self.tab.addTab(janela03, 'Jogando')
        self.tab.setCurrentWidget(janela03)

    def palavrasSecretas(self):
        self.janelaPalavraSecretas = QWidget()
        layout = QVBoxLayout()

        labelIntro = QLabel("<b>" + ".  . " * 5 + "PALAVRAS SECRETAS" + 5 * " .  ." + "</b>")
        labelIntro.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelIntro)

        listaPalavras = QListWidget()
        for palavra in sorted(self.PALAVRAS):
            listaPalavras.addItem(palavra)
        listaPalavras.setAlternatingRowColors(True)
        layout.addWidget(listaPalavras)

        labelExtra = QLabel(f"<i>*{len(self.PALAVRAS)} palavras..</i>")
        labelExtra.setAlignment(Qt.AlignRight)
        labelExtra.setStyleSheet("color:#D1C399;")
        layout.addWidget(labelExtra)

        def fechar(): return self.tab.removeTab(self.tab.currentIndex())

        botaoFechar = QPushButton("Fechar")
        botaoFechar.setStyleSheet('background-color:red;')
        botaoFechar.clicked.connect(fechar)
        layout.addWidget(botaoFechar)

        self.janelaPalavraSecretas.setLayout(layout)
        self.tab.addTab(self.janelaPalavraSecretas, 'Palavras Secretas')
        self.tab.setCurrentWidget(self.janelaPalavraSecretas)


if __name__ == '__main__':
    criar_tabela_jogo()
    app = J3A7P6()
    app.ferramentas.show()
    app.gc.exec_()
