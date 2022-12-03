from Conexion import conexion
from usuario import Usuario
from usuario import UsuarioBase
from decoradoresUsuario import Cliente
from decoradoresUsuario import Empleado
from decoradoresUsuario import AgenteAtencionCliente



conn = conexion
if __name__ == "__main__":
    c=AgenteAtencionCliente
    c.generarReporteCliente(2,"dni")



