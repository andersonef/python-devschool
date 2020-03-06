from src.interfaces.module_interface import ModuleInterface
import sqlite3
import os

from src.io.simple_input_output import SimpleInputOutput
from src.modules.system.modulo_fechar import ModuloFechar


class DevSchool:

    modules = {}

    database_name = 'database.db'

    database = None

    io = SimpleInputOutput()

    def setup(self):
        if not os.path.isfile(self.database_name):
            open(self.database_name, 'a').close()
        self.database = sqlite3.connect(self.database_name)
        self.add_module(ModuloFechar(self), 'x', 'Encerrar Programa')

    def add_module(self, module: ModuleInterface, menu_option: str, menu_text: str):
        if menu_option in self.modules:
            raise ValueError(f'Essa menu_option ({menu_option}) já está cadastrada pra algum módulo.')

        module.setup()
        self.modules[menu_option] = {'text': menu_text, 'module': module}

    def run(self):
        while True:
            print('BEM VINDO AO DEVSCHOOL - ESCOLHA UMA OPÇÃO DO MENU')
            for key in self.modules:
                msg_option = str(key) + ' - ' + self.modules[key]['text']
                print(msg_option)
            selected_option = self.io.input('Sua opção: ', True, self.modules.keys())

            self.modules[selected_option]['module'].run()