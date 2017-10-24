import random
from johnson_algo import johnson_algo
from tree import create_tree, print_tree, print_number_of_nodes, traverse_tree
from data_creating import read_from_file, create_correlation_sur_les_durees_dexecution, create_correlation_sur_les_machines, create_donnees_non_correlees
from ignall_schrage_algo import calculate_time, ignall_schrage_algo, algo_naif
from plot import plot
import time

filename = 'test.txt'

task_num, A1, B1, C1 = read_from_file(filename)



#print(johnson_algo(A4, B4))




n = 100
task_num_tab, mean_time_tab, mean_time_naif_tab = [], [], []

for j in range(2, 7):
    task_num = j
    time_tab, time_tab_naif = [], []
    tree = create_tree(list(range(0, task_num)))
    for i in range(0, n):
        A, B, C = create_donnees_non_correlees(task_num)
        start = time.time()
        best_permutation = ignall_schrage_algo(tree, A, B, C)
        end = time.time()
        time_tab.append(end - start)

        start = time.time()
        best_permutation_naif = algo_naif(tree, A, B, C)
        end = time.time()
        time_tab_naif.append(end - start)

    task_num_tab.append(task_num)
    mean_time_tab.append(sum(time_tab)/n)
    mean_time_naif_tab.append(sum(time_tab_naif)/n)

plot(task_num_tab, mean_time_tab, mean_time_naif_tab, 'Moyenne de {0} tests, donnees non-correlees'.format(n))

pass





#
# tree = create_tree(list(range(0, task_num)))
# #print_tree(tree)
# #print_number_of_nodes(tree)
# best_permutation_naif = algo_naif(tree, A1, B1, C1)
#
# best_permutation = ignall_schrage_algo(tree, A1, B1, C1)
#
#
# print(best_permutation_naif)
# print(calculate_time(A1, B1, C1, best_permutation_naif))
# print(best_permutation)
# print(calculate_time(A1, B1, C1, best_permutation))
# #traverse_tree(tree, [], A1, B1, C1)
# pass





