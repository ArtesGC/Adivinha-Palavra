import webbrowser
from random import randint
from sys import argv, exit
from time import sleep
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *
from PyQt6.QtWidgets import *
from history import add_dados, criar_tabela_jogo, apagar_historico
from words import Palavras


class J3A7P6:
    def __init__(self):
        # instancia principal da aplicação
        self.gc = QApplication(argv)

        # fonte do programa
        QFontDatabase.addApplicationFont('fonts/megrim.ttf')

        # ferramenta principal da aplicação
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle("Adivinha Palavra")
        self.ferramentas.setStyleSheet(theme)
        self.ferramentas.setWindowIcon(QIcon("img/icons/favicon-192x192.png"))
        self.ferramentas.setFixedSize(650, 600)

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
        palavra_secretas.triggered.connect(self._palavras_secretas)
        opcoes.addSeparator()

        histor = opcoes.addAction("Historico de Jogadores")
        histor.triggered.connect(self._historico)
        opcoes.addSeparator()

        sair = opcoes.addAction("Sair")
        sair.triggered.connect(self._sair)

        sobre = menu_ferramentas.addAction("Sobre")
        sobre.triggered.connect(self._sobre)

        # layout principal da aplicação
        layout_principal = QVBoxLayout()
        layout_principal.setMenuBar(menu_ferramentas)

        # ******* criando abas para melhor organização *******
        self.tab = QTabWidget()
        self.tab.setTabShape(self.tab.TabShape.Triangular)
        self.tab.setDocumentMode(True)
        self.tab.setTabBarAutoHide(True)
        layout_principal.addWidget(self.tab)

        # ******* ... *******
        def browser():
            webbrowser.open('https://artesgc.home.blog')

        label_copyright = QLabel("<hr><a href='#' style='text-decoration:none;'>&trade;ArtesGC Inc.</a>",
                                 self.ferramentas)
        label_copyright.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_copyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        label_copyright.linkActivated.connect(browser)
        layout_principal.addWidget(label_copyright)
        self.ferramentas.setLayout(layout_principal)

        # ******* variáveis globais *******
        self.janela_dados_jogador = None
        self.janela_palavra_secretas = None
        self.janela_historico_jogadores = None
        self.nome_jogador = None
        self.nivel = None
        self.letra_jogador = None

        # constantes globais
        self.NUMERO_TENTATIVA = 0
        self.PONTOS = 0
        self.JOGADA = 0
        self.PALAVRAS = Palavras().listadas()

        # inicialização do programa
        self.janela_principal()

    # optimização para abertura das janelas
    def _historico(self):
        """
        abrir a janela do historico de jogadores sem duplicacoes
        ou retorno de valores nulos
        """
        if self.janela_historico_jogadores is None:
            self.historico_jogadores()
        else:
            try:
                self.tab.addTab(self.janela_historico_jogadores, 'Historico')
                self.tab.setCurrentWidget(self.janela_historico_jogadores)
            except Exception:
                self.tab.removeTab(1)
                self.historico_jogadores()

    def _reiniciar_jogo(self):
        """
        reiniciar o jogo, ie, apartir da janela de introducao de dados
        """
        if self.janela_dados_jogador is None:
            self.dados_jogador()
        else:
            try:
                self.tab.removeTab(0)
                self.tab.addTab(self.janela_dados_jogador, 'Jogador')
                self.tab.setCurrentWidget(self.janela_dados_jogador)
            except Exception:
                self.tab.removeTab(0)
                self.dados_jogador()

    def _palavras_secretas(self):
        """
        abrir a janela com as possiveis palavras secretas sem duplicacoes
        ou retorno de valores nulos
        """
        if self.janela_palavra_secretas is None:
            self.palavras_secretas()
        else:
            try:
                self.tab.addTab(self.janela_palavra_secretas, 'Palavras Secretas')
                self.tab.setCurrentWidget(self.janela_palavra_secretas)
            except Exception:
                self.tab.removeTab(1)
                self.palavras_secretas()

    # funções do menu
    def _instr(self):
        janelainfo = QDialog(self.ferramentas)
        janelainfo.setWindowTitle('Instruções')

        layout = QVBoxLayout()
        layout.setSpacing(20)

        info_prog = QLabel("""
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
<a href="https://artesgc.home.blog" style="text-decoration:none;"><b>&trade;ArtesGC Inc</b></a>""")
        info_prog.setStyleSheet("border-style:solid;"
                                "border-color:black;"
                                "border-width:1px;"
                                "border-radius:3px;"
                                "background-color:white;"
                                "padding:10px;")
        layout.addWidget(info_prog)

        def fechar():
            janelainfo.close()

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setStyleSheet('background-color:red;')
        botao_fechar.clicked.connect(fechar)
        layout.addWidget(botao_fechar)

        janelainfo.setLayout(layout)
        janelainfo.show()

    def _sobre(self):
        janelainfo = QDialog(self.ferramentas)
        janelainfo.setWindowTitle('Sobre')

        layout = QVBoxLayout()
        layout.setSpacing(20)

        info_prog = QLabel("""
Nome: <b>Jogo Adivinha Palavra</b><br>
Versão: <b>0.8-092021</b><br>
Designers e Programadores: 
<a href="https://github.com/Nurul-GC" style="text-decoration:none;"><b>Nurul GC</b></a>, 
<a href="https://github.com/Paulo-Lopes-Estevao" style="text-decoration:none;"><b>Paulo Lopes Estevão</b></a><br>
Empresa: <a href="https://artesgc.home.blog" style="text-decoration:none;"><b>&trade;ArtesGC Inc</b></a>""")
        info_prog.setStyleSheet("border-style:solid;"
                                "border-color:black;"
                                "border-width:1px;"
                                "border-radius:3px;"
                                "background-color:white;"
                                "padding:10px;")
        layout.addWidget(info_prog)

        def fechar():
            janelainfo.close()

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setStyleSheet('background-color:red;')
        botao_fechar.clicked.connect(fechar)
        layout.addWidget(botao_fechar)

        janelainfo.setLayout(layout)
        janelainfo.show()

    def _sair(self):
        sair = QMessageBox.question(
            self.ferramentas, "Sair", "Tem mesmo a certeza que deseja terminar o jogo?")
        if sair == QMessageBox.StandardButton.Yes:
            exit(0)
        else:
            pass

    # janelas do programa
    def janela_principal(self):
        janela01 = QWidget()
        layout = QVBoxLayout()

        label_imagem = QLabel()
        label_imagem.setPixmap(QPixmap("img/icons/favicon-512x512.png"))
        label_imagem.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(label_imagem)

        barra_progresso = QProgressBar()
        barra_progresso.setGeometry(200, 100, 200, 30)
        barra_progresso.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(barra_progresso)

        def processar():
            n = randint(3, 5)
            sec = 0.2
            for i in range(0, 101, n):
                sleep(sec)
                barra_progresso.setValue(i)
            self.tab.removeTab(self.tab.currentIndex())
            self.dados_jogador()

        botao_iniciar = QPushButton("Iniciar Jogo")
        botao_iniciar.setStyleSheet("QPushButton{background-color:#D1C399;}"
                                    "QPushButton:hover{background-color:white;}")
        botao_iniciar.clicked.connect(processar)
        layout.addWidget(botao_iniciar)

        janela01.setLayout(layout)
        self.tab.addTab(janela01, "Bem-Vindo")
        self.tab.setCurrentWidget(janela01)

    def historico_jogadores(self):
        def inciar_model(_model):
            _model.setTable('tb_jogo')
            _model.select()
            _model.setHeaderData(0, Qt.Orientation.Horizontal, "id")
            _model.setHeaderData(1, Qt.Orientation.Horizontal, "nome")
            _model.setHeaderData(2, Qt.Orientation.Horizontal, "pontos")
            _model.setHeaderData(3, Qt.Orientation.Horizontal, "tentativas")
            _model.setHeaderData(4, Qt.Orientation.Horizontal, "nivel")

        def conectar_db():
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('historico/ap.db')

        def zerar_db():
            apagar_historico()
            QMessageBox.information(self.ferramentas, 'Operação bem sucedida',
                                    f'Operação concluida, os dados serão atualizados automaticamente após o reinício '
                                    f'do programa..')
            return fechar()

        def fechar():
            self.tab.removeTab(self.tab.currentIndex())

        self.janela_historico_jogadores = QWidget()
        layout = QVBoxLayout()

        conectar_db()
        model = QSqlTableModel()
        inciar_model(model)

        label_intro = QLabel("<b>" + ".  . " * 5 + "H I S T O R I C O" + 5 * " .  ." + "</b><hr>")
        label_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_intro)

        view = QTableView()
        view.setFixedWidth(600)
        view.setAlternatingRowColors(True)
        view.setModel(model)
        layout.addWidget(view, alignment=Qt.AlignmentFlag.AlignHCenter)

        botao_zerar = QPushButton("Zerar Historico")
        botao_zerar.setStyleSheet("QPushButton{background-color:cyan;}"
                                  "QPushButton:hover{background-color:white;}")
        botao_zerar.clicked.connect(zerar_db)
        layout.addWidget(botao_zerar)

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setStyleSheet("QPushButton{background-color:red;}"
                                   "QPushButton:hover{background-color:white;}")
        botao_fechar.clicked.connect(fechar)
        layout.addWidget(botao_fechar)

        self.janela_historico_jogadores.setLayout(layout)
        self.tab.addTab(self.janela_historico_jogadores, 'Historico')
        self.tab.setCurrentWidget(self.janela_historico_jogadores)

    def dados_jogador(self):
        # activar a opção de reiniciar jogo
        self.reiniciar_jogo.setEnabled(True)
        QMessageBox.information(self.ferramentas, "Atenção",
                                "Para uma melhor experiência de jogo leia as instruções que se encontram na barra de "
                                "menu.. "
                                "\n\nObrigado pelo apoio! - ArtesGC")

        def validar_dados_jogador():
            if self.nome_jogador.text() == "" or self.nome_jogador.text().isspace():
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Nome do jogador não definido..')
            else:
                if self.nivel.currentText() == '3':
                    self.NUMERO_TENTATIVA = 15
                    self.PONTOS = 0
                    self.tab.removeTab(self.tab.currentIndex())
                    self.janela_jogo()
                elif self.nivel.currentText() == '2':
                    self.NUMERO_TENTATIVA = 20
                    self.PONTOS = 0
                    self.tab.removeTab(self.tab.currentIndex())
                    self.janela_jogo()
                elif self.nivel.currentText() == '1':
                    self.NUMERO_TENTATIVA = 25
                    self.PONTOS = 0
                    self.tab.removeTab(self.tab.currentIndex())
                    self.janela_jogo()
                else:
                    QMessageBox.warning(self.ferramentas, 'Aviso', 'Nível não definido..')

        self.janela_dados_jogador = QWidget()
        layout = QFormLayout()
        layout.setSpacing(10)

        label_imagem = QLabel()
        label_imagem.setPixmap(QPixmap("img/01.png"))
        label_imagem.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addRow(label_imagem)

        label_extra = QLabel("<b>" + ".  . " * 5 + "D A D O S - D O - J O G A D O R" + " .  ." * 5 + "</b><hr>")
        label_extra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_extra)

        self.nome_jogador = QLineEdit()
        self.nome_jogador.setPlaceholderText("Digite o seu nome..")
        layout.addRow(self.nome_jogador)

        niveis = ['1', '2', '3']
        self.nivel = QComboBox()
        self.nivel.addItems(niveis)
        self.nivel.setToolTip('Nível 1 - 25 tentativas\nNível 2 - 20 tentativas\nNível 3 - 15 tentativas')
        layout.addRow("<b>Selecione o &Nível:</b>", self.nivel)

        botao_jogar = QPushButton("Jogar")
        botao_jogar.setStyleSheet("QPushButton{background-color:green;}"
                                  "QPushButton:hover{background-color:white;}")
        botao_jogar.clicked.connect(validar_dados_jogador)
        layout.addRow(botao_jogar)

        self.janela_dados_jogador.setLayout(layout)
        self.tab.addTab(self.janela_dados_jogador, 'Jogador')
        self.tab.setCurrentWidget(self.janela_dados_jogador)

    def janela_jogo(self):
        tamanho_lista_palavras = len(self.PALAVRAS)
        seleciona_palavra_aleatoria = self.PALAVRAS[randint(0, tamanho_lista_palavras - 1)]
        agrupa_letras_palavra = ['_' for _ in seleciona_palavra_aleatoria]

        def valida_jogada():
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

