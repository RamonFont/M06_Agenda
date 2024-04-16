from abc import ABC, abstractmethod

class Evento(ABC):
    @abstractmethod
    def createE(self):
        pass

    def deleteE(self):
        pass

    def updateE(self):
        pass

    def getE(self):
        pass