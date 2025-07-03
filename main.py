import matplotlib.pyplot as plt
import random

# Generate random data
num_points = 10  # Number of data points
x = sorted([random.randint(1, 100) for _ in range(num_points)])  # Random x-values (sorted for better visualization)
y = [random.randint(1, 100) for _ in range(num_points)]  # Random y-values

# Create a line graph
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Random Data')

# Add labels and title
plt.xlabel('Random X Values')
plt.ylabel('Random Y Values')
plt.title('Line Graph with Random Numbers')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()