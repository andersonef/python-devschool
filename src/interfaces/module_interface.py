import abc

class ModuleInterface(abc.ABC):

    app = None

    def __init__(self, app):
        self.app = app

    @abc.abstractmethod
    def setup(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass