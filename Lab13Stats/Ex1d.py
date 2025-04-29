import matplotlib.pyplot as plt

# First set of x and y values
x_values1 = [1, 2, 3, 4, 5]
y_values1 = [2, 4, 1, 8, 7]

# Second set of x and y values
x_values2 = [1, 2, 3, 4, 5]
y_values2 = [1, 3, 5, 7, 9]

# First figure: Line Plot
plt.figure("Line Plot")
plt.plot(x_values1, y_values1, marker='o', linestyle='-', color='blue', label='Dataset 1')
plt.plot(x_values2, y_values2, marker='s', linestyle='--', color='green', label='Dataset 2')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Line Plot with Two Datasets')
plt.grid(True)
plt.legend()

# Second figure: Scatter Plot
plt.figure("Scatter Plot")
plt.scatter(x_values1, y_values1, color='red', marker='o', label='Dataset 1')
plt.scatter(x_values2, y_values2, color='purple', marker='x', label='Dataset 2')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot with Two Datasets')
plt.grid(True)
plt.legend()

# Show both plots
plt.show()
