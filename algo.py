import random
from johnson import johnson

A1 = [2, 5, 9, 5]
B2 = [3, 3, 4, 1]

n = 5 # nombre des taches

# donnees non-correlees
A2 = random.sample(range(100), n)
B2 = random.sample(range(100), n)

# correlation sur les durees d'execution
A3, B3 = [], []
for i in range (0, n):
    r = random.randint(0, 5)
    A3.append(random.randint(r*20, 20 + r*20))
    B3.append(random.randint(r*20, 20 + r*20))

# correlation sur les machines
a, b, c = 1, 2, 3
A4 = [random.randint(15*(a - 1) + 1, 15*(a - 1) + 100) for i in range(0, n)]
B4 = [random.randint(15*(b - 1) + 1, 15*(b - 1) + 100) for i in range(0, n)]

print(A4)
print(B4)

print(johnson(A4, B4))

# Montrer que l'ordonnancement obtenu est 2-approché pour notre problème.
# Préciserer la complexité de cet algo.
