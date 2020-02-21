from src.interfaces.module_interface import ModuleInterface


class DevSchool:

    modules = {}

    def add_module(self, module: ModuleInterface, menu_option: str, menu_text: str):
        self.modules[menu_option] = {'text': menu_text, 'module': module}


    def run(self):

        while True:
            print('BEM VINDO AO DEVSCHOOL - ESCOLHA UMA OPÇÃO DO MENU')
            for key in self.modules:
                msg_option = str(key) + ' - ' + self.modules[key]['text']
                print(msg_option)
            selected_option = self.ask_user_option()

            self.modules[selected_option]['module'].run(self)


    def ask_user_option(self):
        user_option = input('Sua Opção: ')
        try:
            if int(user_option) not in self.modules:
                raise ValueError()
            return int(user_option)
        except ValueError:
            print('OPÇÃO INVÁLIDA! Tente novamente.')
            return self.ask_user_option()
