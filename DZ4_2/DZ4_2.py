# Задача 2.
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число N: '))

def get_simple(n):
    simple = []
    i = 2
    while 1 < n:
        if n % i == 0:
            simple.append(i)
            n = n // i
        else:
            i += 1
    return simple

print(get_simple(n))
