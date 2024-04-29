from abc import ABC, abstractmethod
from typing import List
from bson import ObjectId
from EventoObjeto import EventoPrincipal

class IAgenda(ABC):

    @abstractmethod
    def agregar_usuario(self, usuario_id: ObjectId):
        pass

    @abstractmethod
    def eliminar_usuario(self, usuario_id: ObjectId):
        pass

    @abstractmethod
    def agregar_evento(self, evento: EventoPrincipal):
        pass

    @abstractmethod
    def eliminar_evento(self, evento_id: int):
        pass

    @abstractmethod
    def obtener_evento_por_id(self, evento_id: int):
        pass

    @abstractmethod
    def listar_usuarios(self):
        pass

    @abstractmethod
    def listar_eventos(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
