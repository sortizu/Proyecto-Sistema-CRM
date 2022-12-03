from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class ProductosIterator(Iterator):
    _position: int = None

    """
   indica la dirección contraria
    """
    _reverse: bool = False

    def __init__(self, collection: ProductsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        retorna el siguiente item de la coleccion o termina el recorrido si ya es el ultimo
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class ProductsCollection(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> ProductosIterator:
        return ProductosIterator(self._collection)

    def get_reverse_iterator(self) -> ProductosIterator:
        return ProductosIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = ProductsCollection()
    collection.add_item("Huawei P50 Pro 256GB")
    collection.add_item("ZTE Blade A51 32GB Gris")
    collection.add_item("Motorola Moto E20 32GB G Grafito")

    print("Recorrido de la colección:")
    print("\n".join(collection))
    print("")

    print("Recorrido en reversa:")
    print("\n".join(collection.get_reverse_iterator()), end="")
