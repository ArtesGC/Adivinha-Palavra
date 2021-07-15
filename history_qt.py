import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import IntegrityError

def connection():
    """
    criando conexão com db sqlite
    """
    try:
        return sqlite3.connect("historico.db")
    except Error as er:
        raise er

def tabela_jogo():
    db = connection()
    query = """
    CREATE TABLE IF NOT EXISTS tb_jogo(
     id integer primary key autoincrement,
     nome varchar(50) not null,
     pontos varchar(9) not null,
     jogada varchar(10) not null,
     nivel varchar(5) not null
    );
     """
    try:
        sql=db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except Error as er:
        db.rollback()
        raise er
    

def add_pontos(*args):
    """
    criando historico de jogada
    : ** campos obrigatórios! **
    - nome
    - pontos
    - jogada
    - nivel 
    

    """
    db = connection()
    #return f""" "{args[0]}","{args[1]}" """
    query =f"""
        INSERT INTO tb_jogo(nome,pontos,jogada,nivel)VALUES("{args[0]}","{args[1]}","{args[2]}","{args[3]}");
        """

    try:
        sql=db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except Error as er:
        db.rollback()
        raise er
        


def view_pontos():
    db = connection()
    query =f"""
        SELECT nome,pontos,jogada,nivel FROM tb_jogo;
        """
    try:
        sql=db.cursor()
        sql.execute(query)
        result = sql.fetchall()
        db.commit()
        return result
    except Error as er:
        db.rollback
        raise er

def apagar_historico():
    db = connection()
    query ="""
        DELETE FROM tb_jogo;
        """
    try:
        sql=db.cursor()
        result=sql.execute(query)
        db.commit()
        return result
    except Error as er:
        db.rollback
        raise er