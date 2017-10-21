def calculate_time(A, B, C, order):
    task_num = len(order)
    if task_num < len(A):
        return 99999
    machA = [0 for x in range(0, task_num)]
    machB = [0 for x in range(0, task_num)]
    machC = [0 for x in range(0, task_num)]

    machA[0] = A[order[0]]
    for i in range(1, task_num):
        machA[i] = A[order[0]] + machA[i - 1]

    machB[0] = A[order[0]] + B[order[0]]
    for i in range(1, task_num):
        if machB[i - 1] <= machA[i]:
            machB[i] = machA[i] + B[order[0]]
        else:
            machB[i] = machB[i - 1] + B[order[0]]

    machC[0] = A[order[0]] + B[order[0]] + C[order[0]]
    for i in range(1, task_num):
        if machC[i - 1] <= machB[i]:
            machC[i] = machB[i] + C[order[0]]
        else:
            machC[i] = machC[i - 1] + C[order[0]]

    return machC[task_num - 1]


################################################################

def calculate_borne_inf(index, current_permutation, A, B, C):
    min_ba = min_bb = 99999
    nodes_left = [item for item in list(range(0, len(B))) if item not in current_permutation]
    t_a = t_b = t_c = 0
    for i in current_permutation:
        t_a += A[i]
        t_b += B[i]
        t_c += C[i]
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
    bb = t_a + t_b + sum_b + min_bb
    bc = t_a + t_b + t_c + sum_c
    return max(ba, bb, bc)

#################################################################

def ignall_schrage_algo(tree, A, B, C):
    last_permutation = []
    global last_permutation
    ignall_schrage_algo1(tree, [], A, B, C, [0])
    return last_permutation

def ignall_schrage_algo1(node, current_permutation, A, B, C, borne_inf):
    global last_permutation
    if node.children == []:
        last_permutation = current_permutation[:]
        current_permutation.pop(-1)
        return
    #print(current_permutation)
    for child in node.children:
        current_permutation.append(child.value)
        if last_permutation != [] and calculate_time(A, B, C, last_permutation) < borne_inf[0]:
             current_permutation.pop(-1)
             continue
        borne_inf[0] = calculate_borne_inf(child.value, current_permutation, A, B, C)
        ignall_schrage_algo1(child, current_permutation, A, B, C, borne_inf)
    if current_permutation != []:
        current_permutation.pop(-1)