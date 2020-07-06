#!/usr/bin/python
# coding: utf-8

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x // y


print('**********Python Calculator**********')

print("\nSelecione o número da opção desejada: \n")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

option = int(input("\nDigite sua opção (1/2/3/4): "))

if option <= 0 or option > 4:
    print("\nOpção inválida!\n")
    exit(0)

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if option == 1:
    print(num1, "+", num2, "=", addition(num1, num2))

elif option == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif option == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif option == 4:
    print(num1, "/", num2, "=", division(num1, num2))
