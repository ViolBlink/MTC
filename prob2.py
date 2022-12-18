import numpy as np
import matplotlib.pyplot as plt
import json
import random
import math

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
d = 1/np.sqrt(2*(m * (1/a + (a) * (w ** 2)/2)))

# Конфигурация x, заполненая 0
X = np.zeros(N)
# Массив для x^2 и просто x
X2 = np.zeros(NT)
SX = np.zeros(NT)


for i in range(NT):
    # Берется случайный x[j]
    for j in range(N):
        # Из массива вычитается старое значение, чтобы потом заменить новым

        # Высчитывается среднее
        r = np.random.random(1)
        phi= np.random.random(1)
        x0 = (X[(j - 1) % N] + X[(j + 1) % N]) / (2 + (a * w) ** 2)
        z0=math.cos(2*math.pi*phi)*(-2*math.log(r))**(0.5)
        
        # Новый x[j] по Гауссу
        X[j] = x0 + d*z0

        # Добавляется новый x^2 и x
        X2[i] = X2[i] + (m / 2) * (w ** 2) * ((X[j]) ** 2) / N
        SX[i] = SX[i] + X[j] / N


SumOfE = 0

i = T
C = 0

while(i < NT):
    SumOfE = SumOfE + X2[i]
    i += T//2
    C += 1

SumOfE /= C

ax1.plot(range(NT), SX, label = '<x>')
ax1.legend()
ax1.grid(True)
ax2.plot(range(NT), X2, label = '<E>')
ax2.plot(range(NT), [SumOfE] * NT, label = 'Average of E for swips')
ax2.legend()
ax2.grid(True)

print(SumOfE)

plt.show()