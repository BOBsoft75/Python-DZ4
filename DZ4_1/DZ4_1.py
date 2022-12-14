# Задача 1.
# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# !!ВНИМАНИЕ
# !!! не использовать константу math.pi

from decimal import Decimal, getcontext

n = int(input('Укажите точность в формате кол-ва знаков после запятой: '))
getcontext().prec = 100
pi_calc = Decimal(0)
k = 0
while k < n:
    pi_calc += (Decimal(1)/(16**k)) * ((Decimal(4)/(8*k+1)) - (Decimal(2)/(8*k+4)) -
                                       (Decimal(1)/(8*k+5)) - (Decimal(1)/(8*k+6)))
    k += 1
print(f'Референс  Пи: 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
print(f'Расчетное Пи: {(str(pi_calc))[0:n+2]}')
# print(f'Расчетное Пи: {(str(pi_calc))}')


# --------------------------------------------------------
# Другой вариант пробовал
# --------------------------------------------------------

# d = int(input('Введите точность (кол-во знаков после запятой): '))
# pi_calc = 0
# check = 0
# for n in range(int(10000)):
#     pi_calc += (1 / 16**n) * (4/(8*n + 1) - 2 /
#                               (8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))
#     if abs(check - pi_calc) < 10**(-d):
#         break
#     check = pi_calc
# print('Пи = ', round(pi_calc, d))
