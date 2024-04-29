from bson import ObjectId
from typing import List, Optional
from EventoObjeto import EventoPrincipal
from AgendaDAO import IAgenda

class AgendaFuncionamiento(IAgenda):
    def __init__(self, agenda_id: ObjectId, nombre: str):
        self.agenda_id = agenda_id
        self.nombre = nombre
        self.usuarios = []  
        self.eventos = []  

    def agregar_usuario(self, usuario_id: ObjectId):
        if usuario_id not in self.usuarios:
            self.usuarios.append(usuario_id)

    def eliminar_usuario(self, usuario_id: ObjectId):
        self.usuarios = [uid for uid in self.usuarios if uid != usuario_id]

    def agregar_evento(self, evento: EventoPrincipal):
        self.eventos.append(evento)

    def eliminar_evento(self, evento_id: int):
        self.eventos = [evento for evento in self.eventos if evento.id != evento_id]

    def obtener_evento_por_id(self, evento_id: int) -> Optional[EventoPrincipal]:
        for evento in self.eventos:
            if evento.id == evento_id:
                return evento
        return None

    def listar_usuarios(self) -> List[ObjectId]:
        return self.usuarios

    def listar_eventos(self) -> List[EventoPrincipal]:
        return self.eventos

    def to_dict(self) -> dict:
        return {
            "agenda_id": self.agenda_id,
            "nombre": self.nombre,
            "usuarios": self.usuarios,
            "eventos": [evento.to_dict() for evento in self.eventos]
        }
