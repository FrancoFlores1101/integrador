import csv
import numpy as np
from claseCama import Cama
from datetime import date
from ManejadorMedicamentos import manejadorMeds

class manejadorCamas:
    __arreglo=None
    def __init__(self):
        self.__arreglo=np.empty(30,dtype=Cama)
    def leerCSV(self):
        archivo=open('camas.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        i=0
        for row in reader:
            if bandera:
                bandera=False
            else:
                instancia=Cama(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                self.__arreglo[i]=instancia
                i+=1
    def buscarPaciente(self,nombre):
        i=0
        while i<30 and self.__arreglo[i].getNombre.lower() != nombre.lower():
            i+=1
        if i==30:
            i=-1
        return i

    def darAltaPaciente(self,unmanejador:manejadorMeds):
        n=input('ingrese el nombre del paciente a dar el alta')
        i=self.buscarPaciente(n)
        if i != -1 and self.__arreglo[i].getEstado():
            fecha=date.today()
            fecha="{0}/{1}/{2}".format(fecha.day,fecha.month,fecha.year)
            self.__arreglo[i].darAlta(fecha)
            str,total=unmanejador.medicamentosPorcama(self.__arreglo[i].getID)
            print(str)
            print('total: {0}'.format(total))
        else:
            print('ERROR: El paciente no existe o fue dado de alta')
    def listarpacientes(self):
        diag=input('ingrese diagnostico a listar')
        for Cama in self.__arreglo
            if Cama.getDiagnostico() == diag and Cama.getEstado():
                print('{0:<15},{1:<15}'.format(Cama.getNombre(),Cama.getFechaint()))
