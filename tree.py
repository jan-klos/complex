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
    tree = create_node(-1, list)
    return tree

#

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
