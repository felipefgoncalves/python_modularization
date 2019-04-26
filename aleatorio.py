'''
Função simples para gerar um array randômico baseado
num dado comprimento da lista
'''

import random

def geraListaInteiro(tam):
    lista = []
    for i in range(tam):
        lista.append(random.randint(0, tam))
    return lista