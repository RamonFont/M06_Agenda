from abc import ABC, abstractmethod

class IUsuario(ABC):
    @abstractmethod
    def __init__(self, nombre: str, agendas: list) -> None:
        pass
    
    @property
    @abstractmethod
    def nombre(self) -> str:
        pass
    
    @nombre.setter
    @abstractmethod
    def nombre(self, nombre: str) -> None:
        pass
        
    @property
    @abstractmethod
    def agendas(self) -> list:
        pass
    
    @agendas.setter
    @abstractmethod
    def agendas(self, agendas: list) -> None:
        pass
    
    @abstractmethod
    def agregar_agenda(self, agenda) -> None:
        pass

    @abstractmethod
    def eliminar_agenda(self, agenda) -> None:
        pass

    @abstractmethod
    def to_dict(self):
        pass
