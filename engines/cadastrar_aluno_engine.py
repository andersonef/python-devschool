from interfaces.engine_interface import EngineInterface


class CadastrarAlunoEngine(EngineInterface):

    def menu_text(self):
        return 'Cadastrar Aluno'

    def menu_required_option(self):
        return 1

    def run(self, app):
        print('Aluno cadastrado bicho!')