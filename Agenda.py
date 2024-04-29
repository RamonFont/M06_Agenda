from datetime import datetime
import unittest
from Evento import EventoPrincipal
from MongoDBEvento import MongoDB


class Agenda(unittest.TestCase):

    def setUp(self):
        self.mongodb_evento = MongoDB()

    def test_agregar_evento(self):
        evento = EventoPrincipal(1000, datetime.now(), "1 hora", "KPIS", "Valoración del último mes", ["tag1", "tag2"], "Barcelona")
        self.mongodb_evento.createE(evento)

        evento_agregado = self.mongodb_evento.getE(1564)
        self.assertIsNotNone(evento_agregado)

    def test_consultar_eventos_agenda(self):
        eventos = self.mongodb_evento.consultar_eventos()
        self.assertIsInstance(eventos, list)

if __name__ == '__main__':
    unittest.main()
