from cliente import Cliente
class Fiado:
    def __init__(self, compra):
        self.__id = compra.id
        self.__mercadoria = compra.l_compras
        self.__cliente_f = compra.cliente_c