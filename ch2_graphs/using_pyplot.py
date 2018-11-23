import matplotlib.pyplot as plt
from pylab import savefig

def create_graph():
    x_numbers = [1,2,3]
    y_numbers = [2,4,6]

    plt.plot(x_numbers, y_numbers)
    plt.show()

#TODO: Saving graphs? savefig not working.

if __name__ == '__main__':
    create_graph()
