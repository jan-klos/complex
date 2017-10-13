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

def add_father(node, father):
    if node.children == []:
        node.father = father
    for child in node.children:
        add_father(child, node)
        node.father = father

#################################################################

def create_tree(list):
    tree = create_node(0, list)
    add_father(tree, None)
    return tree

#################################################################

def count_nodes(node, n):
    if node.children == []:
        n[0] += 1
        n[1] += 1
        return
    for child in node.children:
        count_nodes(child, n)
    n[0] += 1

def print_nodes_number(tree):
    n = [-1, 0] # tableau parce qu'il est transmis par reference (int par affectation). -1 pour que la racine ne soit pas prise en compte
    count_nodes(tree, n)
    print("Nombre de noeuds (feuilles incluses, racine exclue): {0}. Nombre de feuilles: {1}".format(n[0], n[1]))

def print_tree(node):
    if node.children == []:
        #print(node.value, end = " ")
        return
    node.print_children()
    for child in node.children:
        print_tree(child)

