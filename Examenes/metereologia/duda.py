import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx = lambda x: x* np.log(x)
# intervalo de integracion
a = 1
b = 4
tramos = 10

# Validar cantidad de tramos sea multiplo de 3
esmultiplo3 = tramos%3
while (esmultiplo3==1):
    tramos = int(input('Tramos es multiplo de 3: '))
    esmultiplo3 = tramos%3


# PROCEDIMIENTO
# Regla de Simpson de 5/8, varios tramos
h = b-a/tramos
xi = a

muestras = tramos + 1
xi = np.linspace(a, b, muestras)
fi = fx(xi)

# SALIDA
print(len(xi))
print(fi)
v = np.array([xi, fi])
print(v)
plt.plot(xi, fi,'g')
plt.show()
