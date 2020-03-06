from datetime import date

from src.interfaces.module_interface import ModuleInterface
from src.modules.alunos.aluno_presenter import print_aluno
from src.modules.alunos.entities.aluno import Aluno
from src.modules.alunos.repositories.aluno_repository import AlunoRepository
from src.modules.enderecos.modulo_cadastro import ModuloCadastro as ModuloCadastroEndereco


class ModuloCadastro(ModuleInterface):

    aluno = None

    aluno_repository = AlunoRepository

    def setup(self):
        self.aluno = Aluno()
        self.aluno_repository = AlunoRepository(self.app.database)

        try:
            self.app.database.execute('CREATE TABLE Alunos('
                                 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                 'nome VARCHAR(50), '
                                 'documento VARCHAR(20), '
                                 'data_nascimento DATETIME '
                                 ');')
            self.app.database.commit()
        except:
            pass

    def run(self):
        print('=============== CADASTRO DE ALUNO ==================')
        for x in range(3): print('')
        self.aluno.nome = input('Nome Completo: ')
        self.aluno.documento = input('Informe o Documento: ')
        self.input_data_nascimento()
        # self.input_endereco()

        print('=============== CONFIRME OS DADOS =================')
        print_aluno(self.aluno)
        dados_ok = self.app.io.input('Os dados estão corretos? (s/n): ', True, ('s', 'n'))
        if dados_ok == 'n':
            return self.run()
        print('Salvando aluno no banco de dados, aguarde...')
        self.aluno_repository.save(self.aluno)
        print(f'Aluno salvo. ID: {self.aluno.id}')
        print('Voltando ao menu principal')

    def input_endereco(self):
        modulo_endereco = ModuloCadastroEndereco(self.app)
        modulo_endereco.run()
        self.aluno.endereco = modulo_endereco.endereco

    def input_data_nascimento(self):
        try:
            data = input('Data de Nascimento (dd/mm/yyyy): ')
            partes = data.split('/')
            if len(partes) < 3:
                raise ValueError()
            date(int(partes[2]), int(partes[1]), int(partes[0]))
            self.aluno.data_nascimento = data
        except (ValueError, TypeError) as e:
            print('=======> ERRO - DATA INVÁLIDA <=======')
            self.input_data_nascimento()
