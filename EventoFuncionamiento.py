import pymongo
from EventoDAO import EventoI

class MongoDB(EventoI):

    def __init__(self):
        self.user = "talialopez"
        self.pwd = "1234" 
        self.cluster = "talialopez.7zv3vwa"
        self.db_name = "agenda"
        self.collection_name = "evento"
        self.uri = f"mongodb+srv://{self.user}:{self.pwd}@{self.cluster}.mongodb.net/{self.db_name}?retryWrites=true&w=majority"
        self.connection = pymongo.MongoClient(self.uri)
        self.db = self.connection[self.db_name]
        self.eventos_collection = self.db[self.collection_name]
        
    def createE(self, evento):
        evento_dict = evento.to_dict()
        self.eventos_collection.insert_one(evento_dict)

    def getE(self, id_evento):
        return self.eventos_collection.find_one({"_id": id_evento})

    def deleteE(self, id_evento):
        self.eventos_collection.delete_one({"_id": id_evento})

    def updateE(self, id_evento, nuevo_evento):
        nuevo_evento_dict = nuevo_evento.to_dict()
        self.eventos_collection.update_one({"_id": id_evento}, {"$set": nuevo_evento_dict})

    def consultar_eventos(self):
        print("Consultando eventos...")
        eventos = self.eventos_collection.find()  
        eventos_lista = list(eventos)  
        print("Eventos encontrados:", eventos_lista)
        return eventos_lista