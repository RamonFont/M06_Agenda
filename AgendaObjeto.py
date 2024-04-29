from typing import List
from bson import ObjectId
from EventoObjeto import EventoPrincipal

class Agenda:
    def __init__(self, agenda_id: ObjectId, nombre: str, usuarios: List[ObjectId], eventos: List[EventoPrincipal]):
        self.agenda_id = agenda_id
        self.nombre = nombre
        self.usuarios = usuarios
        self.eventos = eventos

    def agregar_usuario(self, usuario_id: ObjectId):
        if usuario_id not in self.usuarios:
            self.usuarios.append(usuario_id)

    def eliminar_usuario(self, usuario_id: ObjectId):
        self.usuarios = [uid for uid in self.usuarios if uid != usuario_id]

    def agregar_evento(self, evento: EventoPrincipal):
        self.eventos.append(evento)

    def eliminar_evento(self, evento_id: int):
        self.eventos = [evento for evento in self.eventos if evento.id != evento_id]

    def to_dict(self):
        return {
            "agenda_id": self.agenda_id,
            "nombre": self.nombre,
            "usuarios": self.usuarios,
            "eventos": [evento.to_dict() for evento in self.eventos]
        }
