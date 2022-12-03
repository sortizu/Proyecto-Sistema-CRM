from abc import ABC, abstractmethod


class Cupon(ABC):
    def __init__(self) -> None:
        self._descripcion = "Cualquier cupon"
        self._nombre = "CU"

    def set_descripcion(self, valor: str) -> None:
        self._descripcion = valor

    def get_descripcion(self) -> str:
        return self._descripcion

    def set_nombre(self, valor: str) -> None:
        self._nombre = valor

    def get_nombre(self) -> str:
        return self._nombre

    @abstractmethod
    def calcular_descuento(self) -> float:
        raise NotImplementedError


class CuponEmp(Cupon):
    def __init__(self) -> None:
        self._descripcion = "Cupon de empleados"
        self._nombre = "CUE"

    def calcular_descuento(self) -> float:
        return 0.00


class CuponCli(Cupon):
    def __init__(self) -> None:
        self._descripcion = "Cupon de clientes"
        self._nombre = "CUC"

    def calcular_descuento(self) -> float:
        return 0.00
