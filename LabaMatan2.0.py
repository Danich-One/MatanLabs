import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

print("Введите предел суммирования по n: ")
sum_limit = int(input())
print("Введите координату начала отрезка: ")
x1 = float(input())
print("Введите координату конца отрезка: ")
x2 = float(input())

x_native = np.arange(x1, x2, 0.01)

# -----------------------------#

def f(x):
    if (x % (2 * math.pi)) < math.pi / 2:
        return np.cos(x)
    else:
        return 0

y_native = []
for i in range(x_native.size):
    y_native.append(f(x_native[i]))

def f_fur(x):
    res = 1 / (2 * np.pi) + 0.25 * np.cos(x) + np.sin(x) / (2 * np.pi)
    for n in range(2, sum_limit):
        res += (np.cos(np.pi * n / 2) * np.cos(n * x) + (np.sin(np.pi * n / 2) - n) * np.sin(n * x)) / (
                np.pi * (1 - n ** 2))
    return res

y_furie = []
for i in range(x_native.size):
    y_furie.append(f_fur(x_native[i]))

min = 0
for i in range(x_native.size):
    if y_native[i] - y_furie[i] > min:
        min = y_native[i] - y_furie[i]
print('Норма Чебышева = ', min)

min = 0
for i in range(x_native.size-10):
    v1, err1 = integrate.quad(f, x_native[i], x_native[i+10])
    v2, err2 = integrate.quad(f_fur, x_native[i], x_native[i + 10])
    if np.abs(v1-v2) > min:
        min = np.abs(v1-v2)
    print(i)
print('Интегральная норма = ', min)

plt.title('График частичной суммы S через общий тригонометрический ряд')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_native, y_furie, linewidth=1, color='r')
plt.plot(x_native, y_native, linewidth=0.5, color='b')
plt.legend(['Приближение по Фурье', 'Исходная функция'])
plt.show()

# -----------------------------#

def f_even(x):
    if (x % (2 * math.pi)) < math.pi / 2 or (x % (2 * math.pi)) > 3 * math.pi / 2:
        return np.cos(x)
    else:
        return 0

y_native = []
for i in range(x_native.size):
    y_native.append(f_even(x_native[i]))

def f_fur_cos(x):
    res = 2 / (2 * np.pi) + 0.5 * np.cos(x)
    for n in range(2, sum_limit):
        res += 2 * np.cos(np.pi * n / 2) * np.cos(n * x) / (np.pi * (1 - n ** 2))
    return res

y_furie_cos = []
for i in range(x_native.size):
    y_furie_cos.append(f_fur_cos(x_native[i]))

plt.title('График частичной суммы S по косинусам')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_native, y_furie_cos, linewidth=1, color='r')
plt.plot(x_native, y_native, linewidth=0.5, color='b')
plt.legend(['Приближение по косинусам', 'Исходная функция'])
plt.show()

# -----------------------------#

def f_odd(x):
    if (x % (2 * math.pi)) < math.pi / 2:
        return np.cos(x)
    if (x % (2 * math.pi)) > 3 * math.pi / 2:
        return -np.cos(x)
    else:
        return 0

y_native = []
for i in range(x_native.size):
    y_native.append(f_odd(x_native[i]))

def f_fur_sin(x):
    res = 2 * np.sin(x) / (2 * np.pi)
    for n in range(2, sum_limit):
        res += 2 * (np.sin(np.pi * n / 2) - n) * np.sin(n * x) / (np.pi * (1 - n ** 2))
    return res

y_furie_sin = []
for i in range(x_native.size):
    y_furie_sin.append(f_fur_sin(x_native[i]))

plt.title('График частичной суммы S по синусам')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_native, y_furie_sin, linewidth=1, color='r')
plt.plot(x_native, y_native, linewidth=0.5, color='b')
plt.legend(['Приближение по синусам', 'Исходная функция'])
plt.show()
