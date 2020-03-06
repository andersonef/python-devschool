from src.dev_school import DevSchool
from src.modules.alunos.modulo_cadastro import ModuloCadastro as ModuloCadastroAluno
from src.modules.alunos.modulo_listagem import ModuloListagem as ModuloListagemAlunos
app = DevSchool()

app.setup()
app.add_module(ModuloCadastroAluno(app), '1', 'Cadastrar Aluno')
app.add_module(ModuloListagemAlunos(app), '2', 'Listar Alunos')

app.run()
