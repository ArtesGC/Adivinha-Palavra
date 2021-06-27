from unittest import TestCase
from history_qt import connection,tabela_jogo,add_pontos,view_pontos,apagar_historico

class jogo(TestCase):

    def setUp(self):
        pass

    def test_connect(self):
        conection = connection()
        self.assertTrue(True)
    
    def test_create_table(self):
        criar_tabela_historico = tabela_jogo()
        print(criar_tabela_historico)
        self.assertTrue(criar_tabela_historico)

    def test_criando_dados(self):
        criar_historico = add_pontos("Paulo",100,10,1)
        print(criar_historico)
        self.assertTrue(criar_historico)

    def test_ver_dados_in_player(self):
        ver_historico = view_pontos()
        print(ver_historico)
        self.assertTrue(ver_historico)
        

    def test_zerar_jogo(self):
        apagar_todos_historicos =apagar_historico()
        print(apagar_todos_historicos)
        self.assertTrue(apagar_todos_historicos)