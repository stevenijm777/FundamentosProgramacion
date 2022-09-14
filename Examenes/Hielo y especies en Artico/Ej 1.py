import numpy as np

def cuadrantes(matriz): #(Cortesia del examen)
    f,c=matriz.shape
    f_mitad= f//2
    c_mitad=c//2
    Q1= matriz[:f_mitad, :c_mitad]
    Q2= matriz[:f_mitad, c_mitad:]
    Q3=matriz[f_mitad:, :c_mitad]
    Q4=matriz[f_mitad:, c_mitad:]
    return (Q1,Q2,Q3,Q4)

def poblacionEspecie(mAnimales, especie): #(Cortesia del examen)
    t=cuadrantes(mAnimales)
    totales=[]
    for Q in t:
        total=np.sum(Q==especie)
        totales.append(total)
    return tuple(totales)

dicEspecies={'0': 'Delfin',
             '1': 'Ballena',
             '2': 'Cocodrilo',
             '3': 'Venado',
             '4': 'Halcon',
             '5': 'Oso Polar',
             '6': 'Pez Globo'}

