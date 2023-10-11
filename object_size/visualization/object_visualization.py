import matplotlib.pyplot as plt
import seaborn as sns

# Object sizes
object_sizes = [10, 100, 300, 500]

# Overhead values for Ray and LF
ray_overhead = [0.0174, 0.1257, 0.3063, 0.5445]
ray_overhead = [i * 5 for i in ray_overhead]
lf_overhead = [0.0043, 0.0961, 0.2274, 0.4007]
lf_overhead = [i * 5 for i in lf_overhead]


# Set the style for the plot
sns.set_style("whitegrid")

# Plot Ray overhead values
plt.plot(object_sizes, ray_overhead, marker='D',
         label='Ray', linestyle='-', color='blue')

# Plot LF overhead values
plt.plot(object_sizes, lf_overhead, marker='o',
         label='LF', linestyle='-', color='red')

# Labeling the axes and giving a title
plt.xlabel('Object Size (MB)')
ylabel = plt.ylabel('Overhead (millisecond)')
ylabel.set_rotation(90)  # explicitly set rotation to 0 for vertical alignment
plt.title('Mean Overhead of Broadcast and Gather on 16 actors \n for Ray v2.5.1 and LF')

# Displaying the legend
plt.legend()

# Show the plot
plt.show()
