import datetime
from typing import List


class Evento:
    def __init__(self, fecha: datetime, duracion: datetime.timedelta, titulo: str, descripcion: str, tags: List[str], ubicacion: str):
        self.fecha = fecha
        self.duracion = duracion
        self.titulo = titulo
        self.descripcion = descripcion
        self.tags = tags
        self.ubicacion = ubicacion

    def fecha(self) -> datetime:
        return self.fecha
    
    def fecha(self, value: datetime):
        self.fecha = value

    def duracion(self) -> datetime.timedelta:
        return self.duracion
    
    def duracion(self, value:datetime.timedelta):
        self.duracion = value

    def titulo(self) -> str:
        return self.titulo
    
    def titulo(self, value:str):
        self.titulo = value

    def descripcion(self) -> str:
        return self.descripcion
    
    def descripcion(self, value:str):
        self.descripcion = value

    def tags(self) -> List[str]:
        return self.tags
    
    def tags(self, value:List[str]):
        self.tags = value

    def ubicacion(self) -> str:
        return self.ubicacion
    
    def ubicacion(self, value:str):
        self.ubicacion = value