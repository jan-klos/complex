def calculate_time(A, B, C, order):
    task_num = len(order)
    machA = [0 for x in range(0, task_num)]
    machB = [0 for x in range(0, task_num)]
    machC = [0 for x in range(0, task_num)]

    machA[0] = A[order[0]]
    for i in range(1, task_num):
        try:
            machA[i] = A[order[i]] + machA[i - 1]
        except IndexError:
            pass

    if B == []:
        return machA[task_num - 1]
    else:
        machB[0] = A[order[0]] + B[order[0]]
        for i in range(1, task_num):
            if machB[i - 1] <= machA[i]:
                machB[i] = machA[i] + B[order[i]]
            else:
                machB[i] = machB[i - 1] + B[order[i]]

    if C == []:
        return machB[task_num - 1]
    else:
        machC[0] = A[order[0]] + B[order[0]] + C[order[0]]
        for i in range(1, task_num):
            if machC[i - 1] <= machB[i]:
                machC[i] = machB[i] + C[order[i]]
            else:
                machC[i] = machC[i - 1] + C[order[i]]

    return machC[task_num - 1]


################################################################

def calculate_borne_inf1(permutation, A, B, C):
    min_ba = min_bb = 99999999
    nodes_left = [item for item in list(range(0, len(B))) if item not in permutation]
    t_a = calculate_time(A, [], [], permutation)
    t_b = calculate_time(A, B, [], permutation)
    t_c = calculate_time(A, B, C, permutation)
    sum_a = sum_b = sum_c =  0
    if nodes_left == []:
        min_ba = min_bb = 0
    else:
        for i in nodes_left:
            if B[i] + C[i] < min_ba:
                min_ba = B[i] + C[i]
            if C[i] < min_bb:
                min_bb = C[i]
            sum_a += A[i]
            sum_b += B[i]
            sum_c += C[i]
    ba = t_a + sum_a + min_ba
    bb = t_b + sum_b + min_bb
    bc = t_c + sum_c
    return max(ba, bb, bc)

################################################################

def calculate_borne_inf2(permutation, A, B, C):
    nodes_left = [item for item in list(range(0, len(B))) if item not in permutation]
    t_a = calculate_time(A, [], [], permutation)
    min = sum_a = sum_c = 0
    k = -1
    if nodes_left != []:
        min = 99999999
        for i in nodes_left:
            if A[i] + B[i] + C[i] < min:
                min = A[i] + B[i] + C[i]
                k = i
        for i in nodes_left:
            if i != k and A[i] <= C[i]:
                sum_a += A[i]
            if i != k and A[i] > C[i]:
                sum_c += C[i]
    return t_a + min + sum_a + sum_c

################################################################

def calculate_borne_inf3(permutation, A, B, C):
    nodes_left = [item for item in list(range(0, len(B))) if item not in permutation]
    t_b = calculate_time(B, [], [], permutation)
    min = sum_b = sum_c = 0
    k = -1
    if nodes_left != []:
        min = 99999999
        for i in nodes_left:
            if A[i] + B[i] + C[i] < min:
                min = A[i] + B[i] + C[i]
                k = i
        for i in nodes_left:
            if i != k and B[i] <= C[i]:
                sum_b += B[i]
            if i != k and B[i] > C[i]:
                sum_c += C[i]
    return t_b + min + sum_b + sum_c

#################################################################

def ignall_schrage_algo(tree, A, B, C, b):
    if b == 'b2':
        borne = calculate_borne_inf2
    elif b == 'b3':
        borne = calculate_borne_inf3
    else:
        borne = calculate_borne_inf1
    global best_permutation
    best_permutation = []
    traverse_tree(tree, [], A, B, C, borne)
    return best_permutation

def traverse_tree(node, current_permutation, A, B, C, borne):
    global best_permutation
    if node.children == []:
        if best_permutation == []:
            best_permutation = current_permutation[:] #ceci cree une nouvelle liste et pas une copie par reference
        elif calculate_time(A, B, C, best_permutation) > calculate_time(A, B, C, current_permutation):
            best_permutation = current_permutation[:]
        current_permutation.pop(-1)
        return
    for child in node.children:
        current_permutation.append(child.value)
        if best_permutation != []:
            best_time = calculate_time(A, B, C, best_permutation)
            borne_inf = borne(current_permutation, A, B, C)
            if best_time <= borne_inf:
                current_permutation.pop(-1)
                continue
        traverse_tree(child, current_permutation, A, B, C, borne)
    if current_permutation != []:
        current_permutation.pop(-1)

#################################################################

def algo_naif(tree, A, B, C):
    global best_permutation
    best_permutation = []
    algo_naif1(tree, [], A, B, C)
    return best_permutation

def algo_naif1(node, current_permutation, A, B, C):
    global best_permutation
    if node.children == []:
        if best_permutation == []:
            best_permutation = current_permutation[:] #ceci cree une nouvelle liste et pas une copie par reference
        elif calculate_time(A, B, C, best_permutation) > calculate_time(A, B, C, current_permutation):
            best_permutation = current_permutation[:]
        current_permutation.pop(-1)
        return
    for child in node.children:
        current_permutation.append(child.value)
        algo_naif1(child, current_permutation, A, B, C)
    if current_permutation != []:
        current_permutation.pop(-1)