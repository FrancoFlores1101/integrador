import csv
from claseMeds import Medicamento
class manejadorMeds:
    __lista=[]
    def __init__(self):
        __lista=[]
    def leerCSV(self):
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for row in reader:
            if bandera:
                bandera=False
            else:
                instancia=Medicamento(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                self.__lista.append(instancia)
    def medicamentosPorcama(self,id):
        str=''
        total=0
        for Medicamento in self.__lista:
            if id == Medicamento.getIDcama():
                str+='{0:<15},{1:<15},{2:<15} {3:<15}\n'.format(Medicamento.getNombremed(),Medicamento.getPresentacion(),Medicamento.getCantidad(),Medicamento.getPrecio())
                total+= Medicamento.getCantidad() * Medicamento.getPrecio()
        return(str,total)
