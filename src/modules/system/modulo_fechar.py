import sys

from src.interfaces.module_interface import ModuleInterface


class ModuloFechar(ModuleInterface):

    def setup(self):
        pass

    def run(self):
        print('============== OBRIGADO POR UTILIZAR DEVSCHOOL ===============')
        print('ENCERRANDO...')
        sys.exit()
