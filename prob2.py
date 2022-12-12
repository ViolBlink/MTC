import numpy as np
import matplotlib.pyplot as plt
import json
import random

"""Считываем параметры"""
with open("param.json") as FileOfParam:
    Parametrs = json.load(FileOfParam)

# Параметры для первой задачи
Parametrs = Parametrs["Params2"]

random.seed()

fig1 = plt.figure(figsize=(8, 8),dpi=100)
ax1 = fig1.add_subplot(111)

fig2 = plt.figure(figsize=(8, 8),dpi=100)
ax2 = fig2.add_subplot(111)

N = Parametrs[0]["N"]
w = float(Parametrs[0]["w"])
a = float(Parametrs[0]["a"])
NT = Parametrs[0]["NT"]
m = float(Parametrs[0]["m"])
T = Parametrs[0]["T"]

d = 2/np.sqrt((m * (1/a + (a ** 2) * (w ** 2)/2)))


X = [0] * N
X2 = [0]
SX = [0]

for i in range(NT):
    j = random.randint(0, N - 1)
    X2.append(X2[i] - (X[j] ** 2) / N)
    SX.append(SX[i] - X[j] / N)

    x0 = (X[(j - 1) % N] + X[(j + 1) % N])/(2 + (a ** 2) * (w ** 2))
    
    X[j] = np.random.normal(x0, d)

    X2[i + 1] = X2[i] + (X[j] ** 2) / N
    SX[i + 1] = SX[i] + X[j] / N


# SumOfE = 0

# i = T
# C = 0

# while(i < NT):
#     SumOfE = SumOfE + E[i]
#     i += T//2
#     C += 1

# print(SumOfE/C)

ax1.plot(range(NT), SX[1:])
ax2.plot(range(NT), X2[1:])

# ax1.plot(range(NT), [SumOfE/C] * NT)

plt.show()