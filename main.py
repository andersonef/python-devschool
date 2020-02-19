from dev_school import DevSchool
from engines.cadastrar_aluno_engine import CadastrarAlunoEngine

app = DevSchool()

app.add_engine(CadastrarAlunoEngine())

app.run()