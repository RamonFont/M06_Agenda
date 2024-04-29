from abc import ABC, abstractmethod

class IAgenda(ABC):
    @abstractmethod
    def __init__(self, nombre: str, usuarios: list) -> None:
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
    def usuarios(self) -> list:
        pass
    
    @usuarios.setter
    @abstractmethod
    def usuarios(self, usuarios: list) -> None:
        pass
    
    @abstractmethod
    def agregar_usuario(self, usuario) -> None:
        pass
    
    @abstractmethod
    def eliminar_usuario(self, usuario) -> None:
        pass
    
    @abstractmethod
    def to_dict(self):
        pass
