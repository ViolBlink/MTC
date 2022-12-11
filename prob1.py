import numpy as np
import matplotlib.pyplot as plt
import json
import random

"""Считываем параметры"""
with open("param.json") as FileOfParam:
    Parametrs = json.load(FileOfParam)

# Параметры для первой задачи
Parametrs = Parametrs["Params1"]

random.seed()

fig1 = plt.figure(figsize=(8, 8),dpi=100)
ax1 = fig1.add_subplot(111)

N = Parametrs[0]["N"]
k = float(Parametrs[0]["k"])
T = Parametrs[0]["T"]
NT = Parametrs[0]["NT"]

Spins = [0] * (N)

for i in range(N):
    Spins[i] = int((random.randint(0, 1) - 0.5) * 2)

E = []

sum = 0
for s in range(N):
    sum = sum - Spins[s]*Spins[(s + 1) % N]

E.append(sum)

for i in range(NT):
    j = random.randint(0, N - 1)
    pe = np.exp(k*(Spins[(j - 1) % N] + Spins[(j + 1) % N]))
    p = pe/(1/pe + pe)
    r = random.random()

    E.append(E[i] + Spins[(j - 1) % N] * Spins[j] + Spins[j] * Spins[(j + 1) % N])


    if(r < p):
        Spins[j] = 1
    else:
        Spins[j] = -1
    
    E[i + 1] = E[i + 1] - Spins[(j - 1) % N] * Spins[j] - Spins[j] * Spins[(j + 1) % N]


SumOfE = 0

i = T
C = 0

while(i < NT):
    SumOfE = SumOfE + E[i]
    i += T//2
    C += 1

print(SumOfE/C)

ax1.plot(range(NT), E[1:])

ax1.plot(range(NT), [SumOfE/C] * NT)

plt.show()