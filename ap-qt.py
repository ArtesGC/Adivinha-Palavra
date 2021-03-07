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
        self.ferramentas.setFont(QFont('times'))
        self.ferramentas.setPalette(QPalette(QColor('cadetblue')))
        self.ferramentas.setWindowIcon(QIcon("img/adivinhapalavra-ico2.png"))
        self.ferramentas.setFixedSize(600, 500)

        # ******* criando abas para melhor organização *******
        self.tab = QTabWidget(self.ferramentas)
        self.tab.setFixedSize(600, 480)
        self.tab.move(0, 28)

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

        # ******* variaveis *******
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
        menu = QToolBar(self.ferramentas)
        self.reiniciarJogo = menu.addAction("Reiniciar")
        self.reiniciarJogo.setEnabled(False)
        self.reiniciarJogo.triggered.connect(self._reiniciarJogo)
        menu.addSeparator()

        instr = menu.addAction("Instruções")
        instr.triggered.connect(self._instr)
        menu.addSeparator()

        palavraSecretas = menu.addAction("Palavras Secretas")
        palavraSecretas.triggered.connect(self._palavrasSecretas)
        menu.addSeparator()

        sobre = menu.addAction("Sobre")
        sobre.triggered.connect(self._sobre)
        menu.addSeparator()

        sair = menu.addAction("Sair")
        sair.triggered.connect(self._sair)
        menu.addSeparator()

        self.janelaPrincipal()

    def _reiniciarJogo(self):
        if self.janela02 is None:
            return self.iniciarJogo()
        try:
            self.tab.setCurrentWidget(self.janela02)
        except Exception as e:
            self.tab.removeTab(0)
            return self.iniciarJogo()
        else:
            self.tab.removeTab(0)
            return self.iniciarJogo()

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
    conte quantas letras tem a suposta palavra
    identificada pelos simbolos '_' (referem-se as letras da palavra)
    e use a lista de palavras que estão escondidas no menu de opções
    (Palavras Secretas).. Use as como referência para as suas tentativas!

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
Versão: 0.5-032021
Designer e Programador: Nurul GC
Empresa: ArtesGC Inc.
''')

    def _sair(self):
        self.gc.exit(0)

    def janelaPrincipal(self):
        janela01 = QWidget()
        layout = QVBoxLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/adivinhapalavra-ico1.png").scaled(QSize(373, 376)))
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
                n = randint(3, 5)
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
        self.reiniciarJogo.setEnabled(True)
        QMessageBox.information(self.ferramentas, "Atenção", "Para uma melhor experiência de jogo leia as instruções que se encontram na barra de menu..\nObrigado pelo apoio! - ArtesGC")
        self.janela02 = QWidget()
        layout = QFormLayout()
        layout.setVerticalSpacing(20)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/03.png"))
        labelImagem.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelImagem)

        labelExtra = QLabel("<b>" + " .  .  . " * 5 + "DADOS DO JOGADOR" + " .  .  . " * 5 + "</b>")
        labelExtra.setAlignment(Qt.AlignCenter)
        layout.addRow(labelExtra)

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

        self.nomeJogador = QLineEdit()
        layout.addRow("<b>&Nome do Jogador: *</b>", self.nomeJogador)

        niveis = ['1', '2', '3']
        self.nivel = QComboBox()
        self.nivel.addItems(niveis)
        self.nivel.setToolTip('Nível 1 - 25 tentativas\nNível 2 - 20 tentativas\nNível 3 - 15 tentativas')
        layout.addRow("<b>Selecione o &Nível: *</b>", self.nivel)

        botaoJogar = QPushButton("Jogar")
        botaoJogar.setDefault(True)
        botaoJogar.setPalette(QPalette(QColor("green")))
        botaoJogar.clicked.connect(jogo)
        layout.addWidget(botaoJogar)

        browser = lambda p: webbrowser.open('https://artesgc.home.blog')
        labeCopyright = QLabel("<a href='#' style='text-decoration:none;'>ArtesGC Inc.</a>")
        labeCopyright.setAlignment(Qt.AlignRight)
        labeCopyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        labeCopyright.linkActivated.connect(browser)
        layout.addWidget(labeCopyright)

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
                            labelJogo.setText(f"""{'-' * 50}
    Nível: {self.nivel.currentText()} Rodada: {self.jogada} de {self.tentativas}
    
    (^.^) Obaa..
    VOCÊ ACERTOU {self.nomeJogador.text()}!
    
    {agrupaLetrasPalavra}
    
    Pontos {self.pontos}
    {'-' * 50}""")
                            labelJogo.setStyleSheet("QLabel{background-color:white;color:blue;}")
                        posicao += 1
                else:
                    self.pontos -= 50
                    labelJogo.setText(f"""{'-' * 50}
    Nível: {self.nivel.currentText()} Rodada: {self.jogada} de {self.tentativas}
    
    (O_O) Upss..
    VOCÊ ERROU {self.nomeJogador.text()}!
    Pontos {self.pontos}
    {'-' * 50}""")
                    labelJogo.setStyleSheet("QLabel{background-color:white;color:red;}")
                if acertou:
                    labelJogo.setText(f"""{'-' * 50}
    (^3^) Parabéns {self.nomeJogador.text()}
    VOCÊ GANHOU..
    {agrupaLetrasPalavra}
    
    • Pontuação
    Nível: {self.nivel.currentText()}
    Rodada: {self.jogada} de {self.tentativas}
    Pontos: {self.pontos}
    {'-' * 50}""")
                    labelJogo.setStyleSheet("QLabel{background-color:white;color:green;}")
                    botaoValida.setText('Novo Jogo')
                    botaoValida.clicked.connect(novoJogo)
                    botaoFimJogo.setEnabled(True)
                elif self.jogada == self.tentativas:
                    labelJogo.setText(f"""{'-' * 50}
    (T.T) Lamento {self.nomeJogador.text()}
    VOCÊ ESGOTOU TODAS AS TENTATIVAS..
    Palavra Secreta: {selecionaPalavraAleatoria}
    
    • Pontuação
    Nível: {self.nivel.currentText()}
    Rodada: {self.jogada} de {self.tentativas}
    Pontos: {self.pontos}
    {'-' * 50}""")
                    labelJogo.setStyleSheet("QLabel{background-color:white;color:red;}")
                    botaoValida.setText('Novo Jogo')
                    botaoValida.clicked.connect(novoJogo)
                    botaoFimJogo.setEnabled(True)

        janela03 = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(20)

        labelInfo = QLabel(f"""Bem-Vindo <b>{self.nomeJogador.text()}</b><br>
tente adivinhar qual é a palavra secreta.. <br>
<b>{agrupaLetrasPalavra}</b>""")
        labelInfo.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelInfo)

        labelJogo = QLabel('.  .  .  .  .')
        labelJogo.setStyleSheet("QLabel{background-color: white;}")
        labelJogo.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelJogo)

        labelExtra = QLabel("<b>" + " .  .  . " * 5 + "JOGANDO" + " .  .  . " * 5 + "</b>")
        labelExtra.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelExtra)

        layoutLetraJogador = QFormLayout()
        self.letraJogador = QLineEdit()
        self.letraJogador.setMaxLength(1)
        self.letraJogador.returnPressed.connect(validaJogada)
        layoutLetraJogador.addRow('Digite a &letra:', self.letraJogador)
        layout.addLayout(layoutLetraJogador)

        botoesJogoLayout = QHBoxLayout()
        botaoValida = QPushButton('Validar Jogada')
        botaoValida.setDefault(True)
        botaoValida.clicked.connect(validaJogada)
        botaoValida.setPalette(QPalette(QColor('cyan')))

        botaoFimJogo = QPushButton('Terminar o Jogo')
        botaoFimJogo.setDefault(True)
        botaoFimJogo.clicked.connect(self._sair)
        botaoFimJogo.setEnabled(False)
        botaoFimJogo.setPalette(QPalette(QColor('red')))

        botoesJogoLayout.addWidget(botaoValida)
        botoesJogoLayout.addWidget(botaoFimJogo)
        layout.addLayout(botoesJogoLayout)

        janela03.setLayout(layout)
        self.tab.addTab(janela03, 'Jogando')
        self.tab.setCurrentWidget(janela03)

    def palavrasSecretas(self):
        self.janela04 = QWidget()
        layout = QVBoxLayout()

        labelIntro = QLabel("<b>" + " .  .  . " * 5 + "PALAVRAS SECRETAS" + 5 * " .  .  . " + "</b>")
        labelIntro.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelIntro)

        listaPalavras = QListWidget()
        for palavra in sorted(self.palavras):
            listaPalavras.addItem(palavra)
        listaPalavras.setAlternatingRowColors(True)
        layout.addWidget(listaPalavras)

        labelExtra = QLabel(f"<i>* {len(self.palavras)} palavras..</i>")
        labelExtra.setAlignment(Qt.AlignRight)
        labelExtra.setStyleSheet("QLabel{color:lightgreen;}")
        layout.addWidget(labelExtra)

        fechar = lambda: self.tab.removeTab(self.tab.currentIndex())
        botaoFechar = QPushButton("Fechar")
        botaoFechar.setDefault(True)
        botaoFechar.setPalette(QPalette(QColor('red')))
        botaoFechar.clicked.connect(fechar)
        layout.addWidget(botaoFechar)

        self.janela04.setLayout(layout)
        self.tab.addTab(self.janela04, 'Palavras Secretas')
        self.tab.setCurrentWidget(self.janela04)


if __name__ == '__main__':
    app = J3A7P6()
    app.ferramentas.show()
    app.gc.exec_()
