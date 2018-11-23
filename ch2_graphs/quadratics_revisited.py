'''
Quadratic function calculator
'''

import matplotlib.pyplot as plt

# Assume value of x
def quadratic():
    x_values = [i for i in range(1, 10000, 4)]
    y_values = []
    for x in x_values:
        # Calc the value of the function
        y = x**2 + 2*x + 1
        y_values.append(y)
        print(f'x={x} y={y}')
    draw_graph(x_values, y_values)


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-value')
    plt.ylabel('y-value')
    plt.title('Plotting Quadratic functions')
    plt.show()

quadratic()

