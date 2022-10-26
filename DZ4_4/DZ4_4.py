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

degree = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴',
          5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹', 10: '¹⁰', 11: '¹¹', 12: '¹²', 13: '¹³', 14: '¹⁴', 15: '¹⁵', 16: '¹⁶', 17: '¹⁷', 18: '¹⁸', 19: '¹⁹', 20: '²⁰'}
equation = [0 for i in range(k)]
eq_str = ''
koef = random.sample(range(-10, 11), k + 1)
print(f'Рандомные коэффициенты: {koef}')
for i in range(len(equation)):
    if koef[i] == 0:
        equation[i] = ''
    elif koef[i] == 1:
        equation[i] = f'x^{k}'
    elif koef[i] == -1:
        equation[i] = f'-x^{k}'
    else:
        equation[i] = f'{koef[i]}x^{k}'
    k -= 1
equation.append(str(koef[-1]))
print(f'До обработки: {equation}')
eq_str2 = str(equation)
print(f'1: {eq_str2}')
eq_str2 = eq_str2.replace("', '-", ' - ').replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace('^20', degree[20]).replace('^19', degree[19]).replace('^18', degree[18]).replace('^17', degree[17]).replace('^16', degree[16]).replace('^15', degree[15]).replace('^14', degree[14]).replace('^13', degree[13]).replace('^12', degree[12]).replace('^11', degree[11]).replace('^10', degree[10]).replace('^9', degree[9]).replace('^8', degree[8]).replace('^7', degree[7]).replace(
    '^6', degree[6]).replace('^5', degree[5]).replace('^4', degree[4]).replace('^3', degree[3]).replace('^2', degree[2]).replace('^1', '').replace('^0', '').replace('+ -', '- ')

eq_str2 = eq_str2.replace(' + ', '').replace(' - ', ' -')
print(f'2: {eq_str2}')
eq_str2 = eq_str2.replace(' + ', '').replace(' - ', ' -').replace('  ', ' ')

print(f'3: {eq_str2}')
eq_str2 = eq_str2.replace(' ', '+').replace('+-', '-').replace('++',
                                                               '+').replace('+0x', 'x').replace('-0x', 'x').replace('+1x', 'x').replace('-1x', '-x')

print(eq_str2)
eq_str2 = eq_str2 + ' = 0'
print(f'4: {eq_str2}')

r = open('eq1.txt', 'w', encoding="utf-8")
r.write(eq_str2)
