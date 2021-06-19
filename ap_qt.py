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
from sys import argv, exit
from time import sleep
from random import randint
import webbrowser

__nome__ = "Jogo Adivinha Palavra"
__version__ = "0.5-032021"
__copyright__ = "© 2019-2021 Nurul-GC"
__trademark__ = "™ ArtesGC"


class J3A7P6:
    def __init__(self):
        self.gc = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle("Adivinha Palavra")
        self.ferramentas.setStyleSheet('background-color:cadetblue; font-family:consolas; font-size:10pt;')
        self.ferramentas.setWindowIcon(QIcon("img/adivinhapalavra-icon.png"))
        self.ferramentas.setFixedSize(600, 550)

        # ******* criando abas para melhor organização *******
        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 30, 600, 520)

        # ******* lista de palavras *******
        self.palavras = ['ATENCIOSO', 'AGRADAVEL', 'ADORAVEL', 'AMAVEL', 'AFAVEL', 'AMIGAVEL', 'AMOROSO', 'AUTENTICO', 'APIXONADO', 'ANIMADO', 'ALEGRE', 'AMISTOSO', 'AMIGO',
                         'AFETIVO', 'AFETUOSO', 'ACOLHEDOR', 'APRAZIVEL', 'ATRAENTE', 'ATRATIVO', 'AUDAZ', 'AVENTUREIRO', 'ARROJADO', 'AUSPICIOSO', 'APLICADO', 'ALTRUISTA', 'ASSERTIVO', 'ATENTO',
                         'AGIL', 'APTO', 'ATILADO', 'ASTUTO', 'ARGUTO', 'AJUIZADO', 'ASSOMBROSO', 'ADMIRAVEL', 'AIROSO', 'ADONISAFORTUNADO', 'ACAUTELADO', 'ANGELICAL', 'ABERTO', 'ACESSIVEL',
                         'BOM', 'BONDOSO', 'BONITO', 'BELO', 'BACANA', 'BENDITO', 'BATALHADOR', 'BASEADO', 'BENEMERITO', 'BENFEITOR', 'BENEVOLO', 'BENEVOLENTE', 'BRILHANTE', 'BRIOSO', 'BRINCALHAO',
                         'BOMBASTICO', 'BELEZA', 'BELDADE', 'BENEFICO', 'BENIGNO', 'BENFAZEJO', 'BENQUISTO', 'CALMO', 'CALOROSO', 'CAMARADA', 'CANDIDO', 'CAPAZ', 'CARIDOSO', 'CARINHOSO', 'CARISMATICO',
                         'CARITATIVO', 'CATIVANTE', 'CAUTELOSO', 'CAVALHEIRO', 'CELESTIAL', 'CENTRADO', 'CHARMOSO', 'CHEIROSO', 'CHIQUE', 'CHISTOSO', 'CIENTE', 'CIRCUNSPECTO', 'CIVICO', 'CIVIL',
                         'CIVILIZADO', 'CLARIVIDENTE', 'CLEMENTE', 'COERENTE', 'COLABORADOR', 'COLEGA', 'COMEDIDO', 'COMPANHEIRO', 'COMPASSIVO', 'COMPETENTE', 'COMPLACENTE', 'COMPORTADO',
                         'COMPREENSIVO', 'CONFIANTE', 'CONFIAVEL', 'CONFIDENTE, CONHECEDOR', 'CONSCIENCIOSO', 'CONSCIENTE', 'CONTENTE', 'CONVICTO', 'COOPERADOR', 'CORAJOSO', 'CORDIAL',
                         'CORRECTO', 'CORTES', 'CRANIO', 'CREDIVEL', 'CRESCIDO', 'CRIATIVO', 'CRITERIOSO', 'CRIVEL', 'CUIDADOSO', 'CULTO', 'DIVERTIDO', 'DEDICADO', 'DECENTE', 'DIGNO', 'DECOROSO',
                         'DECIDIDO', 'DEFERENTE', 'DELICADO', 'DESTEMIDO', 'DENODADO', 'DADO', 'DOCE', 'DOCIL', 'DISTINTO', 'DIREITO', 'DADIVOSO', 'DOTADO', 'DISPONIVEL', 'DINAMICO', 'DILIGENTE',
                         'DONAIROSO', 'DISPOSTO',
                         'DISCRETO', 'DIPLOMATICO', 'DISCIPLINADO', 'DIRETO', 'DILETO', 'DEVOTO', 'DEVANEADOR', 'DEUS', 'DESLUMBRANTE', 'DESEJAVEL', 'DESENVOLVIDO',
                         'DESENRASCADO', 'DESENROLADO',
                         'EDUCADO', 'EFICIENTE', 'EFUSIVO', 'ELEGANTE', 'ELOQUENTE', 'EMANCIPADO', 'EMINENTE', 'EMPATICO', 'EMPENHADO', 'EMPOLGADO', 'EMPREENDEDOR', 'ENCANTADOR', 'ENCORAJADOR',
                         'ENGENHOSO', 'ENGRACADO',
                         'ENTENDIDO', 'ENTUSIASMADO', 'ENTUSIASTA', 'EQUILIBRADO', 'ESBELTO', 'ESCLARECIDO', 'ESCRUPULOSO', 'ESFORCADO', 'ESMERADO', 'ESPANTOSO', 'ESPECIAL', 'ESPECIALISTA',
                         'ESPERACOSO', 'ESPERTO', 'ESPETACULAR',
                         'ESPIRITUOSO', 'ESPLENDIDO', 'ESPLENDOROSO', 'ESPONTANEO', 'ESTONTEANTE', 'ETERNO', 'EVOLUIDO', 'ESCELENTE', 'EXCELSO', 'EXEMPLAR', 'EXIMIO', 'EXPERIENTE', 'EXTRAORDINARIO',
                         'EXTROVERTIDO', 'EXTREMOSO',
                         'EXUBERANTE', 'EXULTANTE', 'FIEL', 'FORTE', 'FRANCO', 'FRONTAL', 'FIRME', 'FANTASTICO', 'FENOMENAL', 'FABULOSO', 'FASCINANTE', 'FORMIDAVEL', 'FIDEDIGNO', 'FORMOSO', 'FOFO',
                         'FELIZ', 'FELIZARDO', 'FACEIRO',
                         'FERVOROSO', 'GENTIL', 'GENEROSO', 'GENUINO', 'GRACIOSO', 'GRANDE', 'GRANDIOSO', 'GENIO', 'GENIAL', 'GALANTE', 'GATO', 'GOSTOSO', 'GLORIOSO', 'GLAMOROSO', 'GIGANTE',
                         'GIGANTESCO', 'GUERREIRO', 'GANATEADOR',
                         'GRATO', 'HONESTO', 'HONRADO', 'HUMANO', 'HONROSO', 'HONORAVEL', 'HEROI', 'HEROICO', 'HABIL', 'HABILIDOSO', 'HILARIO', 'HILARIANTE', 'HOSPITALEIRO', 'HUMANITARIO',
                         'HOSPEDEIRO', 'HUMILDE',
                         'HUMILDOSO', 'INTELIGENTE', 'IMPORTANTE', 'INTEGRO', 'INCRIVEL', 'ILUSTRE', 'INTERESSANTE', 'IMPRESSIONANTE', 'IMPAR', 'IDEAL', 'IMPONENTE', 'IMAGINATIVO', 'IMPECAVEL',
                         'IRREVERENTE', 'IRRESISTIVEL',
                         'INIGUALAVEL', 'IMPARCIAL', 'IDONEO', 'INDEPENDENTE', 'INSPIRADOR', 'INTERVENTIVO', 'INTUITIVO', 'INTENSO', 'INTELECTUAL', 'INSTRUIDO', 'IMORTAL', 'IMPAVIDO', 'ILUMINADO',
                         'IMACULADO', 'IDEALISTA',
                         'IMPARAVEL', 'INABALAVEL', 'INCANSAVEL', 'IMBATIVEL', 'INVENCIVEL', 'INSUBMISSO', 'INSUBORNAVEL', 'INVULNERAVEL', 'INCURRUPTIVEL', 'INCORRUPTO', 'IMPRESCINDIVEL',
                         'INDISPENSAVEL', 'JUSTO', 'JOVEM',
                         'JOVIAL', 'JOIA', 'JEITOSO', 'JUBILANTE', 'JUBILOSO', 'JANOTA', 'JUSTICEIRO', 'LEAL', 'LEGAL', 'LINDO', 'LIVRE', 'LUTADOR', 'LOUVAVEL', 'LAUDAVEL', 'LARGO', 'LEGITIMO',
                         'LUCIDO', 'LISONJEIRO', 'LIBERAL', 'LIBERTO',
                         'LICITO', 'LIDER', 'LETRADO', 'LABORIOSO', 'MARAVILHOSO', 'MAGNIFICO', 'MAGNANIMO', 'MAJESTOSO', 'MAGNIFICENTE', 'MAIOR', 'MELHOR', 'MAXIMO', 'MERECEDOR', 'MANEIRO', 'MEIGO',
                         'MIMOSO', 'MODESTO', 'MODICO',
                         'MATERNAL', 'MAVIOSO', 'MOTIVADO', 'MARCANTE', 'MAGICO', 'MAGNO', 'MAGISTRAL', 'MAESTRAL', 'MERITORIO', 'MODERNO', 'MODERADO', 'MADURO', 'METICULOSO', 'MINUCIOSO', 'METODICO',
                         'MIRABOLANTE',
                         'NOTAVEL', 'NOBRE', 'NORMAL', 'NATURAL', 'NOVO', 'NATURISTA', 'NUTRIDO', 'OBEDIENTE', 'OBJECTIVO', 'OBSEQUISO', 'OBSERVADOR', 'OBSTINADO', 'OFICIOSO', 'ONIPOTENTE',
                         'ONISCIENTE', 'OPERANTE', 'OPORTUNO',
                         'ORDEIRO', 'ORGANIZADO', 'ORIGINAL', 'OTIMISTA', 'OTIMO', 'OUSADO', 'PACATO', 'PACIENTE', 'PACIFICADOR', 'PACIFICO', 'PARCEIRO', 'PARCIMONIOSO', 'PERFEITO', 'PERITO',
                         'PERSEVERANTE',
                         'PERSISTENTE', 'PERSPICAZ', 'PERTINAZ', 'PIEDOSO', 'PIONEIRO', 'PODEROSO', 'POLIDO', 'PONDERADO', 'PONTUAL', 'PORREIRO', 'PORRETA', 'POSSANTE', 'PRAZENTEIRO', 'PREPARADO',
                         'PRESTATIVO', 'PRESTAVEL',
                         'PRESTIGIOSO', 'PREVENIDO', 'PRIMOROSO', 'PRINCIPE', 'PRODIGIO', 'PRODIGIOSO', 'PROEMINENTE', 'PROEFICIENTE', 'PROTECTOR', 'PROVECTOPRUDENTE', 'PUJANTE', 'PURO', 'QUERIDO',
                         'QUALIFICADO',
                         'QUENTE',
                         'RESPONSAVEL', 'RESPEITAVEL', 'RESPEITADOR', 'RESPEITADO', 'RESPEITOSO', 'REALIZADO', 'RENOMADO', 'RESISTENTE', 'RESOLUTO', 'RESOLVIDO', 'RESILIENTE', 'ROBUSTO', 'ROMANTICO',
                         'RISONHO', 'RADIANTE',
                         'RESPLANDECENTE', 'RELUZENTE', 'REFINADO', 'RACIONAL', 'REALISTA', 'REFLETIDO', 'RELAXADO', 'RECEPTIVO', 'RECONHECIDO', 'RAPIDO', 'RAZOAVEL', 'SIMPATICO', 'SABIO', 'SINCERO',
                         'SENSATO', 'SENSACIONAL',
                         'SEGURO', 'SORRIDENTE', 'SOSSEGADO', 'SUBLIME', 'SOLICITO', 'SOLIDARIO', 'SERENO', 'SENSIVEL', 'SEDUTOR', 'SAGAZ', 'SAUDAVEL', 'SINGULAR', 'SOCIAVEL', 'SOFISTICADO', 'SERIO',
                         'SONHADOR', 'SANTO', 'SENTIMENTAL',
                         'SABEDOR', 'SUTIL', 'TALENTOSO', 'TERNURENTO', 'TERNO', 'TRANQUILO', 'TRANSPARENTE', 'TOLERANTE', 'TRABALHADOR', 'TENAZ', 'TREMENDO', 'TRANSCENDENTE', 'TRANSCENDENTAL',
                         'TOCANTE', 'TRIUNFANTE',
                         'TRIUNFADOR', 'TRIUNFAL', 'TITANICO', 'TRAQUEJADO', 'TENRO', 'TRANSIGENTE', 'TEMPERANTE', 'TRATAVEL', 'TOLERAVEL', 'TENTADOR', 'TRANQUILIZANTE', 'UNICO', 'UNO', 'URBANO',
                         'UNIFICADOR', 'ULTRAFANTASTICO',
                         'ULTRACOMPETENTE', 'ULTRACONFIANTE', 'ULTRACORRECTO', 'ULTRAINDEPENDENTE', 'ULTRANATURAL', 'ULTRARROMANTICO', 'ULTRACIVILIZADO', 'ULTRADIVINO', 'ULTRAMODERNO',
                         'ULTRARRACIONAL', 'VERDADEIRO', 'VALENTE', 'VALIOSO', 'VALOROSO', 'VENCEDOR', 'VERIDICO', 'VENERAVEL', 'VENTUROSO', 'VISTOSO', 'VIRTUOSO', 'VERSADO', 'VERSATIL',
                         'VISIONARIO', 'VITORIOSO', 'VEEMENTE', 'VENERADO', 'VANGUARDISTA', 'VALIDO', 'VELOZ', 'VIRIL', 'VARONIL', 'VERAZ', 'VERBOSO', 'VIBRANTE', 'VIGOROSO', 'VERDEJANTE', 'VIVIDO',
                         'VIVO', 'VIVAZ', 'VITAL', 'VIGILANTE',
                         'VULTOSO', 'ZELOSO', 'ZELADOR', 'ZELANTE']

        # ******* variáveis *******
        self.janela02 = None
        self.janela03 = None
        self.janela04 = None
        self.nomeJogador = None
        self.nivel = None
        self.letraJogador = None
        self.tentativas = 0
        self.pontos = 0
        self.jogada = 0

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

        sair = opcoes.addAction("Sair")
        sair.triggered.connect(self._sair)

        sobre = menuFerramentas.addAction("Sobre")
        sobre.triggered.connect(self._sobre)

        self.janelaPrincipal()

    def _reiniciarJogo(self):
        if self.janela02 is None:
            return self.dadosJogador()
        try:
            self.tab.setCurrentWidget(self.janela02)
        except Exception as e:
            self.tab.removeTab(0)
            return self.dadosJogador()
        else:
            self.tab.removeTab(0)
            return self.dadosJogador()

    def _palavrasSecretas(self):
        if self.janela04 is None:
            return self.palavrasSecretas()
        try:
            self.tab.setCurrentWidget(self.janela04)
        except Exception as e:
            self.tab.removeTab(1)
            return self.palavrasSecretas()
        else:
            self.tab.removeTab(1)
            return self.palavrasSecretas()

    def _instr(self):
        QMessageBox.information(self.ferramentas, 'Instruções', """
Olá Que a Paz e Bençãos de Deus Estejam Sobre Ti e Toda Tua Família..
Este Jogo Consiste em Ganhar o Máximo de Pontos Possiveis em Poucas Tentativas,
acertando Que Palavra Foi Definida (LETRA POR LETRA)..

Para uma melhor experiência de jogo:
- Conte quantas letras tem a suposta palavra
- identificada pelos simbolos '_' (referem-se as letras da palavra)
- e use a lista de palavras que estão escondidas no menu de opções (Palavras Secretas)
- Use as como referência para as suas tentativas!

Que Deus Te Ilumine Nessa Aventura!

Dica:
Códigos de Honra;

Muito Obrigado pelo apoio!
© 2019-2021 Nurul GC
™ ArtesGC Inc
""")

    def _sobre(self):
        QMessageBox.information(self.ferramentas, 'Sobre', '''
Nome: Jogo Adivinha Palavra
Versão: 0.6-052021
Designer e Programador: Nurul GC
Empresa: ArtesGC Inc.
''')

    def _sair(self):
        sair = QMessageBox.question(self.ferramentas, "Sair", "Tem mesmo a certeza que deseja sair?")
        if sair == QMessageBox.Yes:
            exit(0)
        else:
            pass

    def janelaPrincipal(self):
        janela01 = QWidget()
        layout = QVBoxLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/adivinhapalavra-logo.png").scaled(QSize(570, 400)))
        labelImagem.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelImagem)

        barraProgresso = QProgressBar()
        barraProgresso.setGeometry(200, 100, 200, 30)
        barraProgresso.setAlignment(Qt.AlignHCenter)
        barraProgresso.setStyleSheet("border: 1px solid; border-radius: 3px;")
        layout.addWidget(barraProgresso)

        def processar():
            n = randint(1, 5)
            sec = 0.5
            if n < 3:
                sec = 0.1
            for i in range(0, 101, n):
                sleep(sec)
                barraProgresso.setValue(i)
            self.tab.removeTab(0)
            self.dadosJogador()

        botaoIniciar = QPushButton("Iniciar Jogo")
        botaoIniciar.setStyleSheet("background-color:#D1C399;padding:50px;")
        botaoIniciar.clicked.connect(processar)
        layout.addWidget(botaoIniciar)

        janela01.setLayout(layout)
        self.tab.addTab(janela01, "Bem-Vindo")
        self.tab.setCurrentWidget(janela01)

    def dadosJogador(self):
        # activar a opção de reiniciar jogo
        self.reiniciarJogo.setEnabled(True)

        def jogo():
            if self.nomeJogador.text() == "" or self.nomeJogador.text().isspace() or None:
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Nome do jogador não definido..')
            else:
                if self.nivel.currentText() == '3':
                    self.tentativas = 15
                    self.pontos = 0
                    self.tab.removeTab(0)
                    self.jogo()
                elif self.nivel.currentText() == '2':
                    self.tentativas = 20
                    self.pontos = 0
                    self.tab.removeTab(0)
                    self.jogo()
                elif self.nivel.currentText() == '1':
                    self.tentativas = 25
                    self.pontos = 0
                    self.tab.removeTab(0)
                    self.jogo()
                else:
                    QMessageBox.warning(self.ferramentas, 'Aviso', 'Nível não definido..')

        QMessageBox.information(self.ferramentas, "Atenção", "Para uma melhor experiência de jogo leia as instruções que se encontram na barra de menu.."
                                                             "\nObrigado pelo apoio! - ArtesGC")
        self.janela02 = QWidget()
        layout = QFormLayout()
        layout.setVerticalSpacing(30)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/03.png"))
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
        botaoJogar.setStyleSheet("background-color:green;padding:10px;")
        botaoJogar.clicked.connect(jogo)
        layout.addRow(botaoJogar)

        browser = lambda p: webbrowser.open('https://artesgc.home.blog')
        labelCopyright = QLabel("<a href='#' style='text-decoration:none;'>ArtesGC Inc.</a>")
        labelCopyright.setAlignment(Qt.AlignRight)
        labelCopyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        labelCopyright.linkActivated.connect(browser)
        layout.addWidget(labelCopyright)

        self.janela02.setLayout(layout)
        self.tab.addTab(self.janela02, "Jogador")
        self.tab.setCurrentWidget(self.janela02)

    def jogo(self):
        tamanhoListaPalavras = len(self.palavras)
        selecionaPalavraAleatoria = self.palavras[randint(0, tamanhoListaPalavras - 1)]
        agrupaLetrasPalavra = ['_' for letra in selecionaPalavraAleatoria]

        def validaJogada():
            if self.letraJogador.text() == "" or self.letraJogador.text().isspace() or None:
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Letra para tentativa não atribuida..')
            elif not self.letraJogador.text().isalpha():
                QMessageBox.warning(self.ferramentas, 'Aviso', 'Letra para tentativa não atribuida..')
            else:
                def novoJogo():
                    self.jogada = 0
                    self.tab.removeTab(0)
                    self.jogo()

                self.jogada += 1
                posicao = 0
                acertou = '_' not in agrupaLetrasPalavra

                if self.letraJogador.text().upper() in selecionaPalavraAleatoria:
                    for letra in selecionaPalavraAleatoria:
                        if self.letraJogador.text().upper() == letra:
                            self.pontos += 100
                            agrupaLetrasPalavra[posicao] = self.letraJogador.text().upper()
                            labelJogo.setText(f"""
Nível: {self.nivel.currentText()} - Rodada: {self.jogada} de {self.tentativas}

(^.^) Obaa..
VOCÊ ACERTOU {self.nomeJogador.text()}!

{agrupaLetrasPalavra}

Pontos {self.pontos}
""")
                            labelJogo.setStyleSheet("background-color:white; color:blue; border-radius: 3px; border: 2px solid; padding:50px;")
                        posicao += 1
                else:
                    self.pontos -= 50
                    labelJogo.setText(f"""
Nível: {self.nivel.currentText()} - Rodada: {self.jogada} de {self.tentativas}

(O_O) Upss..
VOCÊ ERROU {self.nomeJogador.text()}!

Pontos {self.pontos}
""")
                    labelJogo.setStyleSheet("background-color:white; color:red; border-radius: 3px; border: 2px solid; padding:50px;")
                if acertou:
                    labelJogo.setText(f"""
(^3^) Parabéns {self.nomeJogador.text()}
VOCÊ GANHOU..

{agrupaLetrasPalavra}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.jogada} de {self.tentativas}
Pontos: {self.pontos}
""")
                    labelJogo.setStyleSheet("background-color:white; color:green; border-radius: 3px; border: 2px solid; padding:50px;")
                    botaoValida.setText('Novo Jogo')
                    botaoValida.clicked.connect(novoJogo)
                elif self.jogada == self.tentativas:
                    labelJogo.setText(f"""
(T.T) Lamento {self.nomeJogador.text()}
VOCÊ ESGOTOU TODAS AS SUAS TENTATIVAS..

Palavra Secreta: {selecionaPalavraAleatoria}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.jogada} de {self.tentativas}
Pontos: {self.pontos}
""")
                    labelJogo.setStyleSheet("background-color:white; color:red; border-radius: 3px; border: 2px solid; padding:50px;")
                    botaoValida.setText('Novo Jogo')
                    botaoValida.clicked.connect(novoJogo)

        janela03 = QWidget()
        layout = QFormLayout()
        layout.setSpacing(20)

        labelInfo = QLabel(f"<h3>Bem-Vindo <i>{self.nomeJogador.text()}</i><br>"
                           f"Tente Adivinhar Qual é a Palavra Secreta..<br>"
                           f"{agrupaLetrasPalavra}</h3>")
        labelInfo.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelInfo)

        labelJogo = QLabel('\n.  .  .  .  .')
        labelJogo.setStyleSheet("background-color: white; border-radius: 3px; border: 2px solid; padding:100px;")
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
        botaoValida.setStyleSheet('background-color:cyan;')

        botaoFimJogo = QPushButton('Terminar o Jogo')
        botaoFimJogo.clicked.connect(self._sair)
        botaoFimJogo.setStyleSheet('background-color:red;')
        layout.addRow(botaoValida, botaoFimJogo)

        janela03.setLayout(layout)
        self.tab.addTab(janela03, 'Jogando')
        self.tab.setCurrentWidget(janela03)

    def palavrasSecretas(self):
        self.janela04 = QWidget()
        layout = QVBoxLayout()

        labelIntro = QLabel("<b>" + ".  . " * 5 + "PALAVRAS SECRETAS" + 5 * " .  ." + "</b>")
        labelIntro.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelIntro)

        listaPalavras = QListWidget()
        for palavra in sorted(self.palavras):
            listaPalavras.addItem(palavra)
        listaPalavras.setAlternatingRowColors(True)
        layout.addWidget(listaPalavras)

        labelExtra = QLabel(f"<i>* {len(self.palavras)} palavras..</i>")
        labelExtra.setAlignment(Qt.AlignRight)
        labelExtra.setStyleSheet("color:#D1C399;")
        layout.addWidget(labelExtra)

        fechar = lambda: self.tab.removeTab(self.tab.currentIndex())
        botaoFechar = QPushButton("Fechar")
        botaoFechar.setStyleSheet('background-color:red;')
        botaoFechar.clicked.connect(fechar)
        layout.addWidget(botaoFechar)

        self.janela04.setLayout(layout)
        self.tab.addTab(self.janela04, 'Palavras Secretas')
        self.tab.setCurrentWidget(self.janela04)


if __name__ == '__main__':
    app = J3A7P6()
    app.ferramentas.show()
    app.gc.exec_()
