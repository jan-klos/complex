import matplotlib
import matplotlib.pyplot as plt

def plot_one_curve(y, x, title):
    #plt.ion()
    #plt.figure()
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(y, x)
    ax.set_title(title)
    plt.xlabel('Nombre des tâches', fontsize=18)
    plt.ylabel('Temps [s]', fontsize=16)
    plt.show()

def plot_two_curves(y, x, z, title):
    #plt.ion()
    #plt.figure()
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(y, x)
    ax.plot(y, z)
    ax.set_title(title)
    plt.xlabel('Nombre des tâches', fontsize=18)
    plt.ylabel('Temps [s]', fontsize=16)
    plt.show()