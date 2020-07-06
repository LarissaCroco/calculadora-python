#!/usr/bin/python
# coding: utf-8

print('**********Python Calculator**********')

print('Selecione o número da opção desejada:')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

option = int(input('Digite sua opção (1/2/3/4): '))

if option <= 0 or option > 4:
    print('Opção inválida!')
    exit(0)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if option == 1:
    result = num1 + num2
    print('{0} + {1} = {other}'.format(num1, num2, other=result))

elif option == 2:
    result = num1 - num2
    print('{0} - {1} = {other}'.format(num1, num2, other=result))

elif option == 3:
    result = num1 * num2
    print('{0} * {1} = {other}'.format(num1, num2, other=result))

elif option == 4:
    result = num1 // num2
    print('{0} / {1} = {other}'.format(num1, num2, other=result))
