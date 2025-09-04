'''
# AulaOnline1808.py
# Condicionais
# if elif else
# if == se 
# else == então
# elif == senão (mas se comporta como IF e pode ser usado varias vezes)
# for = para (variavel temporária que só trabalha dentro do for)
# while = enquanto (enquanto a condição for verdadeira, o código dentro do while será executado)


Menor de idade > paga meia
Maior de idade > paga inteira
Idoso tem gratuidade

'''
###Sistema de ingresso de cinema

idade_cliente = int(input('Digite a idade do cliente: '))
dia_quarta = input('É quarta-feira? (s/n): ').strip().lower()

if idade_cliente >= 60:
    print('O cliente tem gratuidade.')
elif dia_quarta == 's':
    print('Cortesia de 50% para todos os clientes.')

if idade_cliente < 18:
    print('O cliente paga meia entrada.')
elif idade_cliente >= 60:
    print('O cliente tem gratuidade.')
else:
    print('O cliente paga inteira.')
