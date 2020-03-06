import sqlite3

from src.modules.alunos.entities.aluno import Aluno


class AlunoRepository:
    db = sqlite3

    def __init__(self, database):
        self.db = database

    def save(self, aluno: Aluno):
        cursor = self.db.cursor()
        if isinstance(aluno.id, int):
            cursor.execute(f"UPDATE Alunos"
                            f" SET nome = '{aluno.nome}',"
                            f" documento = '{aluno.documento}',"
                            f" data_nascimento = '{aluno.data_nascimento}'"
                            f" WHERE id = {aluno.id}")
        else:
            cursor.execute(f"INSERT INTO Alunos(nome, documento, data_nascimento) VALUES ("
                            f"'{aluno.nome}',"
                            f"'{aluno.documento}',"
                            f"'{aluno.data_nascimento}');")
            aluno.id = cursor.lastrowid
        self.db.commit()

    def all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Alunos;")
        return cursor