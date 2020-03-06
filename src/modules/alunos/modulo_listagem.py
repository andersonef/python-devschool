from src.interfaces.module_interface import ModuleInterface
from src.modules.alunos.aluno_presenter import print_alunos
from src.modules.alunos.entities.aluno import Aluno
from src.modules.alunos.repositories.aluno_repository import AlunoRepository


class ModuloListagem(ModuleInterface):

    aluno_repository = AlunoRepository

    def setup(self):
        self.aluno_repository = AlunoRepository(self.app.database)

    def run(self):
        cursor = self.aluno_repository.all()
        alunos = cursor.fetchall()

        lista_alunos = []
        for tupla_aluno in alunos:
            aluno = Aluno()
            aluno.id = tupla_aluno[0]
            aluno.nome = tupla_aluno[1]
            aluno.documento = tupla_aluno[2]
            aluno.data_nascimento = tupla_aluno[3]
            lista_alunos.append(aluno)

        print_alunos(lista_alunos)