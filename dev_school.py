from interfaces.engine_interface import EngineInterface


class DevSchool:

    engines = {}

    def add_engine(self, engine: EngineInterface):
        self.engines[engine.menu_required_option()] = engine


    def run(self):

        while True:
            print('BEM VINDO AO DEVSCHOOL - ESCOLHA UMA OPÇÃO DO MENU')
            for engine_key in self.engines:
                msg_option = str(self.engines[engine_key].menu_required_option())
                msg_option += ' - ' + self.engines[engine_key].menu_text()
                print(msg_option)
            selected_option = self.ask_user_option()

            self.engines[selected_option].run(self)


    def ask_user_option(self):
        user_option = input('Sua Opção: ')
        try:
            if int(user_option) not in self.engines:
                raise ValueError()
            return int(user_option)
        except ValueError:
            print('OPÇÃO INVÁLIDA! Tente novamente.')
            return self.ask_user_option()
