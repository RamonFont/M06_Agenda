from UsuarioDAO import IUsuario

class UsuarioObjeto(IUsuario):
    def __init__(self, nombre: str, agendas: list) -> None:
        self._nombre = nombre
        self._agendas = agendas
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    @property
    def agendas(self) -> list:
        return self._agendas
    
    @agendas.setter
    def agendas(self, agendas: list) -> None:
        self._agendas = agendas
    
    def agregar_agenda(self, agenda) -> None:
        self._agendas.append(agenda)
    
    def eliminar_agenda(self, agenda) -> None:
        if agenda in self._agendas:
            self._agendas.remove(agenda)
    
    def to_dict(self):
        return {"nombre": self.nombre, "agendas": self.agendas}
