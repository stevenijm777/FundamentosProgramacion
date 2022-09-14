#!/usr/bin/env python
# coding: utf-8

# # Numpy

# Los arreglos pueden realizar operaciones con datos numéricos mucho más rápido, y en general son más eficientes que las listas.
# * Una colección de elementos que son todos del mismo tipo (float o int)
# * Una o más dimensiones (2)
# * Que son indexados por una tupla de enteros no negativos.

# In[2]:


# importar Modulo
import numpy as np


# In[ ]:


# crear un vector
# np.array(Lista, tipo)
vector1 = np.array([1,5,7,9.5])
vector2 = vector1.copy()
vector2+=1
print(vector1)
print(vector2)


# In[ ]:


# A.tolist()
lista = vector1.tolist()
lista


# In[ ]:


notas= np.array([ 4.13 , 3.76, 3.68, 1.62 , 8.77, 8.70, 8.89, 6.75])
notas[-1]


# In[ ]:


print(vector1.size)


# In[ ]:


print(vector1.shape)


# In[ ]:


M = np.array([[0,1,2,3],[1,1,1,1],[2,2,2,2]],float)
lista = M.tolist()
lista


# In[ ]:


M.shape


# In[ ]:


#Matriz
M = np.array([[2,4,6,8],[8,10,12,14]])
M


# In[ ]:


M.size


# In[ ]:


M.shape


# In[ ]:


np.zeros((5,5))


# In[ ]:


np.ones(M.shape)


# In[ ]:


np.full(M.shape,10,int)


# In[3]:


# retorna una matriz 
# np.random.randint(desde, hasta_sinIncluir, size = (fil,cols))
A=np.random.randint(5,11,size=(2,3))
A


# In[4]:


# reordena una matriz
B=A.reshape((3,2))
B


# In[5]:


B.reshape((6,))


# In[ ]:


C = np.arange(9,0,-1)
C


#                  Jose             Juan
#              1P    |  2P   | 1P    |  2P
# Matematicas: 71.73 | 91.68 | 81.71 | 61.89
#     Fisica :

# In[ ]:


C.dtype


# In[6]:


M = np.array([[ 71.73, 91.68, 81.71, 61.89, 21.79, 45.56],
              [ 65.4 , 59.2 , 63.6 , 88.4 , 68.7, 56.78 ],
              [ 68.4 , 79.2 , 53.6 , 48.4 , 98.7, 56.78 ]])
M


# nom_Matriz[ini_Fila:Fin_Fila, Ini_Col:Fin_Col]
# nom_Matriz[:,:]
# nom_Matriz[fila,columna] # sacar un elemento de mi matriz
# 

# In[7]:


# Sacar la segunda fila
# Sacar toda una fila
# M[fila,:]
M[1,:]


# In[ ]:


# Sacar toda una columna
# M[:,columna]
# Sacar la tercera columna
M[:,2]


# In[ ]:


# Sacar un elemento de la Matriz
# M[fila, columna]
M[1,1]


# In[ ]:


# Sacar una parte de la matriz
# Sacar notas de jose
M [:,0:2]


# In[ ]:


# Slicing a una Matriz
# M[iniFila: finFila, iniCol: finCol]


# In[ ]:


Matriz = np.random.randint(1,10, size = (5,10))
Matriz


# In[ ]:


Matriz[3,:]


# In[ ]:


Matriz2 = np.array([[ 1.73, 1.68, 1.71, 1.89, 1.79],
                    [ 65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])
Matriz2[:,1:3] -= 10

print("2....")
print(Matriz2)


# In[ ]:


a =10 #20
a-=10
print(a)


# In[ ]:


lista = [1,9,8]

lista = lista[:2]
print(lista)


# In[ ]:




