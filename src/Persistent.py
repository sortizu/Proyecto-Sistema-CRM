from abc import ABC, abstractmethod
class Persistent(ABC):
    pass

class PersistentFactory(ABC):
    def agregar(persistent:Persistent):
        pass
    def listar() -> Persistent:
        pass
    def actualizar(persistent:Persistent):
        pass
    def eliminar(id):
        pass