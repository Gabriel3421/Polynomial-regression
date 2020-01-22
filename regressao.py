
'''
Aluno: Gabriel de Souza Nogueira da Silva
'''

import matplotlib.pyplot as plp
import re
import numpy as np

grau_poli = int(input('Digite o grau do polinômio: '))

def normaliza(k):
    #normaliza os dados recebidos
    media_k = float(sum(k))/len(k)
    for valor in k:
        norma = (valor - media_k)/(valor - media_k)*(valor - media_k)
        y1.append(norma)
    return y1

def cria_X(x, grau):
    #cria a matriz de valores x
    Kx = np.ones((len(x),grau_poli+1))
    for n in range(0,len(x)):
        for m in range(1,grau_poli+1):
            Kx[n][m] = x[n]**m     
    return Kx        

def cria_Y(y):
    #cria a matriz de valores y
    Ky = np.ones((len(y), 1))
    for m in range(0, len(y)):
        Ky[m][0]= y[m]
    return Ky

def somatorioQe(vet_y, vet_y_linha):
    #cria o somatorio de Qe
    somador = 0
    for k in range(0,len(y)):
        somador = somador + (vet_y[k] - vet_y_linha[k])**2
    return somador

def somatorioYy(y):
    #cria o somatorio de yy
    somador = 0
    y_media = np.sum(y)/len(y)
    for k in range(0,len(y)):
        somador = somador + (y[k] - y_media)**2
    return somador   

x = []
y = []
y1 = []

dados = open("aerogerador.dat", "r")
for line in dados:
    #separando o que é x do que é y 
    line = line.strip()#quebra no \n
    line = re.sub('\s+',',',line)#trocando os espaços vazios por virgula   
    X,Y = line.split(",")#quebra nas virgulas e retorna 2 valores
    x.append(float(X))
    y.append(float(Y))
dados.close()

y1 = normaliza(y)

kx = cria_X(x, grau_poli)
ky = cria_Y(y1)

#criando o beta usando as funçoes de matrizes da biblioteca numpy
B = (np.linalg.inv(np.transpose(kx)@kx))@np.transpose(kx)@ky

y_linha = kx@B

e = ky - y_linha

r2 = 1 - (somatorioQe(y1, y_linha)/somatorioYy(y1))

r2aj = 1 -((somatorioQe(y1, y_linha)/(len(x) - (grau_poli+1)))/(somatorioYy(y1)/(len(x) - 1)))

print("Valor de R2: "+ str(r2))

print("Valor de R2 ajustado: "+ str(r2aj))

plp.plot(x,y_linha, color ='black')
plp.scatter(x,y1, marker=".")
plp.show()

