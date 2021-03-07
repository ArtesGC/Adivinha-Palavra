# ******************************************************************************
#  (c) 2019-2021. Nurul GC                                                     *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicaçoes                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from random import *
from tkinter import *
import tkinter.ttk as ttk
from tk_tools.tooltips import ToolTip
from tkinter.messagebox import *
from tkinter.scrolledlist import ScrolledList


class J3A7P6:
    """
    Type: PythonSource
    Name: Jogo Adivinha a Palavra
    Modified: 18/04/2020 10:00pm
    Created: 31/03/2020 07:00am
    Version: 0.1-042020 - 0.2-042020 - 0.3-042020 - 0.4-012021
    Autor: Nurul GC - https://artesgc.home.blog
    cor: (2)MistyRose1, (1)#d513bc
    """

    def __init__(self):
        self.gc_ = None
        self.janela = None
        self.gc = Tk()
        # self.gc.iconbitmap(default='./img/adivinhapalavra_gc.ico')
        self.gc.title('Adivinha Palavra')
        self.gc.resizable(0, 0)

        self.ft = PhotoImage(file="img/02.png")
        self.foto5 = PhotoImage(file="img/03.png")
        self.nome = StringVar()
        self.nivel = IntVar()
        self.n_tentativas = IntVar()
        self.rodada = IntVar()
        self.pontos = IntVar()
        self.chute = StringVar()

        #
        self.menu = Menu(self.gc)
        self.tab = ttk.Notebook(self.gc)
        self.tab.pack(expand=1, fill='both')
        self.jogo()

    def jogo(self):

        def pt():
            showinfo("Atenção", "Para uma melhor experiência de jogo leia as instruções que se encontram no menu de opções..\nObrigado pelo apoio! - ArtesGC")
            palavra_ = ['ATENCIOSO', 'AGRADAVEL', 'ADORAVEL', 'AMAVEL', 'AFAVEL', 'AMIGAVEL', 'AMOROSO', 'AUTENTICO', 'APIXONADO', 'ANIMADO', 'ALEGRE', 'AMISTOSO', 'AMIGO',
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

            def palavra_secreta():
                self.janela = LabelFrame(self.tab)
                self.tab.add(self.janela, text='Palavras Secretas', underline=0)
                self.tab.select(self.janela)
                self.janela.configure(padx=15, pady=15, bg='MistyRose1')

                lst = ScrolledList(self.janela)
                lst.pack(side='left', expand=1, fill='both')

                for p in sorted(palavra_):
                    lst.insert(END, p)

                Button(self.janela, text='Fechar', command=self.janela.destroy, bg='red', fg='black').pack(anchor=SE)

            def palavra_secreta_():
                if self.janela is None:
                    return palavra_secreta()
                try:
                    self.tab.select(self.janela)
                except TclError:
                    return palavra_secreta()

            def instr():
                showinfo('Instruções', """
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
""")

            def hello():
                showinfo('Sobre', '''
Nome: Jogo Adivinha Palavra
Versão: 0.4-012021
Designer e Programador: Nurul GC
Empresa: ArtesGC Inc.
''')

            def pt_():
                if self.root is None:
                    return pt()
                try:
                    self.tab.select(self.root)
                except TclError:
                    self.gc_.destroy()
                    return pt()

            def jogo_nivel():
                #
                if self.nivel.get() == 3:
                    self.n_tentativas.set(15)
                    self.pontos.set(0)
                    jogo()
                elif self.nivel.get() == 2:
                    self.n_tentativas.set(20)
                    self.pontos.set(0)
                    jogo()
                elif self.nivel.get() == 1:
                    self.n_tentativas.set(25)
                    self.pontos.set(0)
                    jogo()
                else:
                    showerror('Erro!', 'Nível não Definido..')

            def jogo():
                self.root.destroy()
                self.gc_ = LabelFrame(self.tab)
                self.tab.add(self.gc_, text='Adivinhe a Palavra', underline=11)
                self.tab.select(self.gc_)
                self.gc_.configure(padx=30, pady=5, bg='MistyRose1')

                #
                self.rodada.set(0)
                palavra_l = len(palavra_)  # 536 palavras
                palavra = palavra_[randrange(palavra_l)]
                letra = ['_' for ltra in palavra]

                #
                def confirma(p):
                    self.rodada.set(abs(self.rodada.get() + 1))
                    posicao = 0

                    def novo():
                        self.gc_.destroy()
                        jogo()

                    #
                    if self.chute.get().upper() in palavra:
                        for ltra in palavra:
                            if self.chute.get().upper() == ltra:
                                self.pontos.set(abs(self.pontos.get() + 100))
                                letra[posicao] = self.chute.get().upper()
                                lr.configure(text=f'''Nível: {self.nivel.get()} Rodada: {self.rodada.get()} de {self.n_tentativas.get()}

(^.^) Obaa..
VOCÊ ACERTOU {self.nome.get()}!
{letra}
Pontos {self.pontos.get()}''', fg='blue')
                            posicao += 1
                    else:
                        self.pontos.set(abs(self.pontos.get() - 50))
                        lr.configure(text=f'''Nível: {self.nivel.get()} Rodada: {self.rodada.get()} de {self.n_tentativas.get()}

(O_O) Upss..
VOCÊ ERROU {self.nome.get()}!
Pontos {self.pontos.get()}''', fg='red')
                    #
                    acertou = '_' not in letra
                    if acertou:
                        lr.configure(text=f"""(^3^) Parabéns {self.nome.get()}
VOCÊ GANHOU..
{letra}

• Pontuação
Nível: {self.nivel.get()}
Rodada: {self.rodada.get()} de {self.n_tentativas.get()}
Pontos: {self.pontos.get()}""", fg='green')
                        b.configure(text='Jogar de Novo', command=novo, bg='blue', fg='white')
                        b2.grid(row=5, column=2, sticky=W)
                    elif self.rodada.get() == self.n_tentativas.get():
                        lr.configure(text=f"""(T.T) LAMENTO {self.nome.get()}
VOCÊ ESGOTOU TODAS AS TENTATIVAS..
Palavra Secreta: {palavra}

• Pontuação
Nível: {self.nivel.get()}
Rodada: {self.rodada.get()} de {self.n_tentativas.get()}
Pontos: {self.pontos.get()}""", fg='red')
                        b.configure(text='Jogar de Novo', command=novo, bg='blue', fg='white')
                        b2.grid(row=5, column=2, sticky=W)

                #
                Label(self.gc_, text='🙇    🙈🙊    🤷    👀    🤓    😂', bg='MistyRose1', font='consolas 16').grid(row=0, columnspan=1)
                f_jogo = LabelFrame(self.gc_, text='J O G A N D O', font='consolas 8 bold', fg='#d513bc', relief='groove', bg='MistyRose1')
                f_jogo.grid(row=1, column=0, pady=10)
                Label(f_jogo, text=f'Olá {self.nome.get()} Tenta Adivinhar Qual é a Palavra Secreta\n{letra}', bg='MistyRose1', font='consolas 10 bold').grid(row=0, columnspan=3)
                Label(f_jogo, text='__________________________________________________\n', bg='MistyRose1').grid(row=1, columnspan=3)
                lr = Label(f_jogo, text='.  .  .  .  .', font='Consolas 10 bold', bg='white')
                lr.grid(row=2, columnspan=3)
                Label(f_jogo, text='__________________________________________________', bg='MistyRose1').grid(row=3, columnspan=3)

                Label(f_jogo, text='Digite a letra', underline=9, bg='MistyRose1', font='consolas 10 bold').grid(row=4, column=0)
                e = ttk.Entry(f_jogo, textvariable=self.chute)
                e.grid(row=4, column=1, sticky=W)
                e.bind("<Return>", confirma)

                b = Button(f_jogo, text='Confirmar', bg='cyan')
                b.grid(row=4, column=2, sticky=W)
                b.bind("<Button-1>", confirma)
                b2 = Button(f_jogo, text='Fim do Jogo', command=self.gc.destroy, bg='red')

            #
            self.tab1.destroy()
            self.root = LabelFrame(self.tab)
            self.tab.add(self.root, text='Paz e Bençãos de Deus Sobre Ti')
            self.tab.select(self.root)
            self.root.configure(padx=15, pady=15, bg='MistyRose1')
            #
            menu_pt = Menu(self.menu, tearoff=0, bg='MistyRose1', font='tahoma 8')
            menu_pt.add_command(label='Novo Jogo', command=pt_, underline=5)
            menu_pt.add_command(label='Instruções', command=instr, underline=0)
            menu_pt.add_command(label='Palavras Secretas', command=palavra_secreta_, underline=5)
            menu_pt.add_separator()
            menu_pt.add_command(label='Sair', command=self.gc.destroy, underline=0)
            detalhes = Menu(self.menu)
            detalhes.add_cascade(label='Opções', menu=menu_pt, underline=0)
            detalhes.add_command(label='Sobre', command=hello, underline=0)
            self.gc.configure(menu=detalhes)
            self.gc.title('Adivinhe a Palavra')

            #
            Label(self.root, image=self.foto5, bg='#d513bc').grid(row=0, column=0)

            f1 = LabelFrame(self.root, text='J O G A D O R', font='consolas 8 bold', fg='#d513bc', relief='groove', bg='MistyRose1')
            f1.grid(row=1, column=0, pady=10)
            Label(f1, text='Digite o Seu Nome', underline=13, font='consolas 10 bold', bg='MistyRose1').grid(row=0, column=0)
            enm = Entry(f1, textvar=self.nome, bd=2)
            enm.grid(row=0, column=1)

            Label(f1, text='Escolha o Seu Nível', underline=14, font='consolas 10 bold', bg='MistyRose1').grid(row=1, column=0)
            vl = [1, 2, 3]
            e1_ = ttk.Combobox(f1, textvariable=self.nivel, values=vl, width=17)
            e1_.grid(row=1, column=1)
            ToolTip(e1_, 'Nível 1 - 25 tentativas\nNível 2 - 20 tentativas\nNível 3 - 15 tentativas')

            Button(f1, text='Jogar', command=jogo_nivel, bg='cyan').grid(row=2, column=1, sticky=E)
            enm.focus()

        self.tab1 = LabelFrame(self.tab)
        self.tab.add(self.tab1, text='Bem Vindo')
        self.tab.select(self.tab1)
        self.tab1.configure(padx=30, pady=10, bg='MistyRose1')

        Label(self.tab1, text="JOGO ADIVINHE A PALAVRA", font='Consolas 12 bold', fg='#d513bc', bg='MistyRose1').grid(row=0, column=0)
        Label(self.tab1, image=self.ft, bg='#d513bc').grid(row=1, column=0, pady=10)
        f = LabelFrame(self.tab1, bg='MistyRose1')
        f.grid(row=2, column=0)
        Radiobutton(f, text=' COMEÇAR ', command=pt, indicatoron=False, font='arial 7 bold').grid(row=0, column=0, padx=5, pady=5)


if __name__ == '__main__':
    app = J3A7P6()
    app.gc.mainloop()
