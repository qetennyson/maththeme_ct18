import matplotlib.pyplot as plt


x_values = list(range(1,1001))
y_values = [value**2 for value in x_values]
cmap = plt.cm.get_cmap('Oranges')
print(cmap)

plt.scatter(x_values, y_values, c=y_values, edgecolor=None,s=35, cmap=cmap)

plt.title("This escalates quickly.", fontsize=12)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=12)

plt.show()

