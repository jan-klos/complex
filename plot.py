import matplotlib
import matplotlib.pyplot as plt

def plot(y, x, z, title):
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(y, x)
    ax.plot(y, z)
    ax.set_title(title)
    plt.xlabel('Nombre des taches', fontsize=18)
    plt.ylabel('Temps', fontsize=16)
    plt.show()