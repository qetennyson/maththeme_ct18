import matplotlib.pyplot as plt
from random_walks import randomwalker as rw

rw = rw.RandomWalk(50000)
while True:
    rw.fill_walk()

    cmap = plt.get_cmap('Blues')
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=10)
    plt.show()

    keep_running = input("Make another walk: ")
    if keep_running == 'n':
        break
