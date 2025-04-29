""" Escreva um script Python que execute as seguintes etapas:
# Use a lista de números: [12, 45, 67, 23, 89, 34, 22, 90, 56, 78].
# Calcule a média dos números usando a biblioteca numpy.
# Identifique os números que são maiores que a média.
# Armazene os números maiores que a média em um DataFrame do pandas.
# Salve o DataFrame em um arquivo CSV chamado "numeros_maiores_que_media.csv"""


import numpy as np
import pandas as pd

# criando o array de numeros e um array vazio
lista = np.array([12, 45, 67, 23, 89, 34, 22, 90, 56, 78])
maiores = []

media = (np.mean(lista))
print ("A média é", media)

# iterando a lista e adicionado os números maiores que a média no array maiores
for numero in lista:
  if (numero > media):
    maiores.append(numero)

# convertendo o array vazio para um array numpy
maiores = np.array(maiores)

#agora criando um dataframe e enviando para o csv
df = pd.DataFrame(maiores, columns=['Números'])

df.to_csv('numeros_maiores_que_media.csv', index=False)