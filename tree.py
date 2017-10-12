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

def count_nodes(tree):
    if node.children = []


def print_tree(node):
    if node.children == []:
        print(node.value, end = " ")
        return
    node.print_children()
    for child in node.children:
        print_tree(child)


    Check if the current node is empty / null.
    Traverse the left subtree by recursively calling the in-order function.
    Display the data part of the root (or current node).
    Traverse the right subtree by recursively calling the in-order function.