Pontos {self.PONTOS}""")
                            label_jogo.setStyleSheet("background-color:white; "
                                                     "color:blue; "
                                                     "border-radius: 3px; "
                                                     "border: 2px solid; "
                                                     "padding:50px;")
                        posicao += 1
                else:
                    self.PONTOS -= randint(10, 50)
                    label_jogo.setText(
                        f"""Nível: {self.nivel.currentText()} - Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}

(O_O) Upss..
VOCÊ ERROU {self.nome_jogador.text()}!

Pontos {self.PONTOS}""")
                    label_jogo.setStyleSheet("background-color:white; "
                                             "color:red; "
                                             "border-radius: 3px; "
                                             "border: 2px solid; "
                                             "padding:50px;")

        def valida_vitoria():
            def novo_jogo():
                self.JOGADA = 0
                self.tab.removeTab(self.tab.currentIndex())
                self.janela_jogo()

            completou = '_' not in agrupa_letras_palavra
            if completou:
                label_jogo.setText(f"""(^3^) Parabéns {self.nome_jogador.text()}
VOCÊ GANHOU..

{agrupa_letras_palavra}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
Pontos: {self.PONTOS}""")
                label_jogo.setStyleSheet("background-color:white; "
                                         "color:green; "
                                         "border-radius: 3px; "
                                         "border: 2px solid; "
                                         "padding:50px;")
                botao_valida.setText('Novo Jogo')
                botao_valida.clicked.connect(novo_jogo)
                add_dados(_nome=self.nome_jogador.text(), _pontos=self.PONTOS, _tentativas=self.JOGADA,
                          _nivel=self.nivel.currentText(), _estado='GANHOU')
            elif self.JOGADA == self.NUMERO_TENTATIVA:
                label_jogo.setText(f"""(T.T) Lamento {self.nome_jogador.text()}
