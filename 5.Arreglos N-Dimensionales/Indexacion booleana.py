#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([5,2,6])
b = np.array([3,2,7])
a<b


# In[14]:


A = np.random.randint(1,10,(3,3))
B = np.random.randint(1,10,(3,3))
print(A)
print()
print(B)
C = np.array([["A","B","c"],["D","E","F"],["G","H","I"]])
print()
print(C)


# In[ ]:


np.any(A ==9)


# In[15]:


A==B # se comparan los elementos que estan en la misma posicion


# In[16]:


C[A==B] # Devuelve el vector con los elementos que estan en la posicion donde se cumple la condicion


# In[11]:


A[B==A] 


# In[ ]:


c = np.ones((3,3))
c


# In[ ]:


c==1


# In[ ]:


np.all(c==2)


# In[ ]:


#np.where()
A = np.random.randint(1,10,(4,4))
print(A)


# In[ ]:


#np.where(A==1)
np.where(A==1)
for fila in np.where(A==1)


# In[ ]:




