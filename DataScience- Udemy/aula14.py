# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# Crescimento da População Brasileira 1980-2016
# DataSus

dados = open("populacao_brasileira.csv").readlines()


x = []
y = []

for num, lin in enumerate(dados):
    if num != 0:
        lista = lin.split(';')
        x.append(int(lista[0]))
        y.append(int(lista[1].replace('\n', '')))

plt.bar(x, y, color='#e4e4e4')
plt.plot(x, y, color='k', linestyle='--')
plt.title('Crescimento da População Brasileira 1980-2016')
plt.ylabel('População x 10⁸')
plt.xlabel('Ano')
#plt.show()
plt.savefig('população_brasileira.png', dpi=300)
