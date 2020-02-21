import abc

class ModuleInterface(abc.ABC):

    @abc.abstractmethod
    def run(self, app):
        pass