import unittest
from EventoFuncionamiento import MongoDB
from EventoObjeto import EventoPrincipal

class TestEvento(unittest.TestCase):

    def setUp(self):
        self.mongo_connection = MongoDB()

    def test_crear_evento(self):
        evento = EventoPrincipal(1, "2024-04-19T10:00:00", "1 hour", "Sant Jordi", "Reunión de Marketing", ["tag1", "tag2"], "Nou Barris, Barcelona")
        self.mongo_connection.createE(evento)

        # Confirmamos que el evento se haya creado correctamente
        evento_creado = self.mongo_connection.getE(1)
        self.assertIsNotNone(evento_creado)
        self.assertEqual(evento_creado['_id'], 1)

    def test_actualizar_evento(self):
        evento = EventoPrincipal(2, "2024-04-19T12:00:00", "2 hours", "Rosas", "Merchandising", ["tag1", "tag2"], "Passeig de gracia, 15")
        self.mongo_connection.createE(evento)

        # Actualizamos el evento creado anteriormente
        nuevo_evento = EventoPrincipal(2, "2024-04-19T14:00:00", "3 hours", "Rosas", "Marketing", ["tag3"], "Trinxant, 128")
        self.mongo_connection.updateE(2, nuevo_evento)

        # Confirmamos que el evento se haya actualizado correctamente
        evento_actualizado = self.mongo_connection.getE(2)
        self.assertEqual(evento_actualizado['duracion'], "3 hours")

    def test_eliminar_evento(self):
        evento = EventoPrincipal(3, "2024-04-19T15:00:00", "1 hour", "Evento a eliminar", "Evento a eliminar", ["tag1", "tag2"], "Madrid")
        self.mongo_connection.createE(evento)

        # Eliminamos el evento
        self.mongo_connection.deleteE(3)

        # Confirmamos que el evento se haya eliminado correctamente
        evento_eliminado = self.mongo_connection.getE(3)
        self.assertIsNone(evento_eliminado)

if __name__ == '__main__':
    unittest.main()
