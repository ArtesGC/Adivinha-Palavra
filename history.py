import os
import sqlite3


def connect_db():
    """
    criando conexão com db sqlite
    """
    try:
        if not os.path.exists('historico'):
            os.mkdir('historico')

        return sqlite3.connect("historico/ap.db")
    except sqlite3.Error as erro:
        raise erro


def criar_tabela_jogo():
    db = connect_db()
    query = "CREATE TABLE IF NOT EXISTS tb_jogo" \
            "(id integer primary key autoincrement," \
            " nome varchar(50) not null," \
            " pontos varchar(20) not null," \
            " jogada varchar(10) not null," \
            " nivel varchar(5) not null);"
    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as erro:
        db.rollback()
        raise erro


def add_dados(_nome, _pontos, _jogada, _nivel):
    """
    criando historico de jogada
    : ** campos obrigatórios! **
    - nome
    - pontos
    - jogada
    - nivel
    """
    db = connect_db()
    query = f'INSERT INTO tb_jogo' \
            f'(nome,pontos,jogada,nivel)' \
            f'VALUES("{_nome}","{_pontos}","{_jogada}","{_nivel}");'

    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as er:
        db.rollback()
        raise er


def ver_dados():
    db = connect_db()
    query = f"SELECT nome,pontos,jogada,nivel FROM tb_jogo;"
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
    db = connect_db()
    query = "DELETE FROM tb_jogo;"
    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as erro:
        db.rollback()
        raise erro
