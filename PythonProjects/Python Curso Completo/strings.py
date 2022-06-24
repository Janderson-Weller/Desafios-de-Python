#declarando uma string
nome1 = "João"
nome2 = 'Da Vida'
print("Nome1 = %s  e  Nome2 = %s" % (nome1, nome2))

#concatenando strings
Nome = "João"
Sobrenome = "Silva"
nomeSobrenome = Nome + Sobrenome
print(nomeSobrenome)

#slicing (fatiamento) de string
string1 = "vida de gado novo"
print("1: ", string1[1:4]) #mostrando os caracteres no intervalo de 1 ao 4 (caracteres 1,2,3)
print("2: ", string1[0:-1:2]) #mostrando os elementos do caracter 0 ao final da string, porém, pulando de 2 em 2
print("3: ", string1[4:10]) #mostrando os caracteres no intervalo 4 ao 10 (caracteres 4,5,6,7,8,9)

#função split - criando uma lista atravé de uma string
print(string1.split()) #por padrão, cria uma lista com todas as palavras, excluindo espaço