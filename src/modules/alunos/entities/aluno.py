from src.modules.enderecos.entities.endereco import Endereco


class Aluno:
    id = int
    nome = str
    documento = str
    data_nascimento = str
    endereco = Endereco
