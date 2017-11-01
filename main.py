import random
from johnson_algo import johnson_algo
from tree import create_tree, print_tree, print_number_of_nodes, traverse_tree
from data_creating import read_from_file, create_correlation_sur_les_durees_dexecution, create_correlation_sur_les_machines, create_donnees_non_correlees
from ignall_schrage_algo import calculate_time, ignall_schrage_algo, algo_naif
from plot import plot_one_curve, plot_two_curves
import time

filename = 'test.txt'

task_num, A1, B1, C1 = read_from_file(filename)

n = 100
max_task_num = 10

#print(johnson_algo(A4, B4))


time_tab, time_tab_naif = [], []
def mesure_time_naif(create_function):
    task_num_tab, mean_time_tab, mean_time_naif_tab = [], [], []

    for j in range(2, max_task_num + 1):
        task_num = j
        time_tab, time_tab_naif = [], []
        tree = create_tree(list(range(0, task_num)))
        for i in range(0, n):
            A, B, C = create_function(task_num)
            start = time.time()
            algo_naif(tree, A, B, C)
            end = time.time()
            time_tab_naif.append(end - start)
        mean_time_naif_tab.append(sum(time_tab_naif)/n)
    file = open('mean_time_naif.txt', 'w')
    file.write(' '.join(str(x) for x in mean_time_naif_tab))
    file.close()



def mesure_time(create_function, data_type):
    task_num_tab, mean_time_tab, mean_time_naif_tab = [], [], []

    for j in range(2, max_task_num + 1):
        task_num = j
        tree = create_tree(list(range(0, task_num)))
        for i in range(0, n):
            A, B, C = create_function(task_num)
            start = time.time()
            ignall_schrage_algo(tree, A, B, C)
            end = time.time()
            time_tab.append(end - start)

        task_num_tab.append(task_num)
        mean_time_tab.append(sum(time_tab)/n)

    plot_one_curve(list(set(task_num_tab)), mean_time_tab, 'Moyenne de {0} tests, {1}'.format(n, data_type))
    #plot_two_curves(task_num_tab, mean_time_tab, mean_time_naif_tab, 'Moyenne de {0} tests, {1}'.format(n, data_type))

#mesure_time_naif(create_donnees_non_correlees)
#mesure_time(create_donnees_non_correlees, 'données non-correlées')
#mesure_time(create_correlation_sur_les_durees_dexecution, 'données correlées sur les durées d\'exécution')
#mesure_time(create_correlation_sur_les_machines, 'données correlées sur les machines')

pass

tree = create_tree(list(range(0, task_num)))

#best_permutation_naif = algo_naif(tree, A1, B1, C1)
#
best_permutation = ignall_schrage_algo(tree, A1, B1, C1, 'b3')
#
#
# print(best_permutation_naif)
# print(calculate_time(A1, B1, C1, best_permutation_naif))
print(best_permutation)
print(calculate_time(A1, B1, C1, best_permutation))






