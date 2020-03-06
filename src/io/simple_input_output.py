from os.path import join


class SimpleInputOutput:

    def input(self, msg, required, values=None):
        try:
            value = input(msg)
            if required and len(value) < 1:
                raise ValueError('ERRO: É obrigatório informar uma resposta.')

            if values and value not in values:
                raise ValueError('ERRO: É obrigatório que sua resposta seja uma das opções: [' + ','.join(str(v) for v in values) + ']')

            return str(value)

        except ValueError as e:
            print(e)
            self.input(msg, required, values)
