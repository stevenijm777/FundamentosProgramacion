#!/usr/bin/env python
# coding: utf-8

# # Matrices

# In[1]:


# Importar Modulo
import numpy as np


# In[3]:


# iterar por elemento a un matriz
for i in range(filas): # [0,1,2] # 0
    for j in range(columnas): #[0,1,2,3] # 1
        print(Matriz[i,j])


# In[2]:


Matriz= np.random.randint(1,10,(3,4))
filas = Matriz.shape[0]
columnas = Matriz.shape[1]
print(filas)
print(columnas)
print(Matriz)


# In[ ]:


#recorrer por fila

for fila in range(filas):#[0,1,2]
    print(Matriz[fila,:])
    print()


# In[ ]:


#recorrer por columna

for columna in range(columnas):#[0,1,2,3]
    print(Matriz[:,columna])
    print()
print("#imprimr la columna 2 con todas sus filas")
print(Matriz[:,2])#imprimr la columna 2 con todas sus filas


# ## Operaciones básicas –Aritméticas.
#     * a.sum(axis=num_axis)
#     * a.prod(axis=num_axis)

# In[ ]:


# Sacar el total por fila 
l_T_fila = []
for fila in range(filas):#[0,1,2]
    T_fila = Matriz[fila,:].sum()
    l_T_fila.append(T_fila)
v_T_fila = np.array(l_T_fila)
print(v_T_fila)
v_filas = Matriz.sum(axis=1) # axis = 1 para iterar por filas
print("vector",v_filas)


# In[ ]:


# Sacar el total por columna
lista = []
for columna in range(columnas):#0
    total_Col = Matriz[:,columna].sum()
    lista.append(total_Col)
    print()
vector = np.array(lista)
print("vector",vector)
print("por axis = 0")
total_Cols = Matriz.sum(axis=0)
print(total_Cols)


# In[ ]:


#LLenar una MAtriz


#                  Jose             Juan            Pepe
#              1P    |  2P   | 1P    |  2P    |  1P    |  2P    |
# Matematicas: 71.73 | 91.68 | 81.71 | 61.89
#     Fisica : 65.4  | 59.2 

# In[ ]:


M = np.array([[ 71.73, 91.68, 81.71, 61.89, 21.79, 45.56],
            [ 65.4 , 59.2 , 63.6 , 88.4 , 68.7, 56.78 ]])
M


# In[ ]:


# quienes pasaron en matematica
promFinal = []
fila = 0
estudiantes = ["Jose","Juan","Pepe"]
l_Parcial  = ["1P","2P"]
cont_columna = 0
for ind_Est in range(estudiantes): #[0,1,2]
    ini_Columna =  ind_Est*len(l_Parcial)
    fin_Columna = ini_columna+len(L_parcial)
    vector = M[fila,ini_Columna:fin_Columna]
    


# In[4]:


import numpy as np 
letra_b = np.random.randint(1,15,(5,))
letra_i = np.random.randint(16,30,(5,))
letra_n = np.random.randint(31,45,(5,))
letra_g = np.random.randint(46,60,(5,))
letra_o = np.random.randint(61,75,(5,))
print(letra_b)
print(letra_i)
print(letra_n)
print(letra_g)
print(letra_o)
M = np.array(letra_b+letra_i+letra_n+letra_g+letra_o)
print(M)


# In[ ]:




