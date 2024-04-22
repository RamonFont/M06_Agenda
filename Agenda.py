import unittest
from datetime import datetime, timedelta
from Evento import EventoPrincipal
from MongoDBEvento import MongoDB


class Agenda(unittest.TestCase):

    def setUp(self):
        self.mongodb_evento = MongoDB()

    def agregar_evento(self):
        evento = EventoPrincipal(1, datetime.now(), timedelta(hours=1), "KPIS", "Valoración del último mes", ["tag1", "tag2"], "Barcelona")
        self.mongodb_evento.createE(evento)

        evento_agregado = self.mongodb_evento.getE(1)
        self.assertIsNotNone(evento_agregado)

    def consultar_eventos_agenda(self):
        eventos = self.mongodb_evento.consultar_eventos()
        self.assertIsInstance(eventos, list)

if __name__ == '__main__':
    unittest.main()
