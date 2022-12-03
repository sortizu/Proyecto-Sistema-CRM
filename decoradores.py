from abc import abstractmethod
from cupon import Cupon


class Decorador(Cupon):
    @abstractmethod
    def get_descripcion(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def calcular_descuento(self) -> float:
        raise NotImplementedError


class Cupon05(Decorador):
    def __init__(self, cupon: Cupon) -> None:
        self.__cupon = cupon

    def get_descripcion(self) -> str:
        return f"{self.__cupon.get_descripcion()}, con 5 por ciento de descuento"

    def get_nombre(self) -> str:
        return f"{self.__cupon.get_nombre()}05"

    def calcular_descuento(self) -> float:
        return self.__cupon.calcular_descuento()+0.05


class Cupon10(Decorador):
    def __init__(self, cupon: Cupon) -> None:
        self.__cupon = cupon

    def get_descripcion(self) -> str:
        return f"{self.__cupon.get_descripcion()}, con 10 por ciento de descuento"

    def get_nombre(self) -> str:
        return f"{self.__cupon.get_nombre()}10"

    def calcular_descuento(self) -> float:
        return self.__cupon.calcular_descuento()+0.10


class Cupon15(Decorador):
    def __init__(self, cupon: Cupon) -> None:
        self.__cupon = cupon

    def get_descripcion(self) -> str:
        return f"{self.__cupon.get_descripcion()}, con 15 por ciento de descuento"

    def get_nombre(self) -> str:
        return f"{self.__cupon.get_nombre()}15"

    def calcular_descuento(self) -> float:
        return self.__cupon.calcular_descuento()+0.15
