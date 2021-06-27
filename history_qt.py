import sqlite3
from sqlite3 import Error

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
     nome varchar(50) unique not null,
     pontos varchar(9) not null
    );
     """
    try:
        sql=db.cursor()
        result = sql.execute(query)
        return result
    except Error as er:
        raise er
    

def add_pontos(*args):

    db = connection()
    #return f""" "{args[0]}","{args[1]}" """
    query =f"""
        INSERT INTO tb_jogo(nome,pontos)VALUES("{args[0]}","{args[1]}");
        """

    try:
        sql=db.cursor()
        result = sql.execute(query)
        db.commit()
        return result
    except Error as er:
        db.rollback
        raise er


def view_pontos():
    db = connection()
    query =f"""
        SELECT *FROM tb_jogo;
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