VOCÊ ESGOTOU TODAS AS SUAS TENTATIVAS..

Palavra Secreta: {seleciona_palavra_aleatoria}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
Pontos: {self.PONTOS}""")
                label_jogo.setStyleSheet("background-color:white; "
                                         "color:red; "
                                         "border-radius: 3px; "
                                         "border: 2px solid; "
                                         "padding:50px;")
                botao_valida.setText('Novo Jogo')
                botao_valida.clicked.connect(novo_jogo)
                add_dados(_nome=self.nome_jogador.text(), _pontos=self.PONTOS, _tentativas=self.JOGADA,
                          _nivel=self.nivel.currentText(), _estado='PERDEU')
            else:
                valida_jogada()

        janela03 = QWidget()
        layout = QFormLayout()
        layout.setSpacing(20)

        label_info = QLabel(f"<h3>Bem-Vindo <i>{self.nome_jogador.text()}</i><br>"
                            f"Tente Adivinhar Qual é a Palavra Secreta</h3><hr>"
                            f"<b>{agrupa_letras_palavra}</b>")
        label_info.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addRow(label_info)

        label_jogo = QLabel('.  .  .  .  .')
        label_jogo.setStyleSheet("background-color: white; "
                                 "border-radius: 3px; "
                                 "border: 2px solid; "
                                 "padding:100px;")
        label_jogo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addRow(label_jogo)

        label_extra = QLabel("<b>" + ".  . " * 5 + "J O G A N D O" + " .  ." * 5 + "</b><hr>")
        label_extra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_extra)

        self.letra_jogador = QLineEdit()
        self.letra_jogador.setMaxLength(1)
        self.letra_jogador.setPlaceholderText("Digite a letra e pressione ENTER..")
        self.letra_jogador.returnPressed.connect(valida_vitoria)
        layout.addRow(self.letra_jogador)

        botao_valida = QPushButton('Validar Jogada')
        botao_valida.setDefault(True)
        botao_valida.clicked.connect(valida_vitoria)
        botao_valida.setStyleSheet("QPushButton{background-color:cyan;}"
                                   "QPushButton:hover{background-color:white;}")

        botao_fim_jogo = QPushButton('Terminar o Jogo')
        botao_fim_jogo.clicked.connect(self._sair)
        botao_fim_jogo.setStyleSheet("QPushButton{background-color:red;}"
                                     "QPushButton:hover{background-color:white;}")
        layout.addRow(botao_valida, botao_fim_jogo)

        janela03.setLayout(layout)
        self.tab.addTab(janela03, 'Jogando')
        self.tab.setCurrentWidget(janela03)

    def palavras_secretas(self):
        self.janela_palavra_secretas = QWidget()
        layout = QVBoxLayout()

        label_intro = QLabel("<b>" + ".  . " * 5 + "P A L A V R A S - S E C R E T A S" + 5 * " .  ." + "</b><hr>")
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

        def fechar(): return self.tab.removeTab(self.tab.currentIndex())

        botao_fechar = QPushButton("Fechar")
        botao_fechar.setStyleSheet("QPushButton{background-color:red;}"
                                   "QPushButton:hover{background-color:white;}")
        botao_fechar.clicked.connect(fechar)
        layout.addWidget(botao_fechar)

        self.janela_palavra_secretas.setLayout(layout)
        self.tab.addTab(self.janela_palavra_secretas, 'Palavras Secretas')
        self.tab.setCurrentWidget(self.janela_palavra_secretas)


if __name__ == '__main__':
    theme = open('themes/ap.qss').read().strip()
    criar_tabela_jogo()
    app = J3A7P6()
    app.ferramentas.show()
    app.gc.exec()
