import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.figure()
plt.boxplot(y)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()

plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.figure()
plt.hist(y, bins=5)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()