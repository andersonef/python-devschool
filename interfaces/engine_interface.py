import abc

class EngineInterface(abc.ABC):

    @abc.abstractmethod
    def menu_text(self):
        pass

    @abc.abstractmethod
    def menu_required_option(self) -> int:
        pass

    @abc.abstractmethod
    def run(self, app):
        pass