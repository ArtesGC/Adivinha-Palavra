"""
modulo para funcoes auxiliares ao programa

- (c) 2019-2022 Nurul-GC
"""

import os
from subprocess import getoutput


def debugpath() -> str:
    if os.name == 'posix':
        home = getoutput('echo $HOME')
        return os.path.join(home, '.ap-debug')
    return '.ap-debug'


def palavras_listadas() -> list:
    """funcao que retorna as palavras secretas"""
    return ['ATENCIOSO',
            'AGRADAVEL',
            'ADORAVEL',
            'AMAVEL',
            'AFAVEL',
            'AMIGAVEL',
            'AMOROSO',
            'AUTENTICO',
            'APAIXONADO',
            'ANIMADO',
            'ALEGRE',
            'AMISTOSO',
            'AMIGO',
            'AFETIVO',
            'AFETUOSO',
            'ACOLHEDOR',
            'APRAZIVEL',
            'ATRAENTE',
            'ATRATIVO',
            'AUDAZ',
            'AVENTUREIRO',
            'ARROJADO',
            'AUSPICIOSO',
            'APLICADO',
            'ALTRUISTA',
            'ASSERTIVO',
            'ATENTO',
            'AGIL',
            'APTO',
            'ATILADO',
            'ASTUTO',
            'ARGUTO',
            'AJUIZADO',
            'ASSOMBROSO',
            'ADMIRAVEL',
            'AIROSO',
            'ADONISAFORTUNADO',
            'ACAUTELADO',
            'ANGELICAL',
            'ABERTO',
            'ACESSIVEL',
            'BOM',
            'BONDOSO',
            'BONITO',
            'BELO',
            'BACANA',
            'BENDITO',
            'BATALHADOR',
            'BASEADO',
            'BENEMERITO',
            'BENFEITOR',
            'BENEVOLO',
            'BENEVOLENTE',
            'BRILHANTE',
            'BRIOSO',
            'BRINCALHAO',
            'BOMBASTICO',
            'BELEZA',
            'BELDADE',
            'BENEFICO',
            'BENIGNO',
            'BENFAZEJO',
            'BENQUISTO',
            'CALMO',
            'CALOROSO',
            'CAMARADA',
            'CANDIDO',
            'CAPAZ',
            'CARIDOSO',
            'CARINHOSO',
            'CARISMATICO',
            'CARITATIVO',
            'CATIVANTE',
            'CAUTELOSO',
            'CAVALHEIRO',
            'CELESTIAL',
            'CENTRADO',
            'CHARMOSO',
            'CHEIROSO',
            'CHIQUE',
            'CHISTOSO',
            'CIENTE',
            'CIRCUNSPECTO',
            'CIVICO',
            'CIVIL',
            'CIVILIZADO',
            'CLARIVIDENTE',
            'CLEMENTE',
            'COERENTE',
            'COLABORADOR',
            'COLEGA',
            'COMEDIDO',
            'COMPANHEIRO',
            'COMPASSIVO',
            'COMPETENTE',
            'COMPLACENTE',
            'COMPORTADO',
            'COMPREENSIVO',
            'CONFIANTE',
            'CONFIAVEL',
            'CONFIDENTE',
            'CONHECEDOR',
            'CONSCIENCIOSO',
            'CONSCIENTE',
            'CONTENTE',
            'CONVICTO',
            'COOPERADOR',
            'CORAJOSO',
            'CORDIAL',
            'CORRECTO',
            'CORTES',
            'CRANIO',
            'CREDIVEL',
            'CRESCIDO',
            'CRIATIVO',
            'CRITERIOSO',
            'CRIVEL',
            'CUIDADOSO',
            'CULTO',
            'DIVERTIDO',
            'DEDICADO',
            'DECENTE',
            'DIGNO',
            'DECOROSO',
            'DECIDIDO',
            'DEFERENTE',
            'DELICADO',
            'DESTEMIDO',
            'DENODADO',
            'DADO',
            'DOCE',
            'DOCIL',
            'DISTINTO',
            'DIREITO',
            'DADIVOSO',
            'DOTADO',
            'DISPONIVEL',
            'DINAMICO',
            'DILIGENTE',
            'DONAIROSO',
            'DISPOSTO',
            'DISCRETO',
            'DIPLOMATICO',
            'DISCIPLINADO',
            'DIRETO',
            'DILETO',
            'DEVOTO',
            'DEVANEADOR',
            'DEUS',
            'DESLUMBRANTE',
            'DESEJAVEL',
            'DESENVOLVIDO',
            'DESENRASCADO',
            'DESENROLADO',
            'EDUCADO',
            'EFICIENTE',
            'EFUSIVO',
            'ELEGANTE',
            'ELOQUENTE',
            'EMANCIPADO',
            'EMINENTE',
            'EMPATICO',
            'EMPENHADO',
            'EMPOLGADO',
            'EMPREENDEDOR',
            'ENCANTADOR',
            'ENCORAJADOR',
            'ENGENHOSO',
            'ENGRACADO',
            'ENTENDIDO',
            'ENTUSIASMADO',
            'ENTUSIASTA',
            'EQUILIBRADO',
            'ESBELTO',
            'ESCLARECIDO',
            'ESCRUPULOSO',
            'ESFORCADO',
            'ESMERADO',
            'ESPANTOSO',
            'ESPECIAL',
            'ESPECIALISTA',
            'ESPERACOSO',
            'ESPERTO',
            'ESPETACULAR',
            'ESPIRITUOSO',
            'ESPLENDIDO',
            'ESPLENDOROSO',
            'ESPONTANEO',
            'ESTONTEANTE',
            'ETERNO',
            'EVOLUIDO',
            'ESCELENTE',
            'EXCELSO',
            'EXEMPLAR',
            'EXIMIO',
            'EXPERIENTE',
            'EXTRAORDINARIO',
            'EXTROVERTIDO',
            'EXTREMOSO',
            'EXUBERANTE',
            'EXULTANTE',
            'FIEL',
            'FORTE',
            'FRANCO',
            'FRONTAL',
            'FIRME',
            'FANTASTICO',
            'FENOMENAL',
            'FABULOSO',
            'FASCINANTE',
            'FORMIDAVEL',
            'FIDEDIGNO',
            'FORMOSO',
            'FOFO',
            'FELIZ',
            'FELIZARDO',
            'FACEIRO',
            'FERVOROSO',
            'GENTIL',
            'GENEROSO',
            'GENUINO',
            'GRACIOSO',
            'GRANDE',
            'GRANDIOSO',
            'GENIO',
            'GENIAL',
            'GALANTE',
            'GATO',
            'GOSTOSO',
            'GLORIOSO',
            'GLAMOROSO',
            'GIGANTE',
            'GIGANTESCO',
            'GUERREIRO',
            'GANATEADOR',
            'GRATO',
            'HONESTO',
            'HONRADO',
            'HUMANO',
            'HONROSO',
            'HONORAVEL',
            'HEROI',
            'HEROICO',
            'HABIL',
            'HABILIDOSO',
            'HILARIO',
            'HILARIANTE',
            'HOSPITALEIRO',
            'HUMANITARIO',
            'HOSPEDEIRO',
            'HUMILDE',
            'HUMILDOSO',
            'INTELIGENTE',
            'IMPORTANTE',
            'INTEGRO',
            'INCRIVEL',
            'ILUSTRE',
            'INTERESSANTE',
            'IMPRESSIONANTE',
            'IMPAR',
            'IDEAL',
            'IMPONENTE',
            'IMAGINATIVO',
            'IMPECAVEL',
            'IRREVERENTE',
            'IRRESISTIVEL',
            'INIGUALAVEL',
            'IMPARCIAL',
            'IDONEO',
            'INDEPENDENTE',
            'INSPIRADOR',
            'INTERVENTIVO',
            'INTUITIVO',
            'INTENSO',
            'INTELECTUAL',
            'INSTRUIDO',
            'IMORTAL',
            'IMPAVIDO',
            'ILUMINADO',
            'IMACULADO',
            'IDEALISTA',
            'IMPARAVEL',
            'INABALAVEL',
            'INCANSAVEL',
            'IMBATIVEL',
            'INVENCIVEL',
            'INSUBMISSO',
            'INSUBORNAVEL',
            'INVULNERAVEL',
            'INCURRUPTIVEL',
            'INCORRUPTO',
            'IMPRESCINDIVEL',
            'INDISPENSAVEL',
            'JUSTO',
            'JOVEM',
            'JOVIAL',
            'JOIA',
            'JEITOSO',
            'JUBILANTE',
            'JUBILOSO',
            'JANOTA',
            'JUSTICEIRO',
            'LEAL',
            'LEGAL',
            'LINDO',
            'LIVRE',
            'LUTADOR',
            'LOUVAVEL',
            'LAUDAVEL',
            'LARGO',
            'LEGITIMO',
            'LUCIDO',
            'LISONJEIRO',
            'LIBERAL',
            'LIBERTO',
            'LICITO',
            'LIDER',
            'LETRADO',
            'LABORIOSO',
            'MARAVILHOSO',
            'MAGNIFICO',
            'MAGNANIMO',
            'MAJESTOSO',
            'MAGNIFICENTE',
            'MAIOR',
            'MELHOR',
            'MAXIMO',
            'MERECEDOR',
            'MANEIRO',
            'MEIGO',
            'MIMOSO',
            'MODESTO',
            'MODICO',
            'MATERNAL',
            'MAVIOSO',
            'MOTIVADO',
            'MARCANTE',
            'MAGICO',
            'MAGNO',
            'MAGISTRAL',
            'MAESTRAL',
            'MERITORIO',
            'MODERNO',
            'MODERADO',
            'MADURO',
            'METICULOSO',
            'MINUCIOSO',
            'METODICO',
            'MIRABOLANTE',
            'NOTAVEL',
            'NOBRE',
            'NORMAL',
            'NATURAL',
            'NOVO',
            'NATURISTA',
            'NUTRIDO',
            'OBEDIENTE',
            'OBJECTIVO',
            'OBSEQUISO',
            'OBSERVADOR',
            'OBSTINADO',
            'OFICIOSO',
            'ONIPOTENTE',
            'ONISCIENTE',
            'OPERANTE',
            'OPORTUNO',
            'ORDEIRO',
            'ORGANIZADO',
            'ORIGINAL',
            'OTIMISTA',
            'OTIMO',
            'OUSADO',
            'PACATO',
            'PACIENTE',
            'PACIFICADOR',
            'PACIFICO',
            'PARCEIRO',
            'PARCIMONIOSO',
            'PERFEITO',
            'PERITO',
            'PERSEVERANTE',
            'PERSISTENTE',
            'PERSPICAZ',
            'PERTINAZ',
            'PIEDOSO',
            'PIONEIRO',
            'PODEROSO',
            'POLIDO',
            'PONDERADO',
            'PONTUAL',
            'PORREIRO',
            'PORRETA',
            'POSSANTE',
            'PRAZENTEIRO',
            'PREPARADO',
            'PRESTATIVO',
            'PRESTAVEL',
            'PRESTIGIOSO',
            'PREVENIDO',
            'PRIMOROSO',
            'PRINCIPE',
            'PRODIGIO',
            'PRODIGIOSO',
            'PROEMINENTE',
            'PROEFICIENTE',
            'PROTECTOR',
            'PROVECTOPRUDENTE',
            'PUJANTE',
            'PURO',
            'QUERIDO',
            'QUALIFICADO',
            'QUENTE',
            'RESPONSAVEL',
            'RESPEITAVEL',
            'RESPEITADOR',
            'RESPEITADO',
            'RESPEITOSO',
            'REALIZADO',
            'RENOMADO',
            'RESISTENTE',
            'RESOLUTO',
            'RESOLVIDO',
            'RESILIENTE',
            'ROBUSTO',
            'ROMANTICO',
            'RISONHO',
            'RADIANTE',
            'RESPLANDECENTE',
            'RELUZENTE',
            'REFINADO',
            'RACIONAL',
            'REALISTA',
            'REFLETIDO',
            'RELAXADO',
            'RECEPTIVO',
            'RECONHECIDO',
            'RAPIDO',
            'RAZOAVEL',
            'SIMPATICO',
            'SABIO',
            'SINCERO',
            'SENSATO',
            'SENSACIONAL',
            'SEGURO',
            'SORRIDENTE',
            'SOSSEGADO',
            'SUBLIME',
            'SOLICITO',
            'SOLIDARIO',
            'SERENO',
            'SENSIVEL',
            'SEDUTOR',
            'SAGAZ',
            'SAUDAVEL',
            'SINGULAR',
            'SOCIAVEL',
            'SOFISTICADO',
            'SERIO',
            'SONHADOR',
            'SANTO',
            'SENTIMENTAL',
            'SABEDOR',
            'SUTIL',
            'TALENTOSO',
            'TERNURENTO',
            'TERNO',
            'TRANQUILO',
            'TRANSPARENTE',
            'TOLERANTE',
            'TRABALHADOR',
            'TENAZ',
            'TREMENDO',
            'TRANSCENDENTE',
            'TRANSCENDENTAL',
            'TOCANTE',
            'TRIUNFANTE',
            'TRIUNFADOR',
            'TRIUNFAL',
            'TITANICO',
            'TRAQUEJADO',
            'TENRO',
            'TRANSIGENTE',
            'TEMPERANTE',
            'TRATAVEL',
            'TOLERAVEL',
            'TENTADOR',
            'TRANQUILIZANTE',
            'UNICO',
            'UNO',
            'URBANO',
            'UNIFICADOR',
            'ULTRAFANTASTICO',
            'ULTRACOMPETENTE',
            'ULTRACONFIANTE',
            'ULTRACORRECTO',
            'ULTRAINDEPENDENTE',
            'ULTRANATURAL',
            'ULTRARROMANTICO',
            'ULTRACIVILIZADO',
            'ULTRADIVINO',
            'ULTRAMODERNO',
            'ULTRARRACIONAL',
            'VERDADEIRO',
            'VALENTE',
            'VALIOSO',
            'VALOROSO',
            'VENCEDOR',
            'VERIDICO',
            'VENERAVEL',
            'VENTUROSO',
            'VISTOSO',
            'VIRTUOSO',
            'VERSADO',
            'VERSATIL',
            'VISIONARIO',
            'VITORIOSO',
            'VEEMENTE',
            'VENERADO',
            'VANGUARDISTA',
            'VALIDO',
            'VELOZ',
            'VIRIL',
            'VARONIL',
            'VERAZ',
            'VERBOSO',
            'VIBRANTE',
            'VIGOROSO',
            'VERDEJANTE',
            'VIVIDO',
            'VIVO',
            'VIVAZ',
            'VITAL',
            'VIGILANTE',
            'VULTOSO',
            'ZELOSO',
            'ZELADOR',
            'ZELANTE']
