import sqlite3


def connection():
    """
    criando conexão com db sqlite
    """
    try:
        return sqlite3.connect("historico/ap.db")
    except sqlite3.Error as erro:
        raise erro


def tabela_jogo():
    db = connection()
    query = """
    CREATE TABLE IF NOT EXISTS tb_jogo(
     id integer primary key autoincrement,
     nome varchar(50) not null,
     pontos varchar(20) not null,
     jogada varchar(10) not null,
     nivel varchar(5) not null
    );
     """
    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as erro:
        db.rollback()
        raise erro


def add_pontos(_nome, _pontos, _jogada, _nivel):
    """
    criando historico de jogada
    : ** campos obrigatórios! **
    - nome
    - pontos
    - jogada
    - nivel
    """
    db = connection()
    query = f'INSERT INTO tb_jogo(nome,pontos,jogada,nivel)VALUES("{_nome}","{_pontos}","{_jogada}","{_nivel}");'

    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as er:
        db.rollback()
        raise er


def view_pontos():
    db = connection()
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
    db = connection()
    query = "DELETE FROM tb_jogo;"
    try:
        sql = db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except sqlite3.Error as erro:
        db.rollback()
        raise erro
