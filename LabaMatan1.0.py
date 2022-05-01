#Не использовать в личных целях! Только для провекри:)

import numpy as np
from matplotlib import pyplot as plt

def f(x): #подынтегральная функция
    return x**2
x_st = 1.0 #концы отрезка интегрирования
x_ed = 2.0 #концы отрезка интегрирования
delta = x_ed - x_st #длина отрезка интегрирования
s = 0 #значение интегральной суммы

print('Введите количество разбиений{exit - Передумал}: ')

def vv():
    q = input()
    if q == 'exit':
        exit(0)
    elif round(float(q)) < 1:
        print('Введите натуральное число...')
        vv()
    else:
        return round(float(q))

n = vv() #количество точек разбиения

z = np.linspace(x_st, x_ed, n)  # счёт точек для графика функции exp(x)
w = [f(i) for i in z]

print('Введите способ выбора значений функции на отрезке: ')
print('1 - Начальная точка отрезка')
print('2 - Средняя точка отрезка')
print('3 - Конечная точка отрезка')
print('{exit - Передумал}')

def vvod():
    q = input()
    if q == 'exit':
        exit(0)
    elif int(q) < 1 or int(q) > 4:
        print('Выберите значение из списка...')
        vvod()
    else:
        return int(q)

a = vvod() #вариант выбора точек разбиения

if a == 1:
    x = [x_st+0.5*delta/n]
    y = [f(x_st)]
    for i in range(n):
        s += delta/n*f(x_st+i*delta/n)
        x.append(x_st+0.5*delta/n+i*delta/n)
        y.append(f(x_st+i*delta/n))

if a == 2:
    x = [x_st+delta/n]
    y = [f(x_st)]
    for i in range(n):
        s += delta/n*f(x_st+(i+0.5)*delta/n)
        x.append((i-1)/n+x_st+(1+0.5*delta)*delta/n)
        y.append(f(x[i + 1]))

if a == 3:
    x = [x_st+0.5*delta/n]
    y = [f(x_st+delta/n)]
    for i in range(n):
        s += delta/n*f(x_st+(i+1)*delta/n)
        x.append(x_st+0.5*delta/n+i*delta/n)
        y.append(f(x_st+(i+1)*delta/n))

deltas13 = 2/n
deltas2 = 1/(12*n**2)
delta13theor = 0
delta2theor = 0
for i in range(1,n+1):
    delta13theor+= (i/n+1)*(delta/n)**2
for i in range(1,n+1):
    delta2theor+= 1/(12*n**3)
reference = 7/3
print('Значение интегральной суммы: ', s, '\n')
print('Эталонное значение по формуле Н-Л = ', reference, '\n')
print('Δ = ', abs(reference-s))
if a == 2:
    print('Δs =', delta2theor)
else:
    print('Δs =', delta13theor)
plt.grid()
plt.plot(z, w, 'k')  # вывод графика функции
plt.bar(x, y, width=delta/n, color='r')  # вывод графа интегральной суммы1
plt.title("Интегральная сумма: ")
plt.ylabel('Ось Y')
plt.xlabel('Ось X')
plt.show()