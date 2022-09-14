import random as rd

# 1
muestras = []
cant = len(muestras)
while (cant<10):
    num = rd.randint(6, 20)
    if num not in muestras:
        muestras.append(num)
    cant = len(muestras)

copyMuestra = muestras[0:len(muestras):1]
efectividades = []

# 2.

for i in range(15):
    # 2.1 desordenar lista
    rd.shuffle(muestras)
    # 2.2
    mezclas = 0
    for j in range(len(muestras)):
        numAnterior = copyMuestra[j]
        numNuevo = muestras[j]
        if numNuevo != numAnterior:
            mezclas += 1
    copyMuestra = muestras[::]
    # calcular el porcentaje de efectividad
    efectividad = mezclas * 100 / len(muestras)
    efectividades.append(efectividad)

# 3.
efecFinal = sum(efectividades) / 100
print("El porcentaje de efectividad final es: ", efecFinal)