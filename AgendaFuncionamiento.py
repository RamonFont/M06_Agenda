class PersistenciaAgenda:
    def __init__(self, nombre: str, eventos: list, usuarios: list) -> None:
        self._nombre = nombre
        self._eventos = eventos
        self._usuarios = usuarios
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
        
    
    @property
    def eventos(self) -> list:
        return self._eventos
    
    @eventos.setter
    def eventos(self, eventos: list) -> None:
        self._eventos = eventos
    
    
    @property
    def usuarios(self) -> list:
        return self._usuarios
    
    @usuarios.setter
    def usuarios(self, usuarios: list) -> None:
        self._usuarios = usuarios
    
    
    def agregar_evento(self, evento) -> None:
        self._eventos.append(evento)
        
    def to_dict(self):
        return {"nombre": self.nombre, "eventos": self.eventos, "usuarios": self.usuarios}
