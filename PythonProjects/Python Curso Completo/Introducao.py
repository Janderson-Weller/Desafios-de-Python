"""Crianção de programa que faça a soma de numeros inteiros, que tire a média e converta os tipos
de dados envolvidos nas operações"""
#-------------------- Operações Básicas -----------------------------
#Parte de soma de inteiros
a, b = 10, 30
print("A soma de ", a, "+", b, "é: ", a+b)

#soma de números reais
c, d = 3.5, 9.5
print("A soma de ", c, "+", d, "é: ", c + d)

#------------------ conversão de tipos --------------------------

intN = 10 #declarando o tipo inteiro para a variável intN
print(type(intN)) #monstrando o tipo int para a variável intN

intN = float(intN) #convertendo o tipo int para float
print(type(intN)) #monstrando o tipo float após a conversão

#Para não escrever código a toa, o inverso também funciona

floatX, intX = 13.0, 345
stringX, stringY = str(intX), str(floatX) #conversão de ambos tipos para string

print(type(stringX), type(stringY)) #impressão dos tipos

intbool, intbool1 = True, False
intbool, intbool1 = int(intbool), int(intbool1)
print(type(intbool), "valor1 ", intbool, "valor2", intbool1)

#----------------------- Manipulando Listas -------------------------------------

lista = [] #cria uma lista vazia
lista1 = [12, 2.4, "ola mundo", "vida"]

lista.append(2) #adiciona o item 2 a lista
lista.append(4) #adiciona o item 4 a lista
lista.append(23)
lista.append(98)
lista.append(43)

print("Lista ", lista)
lista.pop()  #tira o elemento do topo da lista

lista.remove(23) #remove o elemento de valor 23 da lista, valor precisa ser exato para a chave a ser removida
print("Após remoção ", lista)


# ------------------ operação com listas ------------------

#concantenação de listas

l = lista + lista1 #não soma os valores, apenas cria uma nova lista com os valores sequênciais de cada lista
print("Juntando as lista fica ", l)

#repetição de lista
#Assim como é feito a repetição de n (n*x vezes), a lista pode ser repetida assim

print(l * 2) #Repetindo a lista duas vezes
print(l * 3) #Repetindo a lista três vezes

#----------------- Fatiamento de Listas --------------------------

lista_fatiada = [1, 5, 6, "a", "b", "c", "d"]
print("Lista Fatiada", lista_fatiada)

print(lista_fatiada[0:4]) #imprimindo os elementos no intervalo de zero a 3 [1, 5, 6, "a"]
print(lista_fatiada[3:]) #imprimindo os elementos a partir do terceiro índice
print(lista_fatiada[:]) #imprimindo todos os elementos da lista
print(lista_fatiada[:-1]) #imprimindo os elementos da lista com excessão do último elemento
print(lista_fatiada[::-1])#invertendo a lista