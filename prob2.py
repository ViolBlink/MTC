import numpy as np
import matplotlib.pyplot as plt
import json
import random

"""Считываем параметры"""
with open("param.json") as FileOfParam:
    Parametrs = json.load(FileOfParam)

# Считывание параметров
Parametrs = Parametrs["Params2"]

random.seed()

# Шаблоны картинок
fig1 = plt.figure(figsize=(8, 8),dpi=100)
ax1 = fig1.add_subplot(111)

fig2 = plt.figure(figsize=(8, 8),dpi=100)
ax2 = fig2.add_subplot(111)

# Параметры
N = Parametrs[0]["N"]
w = float(Parametrs[0]["w"])
a = float(Parametrs[0]["a"])
NT = Parametrs[0]["NT"]
m = float(Parametrs[0]["m"])
T = Parametrs[0]["T"]

# Дисперсия
d = 2/np.sqrt((m * (1/a + (a ** 2) * (w ** 2)/2)))

# Конфигурация x, заполненая 0
X = [0] * N
# Массив для x^2 и просто x
X2 = [0]
SX = [0]


for i in range(NT):
    # Берется случайный x[j]
    j = random.randint(0, N - 1)
    # Из массива вычитается старое значение, чтобы потом заменить новым
    X2.append(X2[i] - (X[j] ** 2) / N)
    SX.append(SX[i] - X[j] / N)

    # Высчитывается среднее
    x0 = (X[(j - 1) % N] + X[(j + 1) % N])/(2 + (a ** 2) * (w ** 2))
    
    # Новый x[j] по Гауссу
    X[j] = np.random.normal(x0, d)

    # Добовляется новый x^2 и x
    X2[i + 1] = X2[i] + (X[j] ** 2) / N
    SX[i + 1] = SX[i] + X[j] / N


ax1.plot(range(NT), SX[1:])
ax2.plot(range(NT), X2[1:])


plt.show()