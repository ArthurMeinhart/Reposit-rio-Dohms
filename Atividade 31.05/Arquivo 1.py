#Objetivo do arquivo: printar qual a posição de um valor da lista

lista = [2, 6, 1, 23, 6, 8, 1]

for i in range(len(lista)):
    valor = lista[i]
    posicao = i + 1
    print(f"O {posicao}º valor da lista é {valor}")