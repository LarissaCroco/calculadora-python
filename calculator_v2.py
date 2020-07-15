#!/usr/bin/python
# coding: utf-8

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("\nOops! Não é possível dividir por 0.")
        exit(0)


print('**********Python Calculator**********')

print("\nSelecione o número da opção desejada: \n")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

while True:
    try:
        option = int(input("\nDigite sua opção (1/2/3/4): "))
        break

    except ValueError:
        print("\nOops! Não é uma opção válida.  Tente novamente")


if option <= 0 or option > 4:
    print("\nOpção inválida!\n")
    exit(0)

while True:
    try:
        num1 = float(input("\nDigite o primeiro número: "))
        break

    except ValueError:
        print("\nOops! Não é um número inteiro.  Tente novamente")

while True:
    try:
        num2 = float(input("\nDigite o segundo número: "))
        break

    except ValueError:
        print("\nOops! Não é um número inteiro.  Tente novamente")

if option == 1:
    print(num1, "+", num2, "=", addition(num1, num2))

elif option == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif option == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif option == 4:
    print(num1, "/", num2, "=", division(num1, num2))
