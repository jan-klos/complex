import random

def read_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    A = [int(x) for x in lines[1].replace('\n', '').split(' ')]
    B = [int(x) for x in lines[2].replace('\n', '').split(' ')]
    C = [int(x) for x in lines[3].replace('\n', '').split(' ')]
    return int(lines[0]), A, B, C

def create_donnees_non_correlees(task_num):
    A = random.sample(range(100), task_num)
    B = random.sample(range(100), task_num)
    C = random.sample(range(100), task_num)
    return A, B, C

def create_correlation_sur_les_durees_dexecution(task_num):
    A, B, C = [], [], []
    for i in range (0, task_num):
        r = random.randint(0, 5)
        A.append(random.randint(r*20, 20 + r*20))
        B.append(random.randint(r*20, 20 + r*20))
        C.append(random.randint(r*20, 20 + r*20))
    return A, B, C

def create_correlation_sur_les_machines(task_num):
    a, b, c = 1, 2, 3
    A = [random.randint(15*(a - 1) + 1, 15*(a - 1) + 100) for i in range(0, task_num)]
    B = [random.randint(15*(b - 1) + 1, 15*(b - 1) + 100) for i in range(0, task_num)]
    C = [random.randint(15*(c - 1) + 1, 15*(c - 1) + 100) for i in range(0, task_num)]
    return A, B, C