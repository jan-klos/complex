def mark_in_list(A, B, index):
    A[index] = 99999
    B[index] = 99999


def johnson_algo(A, B):
    G, D = [], []
    while len(set(A)) != 1:
        a_index = A.index(min(A))
        b_index = B.index(min(B))
        if A[a_index] < B[b_index]:
            G.append(a_index + 1)
            mark_in_list(A, B, a_index)
        else:
            D.append(b_index + 1)
            mark_in_list(A, B, b_index)
    return G + D