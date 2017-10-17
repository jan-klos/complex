from __future__ import print_function

#################################################################

class Node:
    def __init__(self, value, children):
        self.value = value;
        self.children = children

    def print_children(self):
        for child in self.children:
            print(child.value, end = " ")
        print()

#################################################################

def create_node(value, list):
    if list == None:
        return Node(value, [])
    node = Node(value, []);
    for elem in list:
        list_copy = list[:]
        list_copy.remove(elem)
        node.children.append(create_node(elem, list_copy))
    return node

#################################################################

def create_tree(list):
    tree = create_node(0, list)
    return tree

#################################################################

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

def ignall_schrage_algo(node, current_permutation, A, B, C, borne_inf):
    if node.children == []:
        print(current_permutation)
        current_permutation.pop(-1)
        return
    print(current_permutation)
    for child in node.children:
        current_permutation.append(child.value)
        bi = calculate_borne_inf(child.value, current_permutation, A, B, C)
        if bi > visited
            current_permutation.pop(-1)
            continue
        # if bi < borne_inf[0]:
        #     current_permutation.pop(-1)
        #     continue
        borne_inf[0] = bi
        ignall_schrage_algo(child, current_permutation, A, B, C, borne_inf)
    if current_permutation != []:
        current_permutation.pop(-1)

#################################################################

def traverse_tree(node, current_permutation, A, B, C):
    if node.children == []:
        print("Une des possibilites: {list}".format(list = current_permutation))
        current_permutation.pop(-1)
        return
    print(current_permutation)
    for child in node.children:
        current_permutation.append(child.value)
        traverse_tree(child, current_permutation, A, B, C)
    if current_permutation != []:
        current_permutation.pop(-1)

#################################################################

def count_nodes(node, n):
    if node.children == []:
        n[0] += 1
        n[1] += 1
        return
    for child in node.children:
        count_nodes(child, n)
    n[0] += 1

#################################################################

def print_number_of_nodes(tree):
    n = [-1, 0] # tableau parce qu'il est transmis par reference (int par affectation). -1 pour que la racine ne soit pas prise en compte
    count_nodes(tree, n)
    print("Nombre de noeuds (feuilles incluses, racine exclue): {0}. Nombre de feuilles: {1}".format(n[0], n[1]))

#################################################################

def print_tree(node):
    if node.children == []:
        return
    node.print_children()
    for child in node.children:
        print_tree(child)
