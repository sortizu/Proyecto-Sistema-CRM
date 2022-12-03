from cupon import Cupon, CuponCli, CuponEmp
from decoradores import Cupon05, Cupon10, Cupon15


def ver_detalle(cupon: Cupon) -> None:
    print(f"CUPON: {cupon.get_nombre()}, DESCRIPCION: {cupon.get_descripcion()}, DESCUENTA: {cupon.calcular_descuento()}")


if __name__ == "__main__":
    cupon01 = CuponCli()
    cupon01 = Cupon10(cupon01)
    ver_detalle(cupon01)
