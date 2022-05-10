class Medicamentos:
        __idcama=None
        __idmed=None
        __nombre=''
        __monodroga=''
        __presentacion=''
        __cantidad=None
        __preciototal=float
        def __init__(self,idc,idm,nombre,droga,presentacion,cantidad,precio):
                self.__idcama=idc
                self.__idmed=idm
                self.__nombre=nombre
                self.__monodroga=droga
                self.__presentacion=presentacion
                self.__cantidad=cantidad
                self.__preciototal=precio
        def getIDcama(self):
                return self.__idcama
        def getIDmed(self):
                return self.__idmed
        def getNombremed(self):
                return self.__nombre
        def getDroga(self):
                return self.__monodroga
        def getPresentacion(self):
                return self.__presentacion
        def getCantidad(self):
                return self.__cantidad
        def getPrecio(self):
                return self.__preciototal
