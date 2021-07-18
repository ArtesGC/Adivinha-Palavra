import os
import sqlite3


def connect_db():
    """criando conexão com db sqlite

    :return: resultado da conexao
    """
    try:
        if not os.path.exists('historico'):
            os.mkdir('historico')
        return sqlite3.connect("historico/ap.db")
    except sqlite3.Error as erro:
        raise erro


def criar_tabela_jogo():
    """criando tabela dos jogadores

    :return: resultado da conexao
    """
    db = connect_db()
    query = "CREATE TABLE IF NOT EXISTS tb_jogo" \
            "(id integer primary key autoincrement," \
            " nome varchar(50) not null," \
            " pontos varchar(20) not null," \
            " tentativas varchar(10) not null," \
            " nivel varchar(5) not null);"
    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as erro:
        db.rollback()
        raise erro


def add_dados(_nome, _pontos, _tentativas, _nivel):
    """criando historico de jogada

    :param _nome: nome do jogador
    :param _pontos: pontos obtidos
    :param _tentativas: numero de tentativas
    :param _nivel: nivel selecionado durante o jogo
    :return: resultado da conexao
    """
    db = connect_db()
    query = f'INSERT INTO tb_jogo' \
            f'(nome,pontos,tentativas,nivel)' \
            f'VALUES("{_nome}","{_pontos}","{_tentativas}","{_nivel}");'

    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as er:
        db.rollback()
        raise er


def ver_dados():
    """selecionar os dados guardados na db

    :return: os dados em uma lista
    """
    db = connect_db()
    query = f"SELECT nome,pontos,tentativas,nivel FROM tb_jogo;"
    try:
        sql = db.cursor()
        sql.execute(query)
        result = sql.fetchall()
        db.commit()
        return result
    except sqlite3.Error as erro:
        db.rollback()
        raise erro


def apagar_historico():
    """apagar todos os dados ja guardados

    :return: resultado da conexao
    """
    db = connect_db()
    query = "DELETE * FROM tb_jogo;"
    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as erro:
        db.rollback()
        raise erro
