'''
Meu objetivo aqui é modularizar o código integrando arquivos
com diferentes propósitos. Assim, eu consigo ter um maior nível
de abstração e legibilidade mais fácil.
'''

import aleatorio as a
import media as m

lista = a.geraListaInteiro(10)
media = m.mediaDaLista(lista)
mediana = m.medianaDaLista(lista)
moda = m.moda(lista)

print("A minha lista é ")
print(lista)

print('A média da minha lista é ' + str(media))
print('A mediana da minha lista é ' + str(mediana))
print('A mediana da minha lista é ' + str(moda))