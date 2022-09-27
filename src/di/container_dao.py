from pymongo import MongoClient


class ContainerDAO:
    def __init__(self, container_general):
        self.container_general = container_general
        self._mongo = None

    @property
    def mongo(self):
        if self._mongo is None:
            return MongoClient(
                "mongodb+srv://Chaddi:wfii123098@cluster0.q4d5v9j.mongodb.net/?retryWrites=true&w=majority"
            )
