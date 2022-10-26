# Задача 5.
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0 40x9


file1 = 'eq2.txt'
file2 = 'eq3.txt'
file3 = 'eq_res.txt'
degree = {20: '²⁰', 19: '¹⁹', 18: '¹⁸', 17: '¹⁷', 16: '¹⁶', 15: '¹⁵', 14: '¹⁴', 13: '¹³', 12: '¹²', 11: '¹¹', 10: '¹⁰',
          9: '⁹', 8: '⁸', 7: '⁷', 6: '⁶', 5: '⁵', 4: '⁴', 3: '³', 2: '²', 1: '¹', 0: '⁰'}

dict1 = {}
dict2 = {}
r1 = open('eq2.txt', "r", encoding="utf-8")
eq1 = r1.read()
print(f'1й многочлен: {eq1}')
r2 = open('eq3.txt', "r", encoding="utf-8")
eq2 = r2.read()
print(f'2й многочлен: {eq2}')
print()


eq1 = eq1.replace("', '-", ' - ').replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(degree[20], '^20').replace(degree[19], '^19').replace(degree[18], '^18').replace(degree[17], '^17').replace(degree[16], '^16').replace(degree[15], '^15').replace(degree[14], '^14').replace(degree[13], '^13').replace(degree[12], '^12').replace(degree[11], '^11').replace(degree[10], '^10').replace(degree[9], '^9').replace(degree[8], '^8').replace(degree[7], '^7').replace(degree[6],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  '^6').replace(degree[5], '^5').replace(degree[4], '^4').replace(degree[3], '^3').replace(degree[2], '^2').replace(degree[1], '^1').replace(degree[0], '^0').replace('+ -', '- ').replace(' =', 'x^0 =')
eq2 = eq2.replace("', '-", ' - ').replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(degree[20], '^20').replace(degree[19], '^19').replace(degree[18], '^18').replace(degree[17], '^17').replace(degree[16], '^16').replace(degree[15], '^15').replace(degree[14], '^14').replace(degree[13], '^13').replace(degree[12], '^12').replace(degree[11], '^11').replace(degree[10], '^10').replace(degree[9], '^9').replace(degree[8], '^8').replace(degree[7], '^7').replace(degree[6],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  '^6').replace(degree[5], '^5').replace(degree[4], '^4').replace(degree[3], '^3').replace(degree[2], '^2').replace(degree[1], '^1').replace(degree[0], '^0').replace('+ -', '- ').replace(' =', 'x^0 =')
print(f'1: {eq1}')
print(f'1: {eq2}')

eq1 = eq1.replace(' + ', ' ').replace(' - ', ' -')
eq2 = eq2.replace(' + ', ' ').replace(' - ', ' -')
eq1 = eq1[:-3]
eq2 = eq2[:-3]
print(f'2: {eq1}')
print(f'2: {eq2}')
print()


dict1 = eq1.split()
dict2 = eq2.split()

print(f'3: {eq1}')
print(f'3: {dict1}')
print(f'3: {eq2}')
print(f'3: {dict2}')

# for item in dict1:
#     dict11 = {}


exit()
eq11 = str(dict1)
eq11 = eq11.split('x^')
print(eq11)

#         dictEquation[int(eq1[i][1])] = int(eq1[i][0])

exit()
dict1 = {}
r1 = len(eq1)
print(r1)
for i in range(r1):
    eq1[i] = eq1[i].split('x^')
    dict1[int(eq1[i][1])] = int(eq1[i][0])
print(dict1)
# eq1 = eq1.split()
# eq1 = eq1[:-2]
# eq1 = str(eq1)
print(eq1)
print(eq1)
# for i, deg in enumerate(degree):
#     eq2 = eq2.replace(f'{deg}', f'^{i}').replace(
#         f' + ', ' ').replace(f' - ', ' -')

# eq2 = eq2.split()
# eq2 = eq2[:-2]
# eq2 = str(eq2)

print(eq2)
print()

# dictEq1 = {}
# for i in range(len(eq1)):
#     eq1[i] = eq1[i].split('x^')
#     dictEq1[int(eq1[i][1])] = int(eq1[i][0])
# print(dictEq1)


# print(parseEquation(eq1))
# eq1 = eq1.replace(f' ', '')
#dict1 = eq2.split()

# def parseEquation(eq1: str):  # Разрезает готовое уравнение на словарик
#     eq1 = eq1.replace(' + ', ' ').replace(' - ', ' -')
#     eq1 = eq1.split()
#     eq1 = eq1[:-2]

#     dictEquation = {}
#     for i in range(len(eq1)):
#         eq1[i] = eq1[i].split('x^')
#         dictEquation[int(eq1[i][1])] = int(eq1[i][0])

#     return dictEquation


# for i, deg in enumerate(degree):
#     eq1 = eq1.replace(f'x{(deg)}', f'x^{[i]}').replace(
#         f' + ', ' ').replace(f' - ', ' -')
