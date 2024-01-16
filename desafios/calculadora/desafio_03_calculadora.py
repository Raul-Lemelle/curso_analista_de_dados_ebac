# calculadora.py

import math

def add(x, y):
    """Soma dois números."""
    return x + y

def subtract(x, y):
    """Subtrai dois números."""
    return x - y

def multiply(x, y):
    """Multiplica dois números."""
    return x * y

def divide(x, y):
    """Divide dois números. Retorna None se a divisão por zero."""
    if y != 0:
        return x / y
    else:
        print("Erro: divisão por zero.")
        return None

def power(x, y):
    """Calcula x elevado à potência de y."""
    return x ** y

def square_root(x):
    """Calcula a raiz quadrada de x. Retorna None se x for negativo."""
    if x >= 0:
        return math.sqrt(x)
    else:
        print("Erro: não é possível calcular a raiz quadrada de um número negativo.")
        return None

def logarithm(x, base=10):
    """Calcula o logaritmo de x na base especificada. Retorna None se x for negativo."""
    if x > 0:
        return math.log(x, base)
    else:
        print("Erro: não é possível calcular o logaritmo de um número não positivo.")
        return None
