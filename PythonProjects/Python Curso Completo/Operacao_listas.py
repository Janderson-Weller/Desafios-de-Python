#Inserir elementos em uma lista vazia

lista = [] #criação da lista

i = 0

while i < 10:
    lista.append(i*2)
    i = i+1
print("criando lista com o loop while", lista)
#lista1 = [j for j in range(0, 10)]

print("criando lista com comprehension list", [j for j in range(1,10)])

#remoção de elementos pelo fatiamento
lista[1:4] = [] #remove os elementos do índice 1 ao 3
print(lista)
