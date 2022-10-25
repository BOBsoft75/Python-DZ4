# Задача 4.
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random

k = int(input('Введите натуральную степень k: '))
while k <= 0:
    k = int(input('Введены не корректные данные! Введите натуральную степень k: '))

degree = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

equation = [0 for i in range(k)]
eq_str = ''
koef = random.sample(range(-100, 101), k + 1)
print(f'Рандомные коэффициенты: {koef}')
for i in range(len(equation)):
    equation[i] = f'{koef[i]}x^{k}'
    k -= 1
equation.append(str(koef[-1]))
# print(f'До обработки: {equation}')
eq_str2 = str(equation)
eq_str2 = eq_str2.replace('[', '').replace(
    ']', '').replace("'", '').replace(',', '').replace(' ', ' + ').replace('^9', degree[9]).replace('^8', degree[8]).replace('^7', degree[7]).replace('^6', degree[6]).replace('^5', degree[5]).replace('^4', degree[4]).replace('^3', degree[3]).replace('^2', degree[2]).replace('^1', '').replace('^0', '').replace('+ -', '- ')
eq_str2 = eq_str2 + ' = 0'
print(eq_str2)
r = open('eq1.txt', 'w', encoding="utf-8")
r.write(eq_str2)
