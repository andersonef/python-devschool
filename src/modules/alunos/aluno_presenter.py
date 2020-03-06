from src.modules.alunos.entities.aluno import Aluno

ROW_LENGTH = 120


def print_aluno(aluno: Aluno):
    print('=' * ROW_LENGTH)
    print(texto_centralizado('DADOS DO ALUNO', ROW_LENGTH))
    print(f'| Nome: {aluno.nome}'.ljust(ROW_LENGTH, ' ') + '|')
    print(f'| Documento: {aluno.documento}'.ljust(ROW_LENGTH, ' ') + '|')
    print(f'| Nome: {aluno.data_nascimento}'.ljust(ROW_LENGTH, ' ') + '|')
    print('=' * ROW_LENGTH)


def print_alunos(alunos: list):
    print('=' * ROW_LENGTH)
    header = texto_centralizado('ID', 5)
    header += texto_centralizado('NOME', 55)
    header += texto_centralizado('DOCUMENTO', 30)
    header += texto_centralizado('DATA DE NASCIMENTO', 30)
    print(header)
    for aluno in alunos:
        linha = texto_centralizado(aluno.id, 5)
        linha += texto_centralizado(aluno.nome, 55)
        linha += texto_centralizado(aluno.documento, 30)
        linha += texto_centralizado(aluno.data_nascimento, 30)
        print(linha)


def texto_centralizado(texto, tamanho):
    texto = str(texto)
    margem = int((tamanho / 2) - (len(texto) / 2))-1
    retorno = '|' + ' ' * margem + texto + ' ' * (margem-1) + '|'
    return retorno
