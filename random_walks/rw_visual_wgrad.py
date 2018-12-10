import matplotlib.pyplot as plt
from random_walks import randomwalker as rw

while True:
    rw = rw.RandomWalk()
    rw.fill_walk()

    cmap = plt.get_cmap('Blues')
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=cmap, s=10)
    plt.show()

    keep_running = input("Make another walk: ")
    if keep_running == 'n':
        break

        