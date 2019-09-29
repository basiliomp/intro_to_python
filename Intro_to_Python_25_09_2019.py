#!/usr/bin/env python
# coding: utf-8

# # My first _Jupyter Notebook_ !
# 

# In[ ]:


# Run in python Anaconda Prompt
conda create -n intropython python=3.7 jupyter numpy pandas matplotlib scikit-learn

#activate environment
conda activate intropython

# Run the following code (after the '$' sign)
(intropython)$ jupyter notebook
# Now you should be prompted with the jupyter app in a browser window.

# While on a jupyter notebook can get information on the methods we are prompted with using the shortcut shift + tab.


# # Assignment

# In[ ]:


# Pedir al usuario un tamaño de diámetro por teclado y calcular el área del círculo con el diámetro proporcionado. 
# Imprimir el resultado en pantalla.

# Solución inicial
diametro = input("Introduce el número correspondiente al diámetro del círculo: ")
area_circulo = ((float(diametro) / 2) ** 2) * 3.141592

print(area_circulo)


# In[ ]:


# Solución en una línea
print("El área es", ((float(input("Introduce el número correspondiente al diámetro del círculo: "))/2) ** 2) * 3.141592)

