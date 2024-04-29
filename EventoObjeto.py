from typing import List

class EventoPrincipal:
    def __init__(self, id: int, fecha: str, duracion: str, titulo: str, descripcion: str, tags: List[str], ubicacion: str):
        self._id = id
        self._fecha = fecha
        self._duracion = duracion
        self._titulo = titulo
        self._descripcion = descripcion
        self._tags = tags
        self._ubicacion = ubicacion

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id:int) -> None:
        self._id = id

    @property
    def fecha(self) -> str:
        return self._fecha
    
    @fecha.setter
    def fecha(self, value: str):
        self._fecha = value

    @property
    def duracion(self) -> str:
        return self._duracion
    
    @duracion.setter
    def duracion(self, value: str):
        self._duracion = value

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, value: str):
        self._titulo = value

    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, value: str):
        self._descripcion = value

    @property
    def tags(self) -> List[str]:
        return self._tags
    
    @tags.setter
    def tags(self, value: List[str]):
        self._tags = value

    @property
    def ubicacion(self) -> str:
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, value: str):
        self._ubicacion = value

    def to_dict(self):
        return {"_id": self._id, "fecha": self.fecha, "duracion": self.duracion, "titulo": self.titulo, "descripcion": self.descripcion, "tags": self.tags, "ubicacion": self.ubicacion}