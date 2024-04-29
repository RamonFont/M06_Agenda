import unittest
from UsuarioFuncionamiento import UsuarioFuncionamiento
from AgendaFuncionamiento import AgendaFuncionamiento
from MongoDB import MongoDBConnection

class TestUsuario(unittest.TestCase):

    def setUp(self):
        user = "talialopez"
        pwd = "1234"
        cluster = "talialopez.7zv3vwa"
        db_name = "agenda"

        self.mongo_connection = MongoDBConnection(user, pwd, cluster, db_name)
        
        self.agenda = AgendaFuncionamiento("Agenda Personal", [], self.mongo_connection)
        
        self.usuario = UsuarioFuncionamiento("Ramon Font", [self.agenda], self.mongo_connection)

    def test_agregar_agenda(self):
        nueva_agenda = AgendaFuncionamiento("Agenda de Trabajo", [], self.mongo_connection)
        
        self.usuario.agregar_agenda(nueva_agenda)
        
        self.assertIn(nueva_agenda, self.usuario.agendas)
        
    def test_eliminar_agenda(self):
        self.usuario.eliminar_agenda(self.agenda)
        
        self.assertNotIn(self.agenda, self.usuario.agendas)

if __name__ == '__main__':
    unittest.main()
