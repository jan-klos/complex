import random
from johnson_algo import johnson_algo
from tree import create_tree, print_tree, print_number_of_nodes, traverse_tree
from util import read_from_file
from ignall_schrage_algo import calculate_time, ignall_schrage_algo

filename = 'test.txt'

task_num, A1, B1, C1 = read_from_file(filename)

# donnees non-correlees
A2 = random.sample(range(100), task_num)
B2 = random.sample(range(100), task_num)
C2 = random.sample(range(100), task_num)

# correlation sur les durees d'execution
A3, B3, C3 = [], [], []
for i in range (0, task_num):
    r = random.randint(0, 5)
    A3.append(random.randint(r*20, 20 + r*20))
    B3.append(random.randint(r*20, 20 + r*20))
    C3.append(random.randint(r*20, 20 + r*20))

# correlation sur les machines
a, b, c = 1, 2, 3
A4 = [random.randint(15*(a - 1) + 1, 15*(a - 1) + 100) for i in range(0, task_num)]
B4 = [random.randint(15*(b - 1) + 1, 15*(b - 1) + 100) for i in range(0, task_num)]
C4 = [random.randint(15*(c - 1) + 1, 15*(c - 1) + 100) for i in range(0, task_num)]

#print(johnson_algo(A4, B4))

# Montrer que l'ordonnancement obtenu est 2-approche pour notre probleme.
# Preciserer la complexite de cet algo.


tree = create_tree(list(range(0, task_num)))
#print_tree(tree)
#print_number_of_nodes(tree)
global last_permutation

last_permutation = ignall_schrage_algo(tree, A1, B1, C1)

print(last_permutation)
print(calculate_time(A1, B1, C1, last_permutation))
#traverse_tree(tree, [], A1, B1, C1)
pass











