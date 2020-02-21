from datetime import date

from src.interfaces.module_interface import ModuleInterface
from src.modules.alunos.entities.aluno import Aluno
from src.modules.enderecos.modulo_cadastro import ModuloCadastro as ModuloCadastroEndereco


class ModuloCadastro(ModuleInterface):

    aluno = Aluno()

    def run(self, app):
        print('=============== CADASTRO DE ALUNO ==================')
        for x in range(3): print('')
        self.aluno.nome = input('Nome Completo: ')
        self.aluno.documento = input('Informe o Documento: ')
        self.input_data_nascimento()
        self.input_endereco()

        print('=============== CONFIRME OS DADOS =================')
        print(self.aluno)

    def input_endereco(self):
        modulo_endereco = ModuloCadastroEndereco()
        modulo_endereco.run(None)
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
