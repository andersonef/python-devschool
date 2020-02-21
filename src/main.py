from src.dev_school import DevSchool
from src.modules.alunos.modulo_cadastro import ModuloCadastro as ModuloCadastroAluno

app = DevSchool()

app.add_module(ModuloCadastroAluno(), 1, 'Cadastrar Aluno')

app.run()