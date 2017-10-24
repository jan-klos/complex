import matplotlib
import matplotlib.pyplot as plt

def test(x, y):
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o')
    #ax.set_title('Using hyphen instead of Unicode minus')
    plt.xlabel('Nombre des taches', fontsize=18)
    plt.ylabel('Temps', fontsize=16)
    plt.show()