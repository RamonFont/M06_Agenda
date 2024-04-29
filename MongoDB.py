import pymongo

class MongoDBConnection:
    def __init__(self, user, pwd, cluster, db_name):
        self.user = user
        self.pwd = pwd 
        self.cluster = cluster
        self.db_name = db_name
        self.connection = pymongo.MongoClient(f"mongodb+srv://{self.user}:{self.pwd}@{self.cluster}.mongodb.net/{self.db_name}?retryWrites=true&w=majority")
        self.db = self.connection[self.db_name]
