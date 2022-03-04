from random import randint
from sys import exit
from time import sleep
from webbrowser import open_new

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *
from PyQt6.QtWidgets import *

from ap.history import add_dados, apagar_historico
from ap.words import Palavras

theme = open('themes/ap.qss').read().strip()


class J3A7P6:
    def __init__(self):
        # ******* variáveis globais *******
        self.janela_dados_jogador = None
        self.nome_jogador = None
        self.nivel = None
        self.letra_jogador = None

        # constantes globais
        self.PONTOS = 0
        self.JOGADA = 0
        self.NUMERO_TENTATIVA = 0
        self.PALAVRAS = Palavras().listadas()

        # ferramenta principal da aplicação
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle("Adivinha Palavra")
        self.ferramentas.setWindowIcon(QIcon("icons/favicon-192x192.png"))

        bg_image = QImage(f"icons/icon.png")
        set_bg_image = bg_image.scaled(QSize(300, 300))  # resize Image to widget's size
        palette = QPalette()
        palette.setBrush(palette.ColorGroup.All, palette.ColorRole.Window, QBrush(set_bg_image))
        self.ferramentas.setPalette(palette)
        self.ferramentas.setStyleSheet(theme)

        # ******* menu *******
        menu_ferramentas = QMenuBar()
        self.reiniciar_jogo = menu_ferramentas.addAction("Reiniciar")
        self.reiniciar_jogo.setEnabled(False)
        self.reiniciar_jogo.triggered.connect(self._reiniciar_jogo)

        opcoes = menu_ferramentas.addMenu("Opções")

        instr = opcoes.addAction("Instruções")
        instr.triggered.connect(self._instr)
        opcoes.addSeparator()

        palavra_secretas = opcoes.addAction("Palavras Secretas")
        palavra_secretas.triggered.connect(self.palavras_secretas)
        opcoes.addSeparator()

        histor = opcoes.addAction("Historico de Jogadores")
        histor.triggered.connect(self.historico_jogadores)
        opcoes.addSeparator()

        sair = opcoes.addAction("Sair")
        sair.triggered.connect(self._sair)

        sobre = menu_ferramentas.addAction("Sobre")
        sobre.triggered.connect(self._sobre)

        # layout principal da aplicação
        self.layout_principal = QVBoxLayout()
        self.layout_principal.setMenuBar(menu_ferramentas)

        self.ferramentas.setLayout(self.layout_principal)
        self.janela_principal()

    # optimização para abertura das janelas
    def _reiniciar_jogo(self):
        """
        reiniciar o jogo, ie, apartir da janela de introducao de dados
        """
        if self.janela_dados_jogador is None:
            self.dados_jogador()
        else:
            self.janela_dados_jogador = None
            self.dados_jogador()

    # funções do menu
    def _instr(self):
        janelainfo = QDialog(self.ferramentas)
        janelainfo.setWindowTitle('Instruções')

        layout = QVBoxLayout()
        layout.setSpacing(20)

        info_prog = QLabel(
            """
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
<a href="https://artesgc.home.blog" style="text-decoration:none;"><b>&trade;ArtesGC Inc</b></a>"""
            )
        info_prog.setStyleSheet(
            "border-style:solid;"
            "border-color:black;"
            "border-width:1px;"
            "border-radius:3px;"
            "background-color:cadetblue;"
            "padding:10px;"
            )
        layout.addWidget(info_prog)

        def fechar():
            janelainfo.close()

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setStyleSheet(
            "QPushButton{background-color:red;}"
            "QPushButton:hover{background-color:white;}"
            )
        botao_fechar.clicked.connect(fechar)
        layout.addWidget(botao_fechar)

        janelainfo.setLayout(layout)
        janelainfo.show()

    def _sobre(self):
        janelainfo = QDialog(self.ferramentas)
        janelainfo.setWindowTitle('Sobre')

        layout = QVBoxLayout()
        layout.setSpacing(20)

        info_prog = QLabel(
            """
Nome: <b>Jogo Adivinha Palavra</b><br>
Versão: <b>0.9-032022</b><br>
Designers e Programadores: 
<a href="https://github.com/Nurul-GC" style="text-decoration:none;"><b>Nurul GC</b></a>, 
<a href="https://github.com/Paulo-Lopes-Estevao" style="text-decoration:none;"><b>Paulo Lopes Estevão</b></a><br>
Empresa: <a href="https://artesgc.home.blog" style="text-decoration:none;"><b>&trade;ArtesGC Inc</b></a>"""
            )
        info_prog.setStyleSheet(
            "border-style:solid;"
            "border-color:black;"
            "border-width:1px;"
            "border-radius:3px;"
            "background-color:cadetblue;"
            "padding:10px;"
            )
        layout.addWidget(info_prog)

        def fechar():
            janelainfo.close()

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setStyleSheet(
            "QPushButton{background-color:red;}"
            "QPushButton:hover{background-color:white;}"
            )
        botao_fechar.clicked.connect(fechar)
        layout.addWidget(botao_fechar)

        janelainfo.setLayout(layout)
        janelainfo.show()

    def _sair(self):
        sair = QMessageBox.question(self.ferramentas, "Sair", "<h3>Tem mesmo a certeza que deseja terminar o jogo?</h3>")
        if sair == QMessageBox.StandardButton.Yes:
            exit(0)

    # janelas do programa
    def janela_principal(self):
        janela_principal = QWidget()
        janela_principal.setStyleSheet(
            "background-color: cadetblue;"
            "border-radius: 5px;"
        )

        layout = QFormLayout()

        label_intro = QLabel("<h3>Bem-Vindo ao..</h3>"
                             "<h1 style='color:white;'>A-P</h1><hr>")
        label_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_intro)

        label_imagem = QLabel()
        label_imagem.setPixmap(QPixmap("icons/icon.png").scaled(1200//4, 1200//4))  # todo: duvida no uso dos icons!
        label_imagem.setStyleSheet("margin: auto;")
        label_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_imagem)

        def processar():
            n = randint(1, 5)
            for i in range(0, 101, n):
                sleep(0.5)
                barra_progresso.setValue(i)
            # self.tab.removeTab(self.tab.currentIndex())
            janela_principal.close()
            self.dados_jogador()
            QMessageBox.information(
                self.ferramentas, "Atenção",
                "Para uma melhor experiência de jogo leia as instruções que se encontram na barra de menu.. "
                "\nObrigado pelo apoio! - ArtesGC"
            )

        botao_iniciar = QPushButton("Iniciar Jogo")
        botao_iniciar.setStyleSheet(
            "QPushButton{background-color:#D1C399;}"
            "QPushButton:hover{background-color:white;}"
        )
        botao_iniciar.clicked.connect(processar)

        barra_progresso = QProgressBar()
        barra_progresso.setGeometry(200, 100, 200, 30)
        barra_progresso.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addRow(botao_iniciar, barra_progresso)

        # ******* ... *******
        def browser():
            open_new('https://artesgc.home.blog')

        label_copyright = QLabel("<hr><a href='#' style='text-decoration:none;'>&trade;ArtesGC Inc.</a>", self.ferramentas)
        label_copyright.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_copyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        label_copyright.linkActivated.connect(browser)
        layout.addRow(label_copyright)

        janela_principal.setLayout(layout)
        self.layout_principal.addWidget(janela_principal)

    def historico_jogadores(self):
        # def inciar_model(_model):

        # def conectar_db():

        def zerar_db():
            apagar_historico()
            QMessageBox.information(
                self.ferramentas, 'Operação bem sucedida',
                f'Operação concluida, os dados serão atualizados automaticamente após o reinício '
                f'do programa..'
                )
            return fechar()

        def fechar():
            # self.tab.removeTab(self.tab.currentIndex())
            janela_historico_jogadores.close()

        janela_historico_jogadores = QDialog(self.ferramentas)
        janela_historico_jogadores.setStyleSheet(
            "background-color: cadetblue;"
            "border-radius: 5px;"
            )
        janela_historico_jogadores.setWindowTitle("Historico de Jogadores")

        layout = QVBoxLayout()
        layout.setSpacing(10)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('historico/ap.db')
        model = QSqlTableModel()
        model.setTable('tb_jogo')
        model.select()
        model.setHeaderData(0, Qt.Orientation.Horizontal, "id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "nome")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "pontos")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "tentativas")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "nivel")

        label_intro = QLabel("<b>" + " . " * 5 + "H I S T O R I C O - J O G A D O R E S" + 5 * " . " + "</b><hr>")
        label_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_intro)

        view = QTableView()
        view.setFixedWidth(560)
        view.setAlternatingRowColors(True)
        view.setModel(model)
        layout.addWidget(view, alignment=Qt.AlignmentFlag.AlignHCenter)

        botao_zerar = QPushButton("Zerar Historico")
        botao_zerar.setStyleSheet(
            "QPushButton{background-color:cyan;}"
            "QPushButton:hover{background-color:white;}"
            )
        botao_zerar.clicked.connect(zerar_db)
        layout.addWidget(botao_zerar)

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setStyleSheet(
            "QPushButton{background-color:red;}"
            "QPushButton:hover{background-color:white;}"
            )
        botao_fechar.clicked.connect(fechar)
        layout.addWidget(botao_fechar)

        # ******* ... *******
        def browser():
            open_new('https://artesgc.home.blog')

        label_copyright = QLabel("<hr><a href='#' style='text-decoration:none;'>&trade;ArtesGC Inc.</a>", self.ferramentas)
        label_copyright.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_copyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        label_copyright.linkActivated.connect(browser)
        layout.addWidget(label_copyright)

        janela_historico_jogadores.setLayout(layout)
        janela_historico_jogadores.show()

    def palavras_secretas(self):
        janela_palavra_secretas = QDialog(self.ferramentas)
        janela_palavra_secretas.setStyleSheet(
            "background-color: cadetblue;"
            "border-radius: 5px;"
            )
        janela_palavra_secretas.setWindowTitle("Palavras Secretas")

        layout = QVBoxLayout()
        layout.setSpacing(10)

        label_intro = QLabel("<b>" + " . " * 5 + "P A L A V R A S - S E C R E T A S" + 5 * " . " + "</b><hr>")
        label_intro.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(label_intro)

        lista_palavras = QListWidget()
        for palavra in sorted(self.PALAVRAS):
            lista_palavras.addItem(palavra)
        lista_palavras.setAlternatingRowColors(True)
        layout.addWidget(lista_palavras)

        label_extra = QLabel(f"<i>{len(self.PALAVRAS)} palavras..</i>")
        label_extra.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_extra.setStyleSheet("color:#D1C399;")
        layout.addWidget(label_extra)

        def fechar():
            # self.tab.removeTab(self.tab.currentIndex())
            janela_palavra_secretas.close()

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setStyleSheet(
            "QPushButton{background-color:red;}"
            "QPushButton:hover{background-color:white;}"
            )
        botao_fechar.clicked.connect(fechar)
        layout.addWidget(botao_fechar)

        # ******* ... *******
        def browser():
            open_new('https://artesgc.home.blog')

        label_copyright = QLabel("<hr><a href='#' style='text-decoration:none;'>&trade;ArtesGC Inc.</a>", self.ferramentas)
        label_copyright.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_copyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        label_copyright.linkActivated.connect(browser)
        layout.addWidget(label_copyright)

        janela_palavra_secretas.setLayout(layout)
        janela_palavra_secretas.show()

    def dados_jogador(self):
        # activar a opção de reiniciar jogo
        self.reiniciar_jogo.setEnabled(True)

        def validar_dados_jogador():
            if self.nome_jogador.text() == "" or self.nome_jogador.text().isspace():
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Nome do jogador não definido..')
            else:
                if self.nivel.currentText() == '3':
                    self.NUMERO_TENTATIVA = 15
                    self.PONTOS = 0
                    self.janela_dados_jogador.close()
                    self.janela_jogo()
                elif self.nivel.currentText() == '2':
                    self.NUMERO_TENTATIVA = 20
                    self.PONTOS = 0
                    self.janela_dados_jogador.close()
                    self.janela_jogo()
                elif self.nivel.currentText() == '1':
                    self.NUMERO_TENTATIVA = 25
                    self.PONTOS = 0
                    self.janela_dados_jogador.close()
                    self.janela_jogo()
                else:
                    QMessageBox.warning(self.ferramentas, 'Aviso', 'Nível não definido..')

        self.janela_dados_jogador = QWidget()
        self.janela_dados_jogador.setStyleSheet(
            "background-color: cadetblue;"
            "border-radius: 5px;"
        )
        layout = QFormLayout()

        label_imagem = QLabel()
        label_imagem.setPixmap(QPixmap("icons/01.png"))
        label_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_imagem.setStyleSheet("margin: auto;")
        layout.addRow(label_imagem)

        label_extra = QLabel("<b>" + " . " * 5 + "D A D O S - D O - J O G A D O R" + " . " * 5 + "</b>")
        # label_extra.setStyleSheet("margin: auto;")
        label_extra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_extra)

        self.nome_jogador = QLineEdit()
        self.nome_jogador.setPlaceholderText("Digite o seu nome..")
        self.nome_jogador.returnPressed.connect(validar_dados_jogador)
        layout.addRow(self.nome_jogador)

        niveis = ['1', '2', '3']
        self.nivel = QComboBox()
        self.nivel.addItems(niveis)
        self.nivel.setToolTip('Nível 1 - 25 tentativas\nNível 2 - 20 tentativas\nNível 3 - 15 tentativas')
        layout.addRow("<b>Selecione o &Nível:</b>", self.nivel)

        botao_jogar = QPushButton("Jogar")
        botao_jogar.setStyleSheet(
            "QPushButton{background-color:green;}"
            "QPushButton:hover{background-color:white;}"
            )
        botao_jogar.clicked.connect(validar_dados_jogador)
        layout.addRow(botao_jogar)

        # ******* ... *******
        def browser():
            open_new('https://artesgc.home.blog')

        label_copyright = QLabel("<hr><a href='#' style='text-decoration:none;'>&trade;ArtesGC Inc.</a>", self.ferramentas)
        label_copyright.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_copyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        label_copyright.linkActivated.connect(browser)
        layout.addWidget(label_copyright)

        self.janela_dados_jogador.setLayout(layout)
        self.layout_principal.addWidget(self.janela_dados_jogador)

    def janela_jogo(self):
        tamanho_lista_palavras = len(self.PALAVRAS)
        seleciona_palavra_aleatoria = self.PALAVRAS[randint(0, tamanho_lista_palavras - 1)]
        agrupa_letras_palavra = ['_' for _ in seleciona_palavra_aleatoria]

        def validar_jogada():
            if self.letra_jogador.text() == "" or self.letra_jogador.text().isspace() or None:
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Letra para tentativa não atribuida..')
            elif not self.letra_jogador.text().isalpha():
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Letra para tentativa não atribuida..')
            else:
                self.JOGADA += 1
                posicao = 0
                if self.letra_jogador.text().upper() in seleciona_palavra_aleatoria:
                    for letra in seleciona_palavra_aleatoria:
                        if self.letra_jogador.text().upper() == letra:
                            self.PONTOS += randint(50, 200)
                            agrupa_letras_palavra[posicao] = self.letra_jogador.text().upper()
                            label_jogo.setText(
                                    f"""Nível: {self.nivel.currentText()} - Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}

(^.^) Obaa..
VOCÊ ACERTOU {self.nome_jogador.text()}!

{agrupa_letras_palavra}

Pontos {self.PONTOS}"""
                            )
                            label_jogo.setStyleSheet(
                                "background-color: white;"
                                "color: blue;"
                                "font-weight: bold;"
                                "border-radius: 3px;"
                                "border-width: 2px;"
                                "border-style: solid;"
                                "border-color: blue;"
                                "padding: 50px;"
                                )
                        posicao += 1
                else:
                    self.PONTOS -= randint(10, 50)
                    label_jogo.setText(
                            f"""Nível: {self.nivel.currentText()} - Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}

(O_O) Upss..
VOCÊ ERROU {self.nome_jogador.text()}!

Pontos {self.PONTOS}"""
                    )
                    label_jogo.setStyleSheet(
                        "background-color: white;"
                        "color: orange;"
                        "font-weight: bold;"
                        "border-radius: 3px;"
                        "border-width: 2px;"
                        "border-style: solid;"
                        "border-color: orange;"
                        "padding:50px;"
                        )

        def validar_vitoria():
            def novo_jogo():
                self.JOGADA = 0
                self.tab.removeTab(self.tab.currentIndex())
                self.janela_jogo()

            completou = '_' not in agrupa_letras_palavra
            if completou:
                label_jogo.setText(
                    f"""(^3^) Parabéns {self.nome_jogador.text()}
VOCÊ GANHOU..

{agrupa_letras_palavra}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
Pontos: {self.PONTOS}"""
                    )
                label_jogo.setStyleSheet(
                    "background-color: white;"
                    "color: green;"
                    "font-weight: bold;"
                    "border-radius: 3px;"
                    "border-width: 2px;"
                    "border-style: solid;"
                    "border-color: green;"
                    "padding: 50px;"
                    )
                botao_valida.setText('Novo Jogo')
                botao_valida.clicked.connect(novo_jogo)
                add_dados(
                    _nome=self.nome_jogador.text(), _pontos=self.PONTOS, _tentativas=self.JOGADA,
                    _nivel=self.nivel.currentText(), _estado='GANHOU'
                    )
            elif self.JOGADA == self.NUMERO_TENTATIVA:
                label_jogo.setText(
                    f"""(T.T) Lamento {self.nome_jogador.text()}
VOCÊ ESGOTOU TODAS AS SUAS TENTATIVAS..

Palavra Secreta: {seleciona_palavra_aleatoria}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
Pontos: {self.PONTOS}"""
                    )
                label_jogo.setStyleSheet(
                    "background-color: white;"
                    "color: red;"
                    "font-weight: bold;"
                    "border-radius: 3px;"
                    "border-width: 2px;"
                    "border-style: solid;"
                    "border-color: red;"
                    "padding: 50px;"
                    )
                botao_valida.setText('Novo Jogo')
                botao_valida.clicked.connect(novo_jogo)
                add_dados(
                    _nome=self.nome_jogador.text(), _pontos=self.PONTOS, _tentativas=self.JOGADA,
                    _nivel=self.nivel.currentText(), _estado='PERDEU'
                    )
            else:
                validar_jogada()

        janela_jogo = QWidget()
        janela_jogo.setStyleSheet(
            "background-color: cadetblue;"
            "border-radius: 5px;"
        )
        layout = QFormLayout()

        label_info = QLabel(
            f"<h1>Bem-Vindo <i>{self.nome_jogador.text()}</i></h1><hr>"
            f"<small style='color:white;'>Tente Adivinhar Qual é a Palavra Secreta:</small><br>"
            f"<b>{agrupa_letras_palavra}</b>"
            )
        label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_info.setStyleSheet("margin: auto;")
        layout.addRow(label_info)

        label_jogo = QLabel('.  .  .  .  .')
        label_jogo.setStyleSheet(
            "font-weight: bold;"
            "background-color: white;"
            "border-radius: 3px;"
            "border-width: 2px;"
            "border-style: solid;"
            "padding: 100px;"
            )
        label_jogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_jogo)

        label_extra = QLabel("<hr><b>" + " . " * 5 + "J O G A N D O" + " . " * 5 + "</b>")
        label_extra.setStyleSheet("margin: auto;")
        label_extra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_extra)

        self.letra_jogador = QLineEdit()
        self.letra_jogador.setMaxLength(1)
        self.letra_jogador.setPlaceholderText("Digite a letra e pressione ENTER..")
        self.letra_jogador.returnPressed.connect(validar_vitoria)
        layout.addRow(self.letra_jogador)

        layoutbotoes = QHBoxLayout()
        botao_valida = QPushButton('Validar a Jogada')
        botao_valida.setDefault(True)
        botao_valida.clicked.connect(validar_vitoria)
        botao_valida.setStyleSheet(
            "QPushButton{background-color:cyan;}"
            "QPushButton:hover{background-color:white;}"
            )
        layoutbotoes.addWidget(botao_valida)

        botao_fim_jogo = QPushButton('Terminar o Jogo')
        botao_fim_jogo.clicked.connect(self._sair)
        botao_fim_jogo.setStyleSheet(
            "QPushButton{background-color:red;}"
            "QPushButton:hover{background-color:white;}"
            )
        layoutbotoes.addWidget(botao_fim_jogo)
        layout.addRow(layoutbotoes)

        # ******* ... *******
        def browser():
            open_new('https://artesgc.home.blog')

        label_copyright = QLabel("<hr><a href='#' style='text-decoration:none;'>&trade;ArtesGC Inc.</a>", self.ferramentas)
        label_copyright.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_copyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        label_copyright.linkActivated.connect(browser)
        layout.addWidget(label_copyright)

        janela_jogo.setLayout(layout)
        self.layout_principal.addWidget(janela_jogo)
