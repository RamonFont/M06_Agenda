from abc import ABC, abstractmethod

class EventoI(ABC):

    @abstractmethod
    def createE(self, evento):
        pass

    @abstractmethod
    def getE(self, id_evento):
        pass

    @abstractmethod
    def deleteE(self, id_evento):
        pass

    @abstractmethod
    def updateE(self, id_evento):
        pass