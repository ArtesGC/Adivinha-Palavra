from unittest import TestCase
from ap.history import connect_db, criar_tabela_jogo, add_dados, ver_dados, apagar_historico


class jogo(TestCase):

    def setUp(self):
        pass

    def test_connect(self):
        conection = connect_db()
        self.assertTrue(True)

    def test_create_table(self):
        criar_tabela_historico = criar_tabela_jogo()
        print(criar_tabela_historico)
        self.assertTrue(criar_tabela_historico)

    def test_criando_dados(self):
        criar_historico = add_dados("Lopes", 100, 10, 1)
        print(criar_historico)
        self.assertTrue(criar_historico)

    def test_ver_dados_in_player(self):
        ver_historico = ver_dados()
        for vl in ver_historico:
            print(vl)
        self.assertTrue(ver_historico)

    def test_zerar_jogo(self):
        apagar_todos_historicos = apagar_historico()
        print(apagar_todos_historicos)
        self.assertTrue(apagar_todos_historicos)
