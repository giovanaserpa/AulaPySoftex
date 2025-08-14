""" 
Aula Online 1 - Python Básico
TIPOS DE DADOS
- string (texto)
- int (número inteiro)
- float (número decimal)
- boolean (verdadeiro ou falso)
"""
#casa = "ola"
#print(type(casa))
#print(type(10))
#print(type(10.5))
#print(type(True))

#print(5+5)
#print(5-2)
#print(5*2)
#print(5/5)
#print(5//2)
#print(5%2)
#print(5**2) 
####
print(2+"2")  # Isso vai gerar um erro porque não é possível somar um inteiro com uma string
print("2" + "2")  # Isso vai funcionar porque ambas são strings, concatena os valores
print("2" * 3)  # Isso vai funcionar, repetindo a string "2" três vezes
print(2 * 3)  # Isso vai funcionar, multiplicando os números inteiros
print(2 + 3.5)  # Isso vai funcionar, somando um inteiro com um float
print("2" + str(3))  # Isso vai funcionar, convertendo o inteiro 3 para string antes da concatenação
print("2" + "3")  # Isso vai funcionar, concatenando duas strings
print(2 + 3)  # Isso vai funcionar, somando dois inteiros
print(2 * 3.5)  # Isso vai funcionar, multiplicando um inteiro por um float
print(2 + 3.5)  # Isso vai funcionar, somando um inteiro com um float
####
""=="" #é usado para atribuir um valor a uma variável 
"!=" #diferente
"< e >" #menor e maior
"<= e >=" #menor ou igual e maior ou igual (responde com booleano, ou seja, True ou False)

nome_usuario = input("Digite seu nome: ")  # Isso vai solicitar ao usuário que digite seu nome
print(f"O nome do usuário é: {nome_usuario}")  # Isso vai imprimir o nome do usuário digitado
idade_usuario = int(input("Digite sua idade: "))  # Isso vai solicitar ao usuário que digite sua idade e converter a entrada para um inteiro
print(f"A idade do usuário é: {idade_usuario}")  # Isso vai imprimir a idade

