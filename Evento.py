import datetime
from typing import List

class Evento:
    def __init__(self, fecha: datetime.datetime, duracion: datetime.timedelta, titulo: str, descripcion: str, tags: List[str], ubicacion: str):
        self._fecha = fecha
        self._duracion = duracion
        self._titulo = titulo
        self._descripcion = descripcion
        self._tags = tags
        self._ubicacion = ubicacion

    @property
    def fecha(self) -> datetime.datetime:
        return self._fecha
    
    @fecha.setter
    def fecha(self, value: datetime.datetime):
        self._fecha = value

    @property
    def duracion(self) -> datetime.timedelta:
        return self._duracion
    
    @duracion.setter
    def duracion(self, value: datetime.timedelta):
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
