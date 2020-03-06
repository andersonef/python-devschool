import re

from src.interfaces.module_interface import ModuleInterface
from src.modules.enderecos.entities.endereco import Endereco


class ModuloCadastro(ModuleInterface):

    endereco = Endereco()

    def setup(self):
        pass

    def run(self):
        print('================ CADASTRO DE ENDEREÇO =============')
        self.input_cep()
        self.endereco.rua = input('Nome da Rua: ')
        self.endereco.bairro = input('Bairro: ')
        self.endereco.cidade = input('Cidade: ')
        self.endereco.estado = input('Estado: ')
        self.endereco.numero = input('Número: ')

    def input_cep(self):
        try:
            cep = input('Informe o CEP: ')
            if not re.search('^[0-9]{5}\-[0-9]{3}$', cep):
                raise ValueError()
            self.endereco.cep = cep
        except ValueError:
            print('====> CEP INVÁLIDO <====')
            self.input_cep()