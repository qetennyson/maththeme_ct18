import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.title("Square Numbers", fontsize=12)

plt.xlabel("value", fontsize=10)

plt.ylabel("square of value", fontsize=10)

plt.scatter(x_values, y_values, s=35)
# s controls size of dots

plt.show()