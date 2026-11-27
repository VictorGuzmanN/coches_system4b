# from models import coches_model

# class CochesController:
#     pass
from models.coches_model import CochesModel

class CochesController:
    @staticmethod
    def insertar_coche(marca, color, modelo, velocidad, potencia, asientos):
        coche = CochesModel(marca, color, modelo, velocidad, potencia, asientos)
        respuesta = coche.insertar()
        del coche
        return respuesta

    @staticmethod
    def consultar_coches():
        return CochesModel.consultar()

    @staticmethod
    def buscar_coche(id):
        return CochesModel.buscar(id)

    @staticmethod
    def eliminar_coche(id):
        return CochesModel.eliminar(id)

    @staticmethod
    def modificar_coche(id, marca, color, modelo, velocidad, potencia, asientos):
        coche = CochesModel(marca, color, modelo, velocidad, potencia, asientos)
        respuesta = coche.actualizar(id)
        del coche
        return respuesta