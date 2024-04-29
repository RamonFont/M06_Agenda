from AgendaDAO import IAgenda
from MongoDB import MongoDBConnection


class AgendaFuncionamiento(IAgenda):
    def __init__(self, nombre: str, usuarios: list, db_connection: MongoDBConnection) -> None:
        self._nombre = nombre
        self._usuarios = usuarios
        self._db_connection = db_connection

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    @property
    def usuarios(self) -> list:
        return self._usuarios
    
    @usuarios.setter
    def usuarios(self, usuarios: list) -> None:
        self._usuarios = usuarios
    
    def agregar_usuario(self, usuario) -> None:
        self._usuarios.append(usuario)
        self._db_connection.db["agendas"].update_one({"nombre": self.nombre}, {"$set": self.to_dict()}, upsert=True)
    
    def eliminar_usuario(self, usuario) -> None:
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)
            self._db_connection.db["agendas"].update_one({"nombre": self.nombre}, {"$set": self.to_dict()}, upsert=True)
    
    def to_dict(self):
        return {"nombre": self.nombre, "usuarios": [usuario.to_dict() for usuario in self.usuarios]}