import unittest
from AgendaFuncionamiento import AgendaFuncionamiento
from UsuarioFuncionamiento import UsuarioFuncionamiento
from MongoDB import MongoDBConnection

class TestAgenda(unittest.TestCase):

    def setUp(self):
        user = "talialopez"
        pwd = "1234"
        cluster = "talialopez.7zv3vwa"
        db_name = "agenda"

        self.mongo_connection = MongoDBConnection(user, pwd, cluster, db_name)
        
        self.usuario = UsuarioFuncionamiento("Ramon Font", [], self.mongo_connection)
        self.agenda = AgendaFuncionamiento("Agenda de Trabajo", [self.usuario], self.mongo_connection)

    def test_agregar_usuario(self):
        nuevo_usuario = UsuarioFuncionamiento("Talia López", [], self.mongo_connection)
        
        self.agenda.agregar_usuario(nuevo_usuario)
        
        self.assertIn(nuevo_usuario, self.agenda.usuarios)
        
    def test_eliminar_usuario(self):
        self.agenda.eliminar_usuario(self.usuario)
        
        self.assertNotIn(self.usuario, self.agenda.usuarios)

if __name__ == '__main__':
    unittest.main()
