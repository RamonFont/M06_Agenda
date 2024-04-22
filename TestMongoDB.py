import unittest
from datetime import datetime, timedelta
from MongoDBEvento import MongoDB
from Evento import EventoPrincipal


class TestMongoDB(unittest.TestCase):

    def setUp(self):
        self.mongodb_evento = MongoDB() 

    def test_crear_evento(self):
        evento = EventoPrincipal(1, datetime.now(), timedelta(hours=1), "Sant Jordi", "Reunión de Marketing", ["tag1", "tag2"], "Nou Barris, Barcelona")
        self.mongodb_evento.createE(evento)

        # Confirmamos que el evento se haya creado correctamente
        evento_creado = self.mongodb_evento.getE(1)
        self.assertIsNotNone(evento_creado)
        self.assertEqual(evento_creado['_id'], 1)

    def test_actualizar_evento(self):
        evento = EventoPrincipal(2, datetime.now(), timedelta(hours=2), "Rosas", "Merchandising", ["tag1", "tag2"], "Passeig de gracia, 15")
        self.mongodb_evento.createE(evento)

        # Actualizamos el evento creado anteriormente
        nuevo_evento = EventoPrincipal(2, datetime.now(), timedelta(hours=3), "Rosas", "Marketing", ["tag3"], "Trinxant, 128")
        self.mongodb_evento.updateE(2, nuevo_evento)

        # Confirmamos que el evento se haya actualizado correctamente
        evento_actualizado = self.mongodb_evento.getE(2)
        self.assertEqual(evento_actualizado['duracion'], timedelta(hours=3))

    def test_eliminar_evento(self):
        evento = EventoPrincipal(3, datetime.now(), timedelta(hours=1), "Evento a eliminar", "Evento a eliminar", ["tag1", "tag2"], "Madrid")
        self.mongodb_evento.createE(evento)

        # Eliminamos el evento
        self.mongodb_evento.deleteE(3)

        # Confirmamos que el evento se haya eliminado correctamente
        evento_eliminado = self.mongodb_evento.getE(3)
        self.assertIsNone(evento_eliminado)


if __name__ == '__main__':
    unittest.main()
