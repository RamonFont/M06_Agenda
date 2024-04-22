import pymongo
from EventoDAO import EventoI

class MongoDB(EventoI):
    def __init__(self, user, pwd, cluster):
        self.user = user
        self.pwd = pwd 
        self.cluster = cluster
        self.url = f"mongodb+srv://{self.user}:{self.pwd}@{self.cluster}.mongodb.net/"
        self.connection = None
        self.db = None
        self.eventos_collection = None

    def connect(self):
        try:
            self.connection = pymongo.MongoClient(self.url)
            self.db = self.connection['agenda']
            self.eventos_collection = self.db['eventos']
            print("Connected to MongoDB Atlas!")
        except Exception as e:
            print(f"Error connecting to MongoDB Atlas: {e}")

    def createE(self, evento):
        if not self.connection or not self.db or not self.eventos_collection:
            print("Error: Connection to MongoDB Atlas is not established.")
            return

        evento_dict = evento.to_dict()
        self.eventos_collection.insert_one(evento_dict)

    def getE(self, id_evento):
        if not self.connection or not self.db or not self.eventos_collection:
            print("Error: Connection to MongoDB Atlas is not established.")
            return None

        return self.eventos_collection.find_one({"_id": id_evento})

    def deleteE(self, id_evento):
        if not self.connection or not self.db or not self.eventos_collection:
            print("Error: Connection to MongoDB Atlas is not established.")
            return

        self.eventos_collection.delete_one({"_id": id_evento})

    def updateE(self, id_evento, nuevo_evento):
        if not self.connection or not self.db or not self.eventos_collection:
            print("Error: Connection to MongoDB Atlas is not established.")
            return

        nuevo_evento_dict = nuevo_evento.to_dict()
        self.eventos_collection.update_one({"_id": id_evento}, {"$set": nuevo_evento_dict})
