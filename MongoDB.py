import pymongo

class MongoDBConnection:
    def __init__(self, user: str, pwd: str, cluster: str, db_name: str) -> None:
        self.user = user
        self.pwd = pwd
        self.cluster = cluster
        self.db_name = db_name
        self.uri = f"mongodb+srv://{self.user}:{self.pwd}@{self.cluster}.mongodb.net/{self.db_name}?retryWrites=true&w=majority"
        self.connection = pymongo.MongoClient(self.uri)
        self.db = self.connection[self.db_name]
        self.eventos_collection = self.db["evento"]

