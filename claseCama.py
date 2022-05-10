class Cama:
    __id=None
    __habitacion= None
    __estado= None
    __nombre= ''
    __diagnostico=''
    __fechaint=''
    __fechalta=''
    def __init__(self,id,hab,est,nombre,apellido,diagnostico,fechaint,fechalta):
        self.__id=id
        self.__habitacion=hab
        self.__estado=est
        self.__nombre=nombre
        self.__diagnostico=diagnostico
        self.__fechaint=fechaint
        self.__fechalta=fechalta
    def getID(self):
        return self.__id
    def getHabitacion(self):
        return self.__habitacion
    def getEstado(self):
        return self.__estado
    def getNombre(self):
        return self.__nombre
    def getDiagnostico(self):
        return self.__diagnostico
    def getFechaint(self):
        return self.__fechaint
    def getFechalta(self):
        return self.__fechalta
    def __str__(self):
        cadena = "Paciente: {0:<32} Cama: {1:<5} Habitación: {2:<4}\n".format(self.__nombre, self.__id, self.__habitacion)
        cadena += "Diagnóstico: {0:<20} Fecha internación: {1:<10}\n".format(self.__diagnostico, self.__fechaint)
        cadena += "Fecha de alta: {0:<10}\n".format(self.__fechalta)
        return cadena

