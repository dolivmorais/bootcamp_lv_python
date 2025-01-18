#%%
#bibliotecas
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd


#exercicio 1
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
# %%
def area_quadrado(lado):
    area = lado**2
    return area

def area_triangulo(base, altura):
    area = (base*altura)/2
    return area

def area_retangulo(base, altura):
    area = base*altura
    return area

q = area_quadrado(5)
t = area_triangulo(5, 6)
r = area_retangulo(5, 6)
print("A area do quadrado e: ", q)
print("A area do triangulo e: ", t)
print("A area do retangulo e: ", r)
# %%
#json
import pprint
pprint({"chave1": "valor1", "chave2": "valor2"})
# %%
