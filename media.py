'''
Estas funções já existem se você utilizar o 'from statistics import *',
no entanto, meu objetivo aqui é desenvolver minhas próprias funções
que fazem isto apenas para aprendizagem e entender como funcionam.

mean(lista) - retorna a média
median(lista) - retorna a mediana
mode(lista) - retorna a moda
''' 

def mediaDaLista(lista):
    media = (sum(lista)/float(len(lista)))
    return media

def medianaDaLista(lista):
    lista_ordenada = sorted(lista)
    tamanhoLista = len(lista_ordenada)

    if tamanhoLista % 2 == 0:
        mediana = (lista_ordenada[int(tamanhoLista/2)] + lista_ordenada[int(tamanhoLista/2)-1])/2
    elif tamanhoLista % 2 == 1:
        mediana = lista_ordenada[int(tamanhoLista/2)]
    return mediana

def modaDaLista(lista):
    lista_dicionario = {}
    
    for l in lista:
        if l not in lista_dicionario:
            lista_dicionario[l] = 1
        else:
            lista_dicionario[l] += 1
    
    maior_repeticao = max(lista_dicionario.values())
    
    for i in lista_dicionario:
        if lista_dicionario[i] == maior_repeticao:
            moda = i
    
    return moda