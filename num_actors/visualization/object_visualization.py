import matplotlib.pyplot as plt
import seaborn as sns

# Number of Actors
actors = [2, 4, 8, 16]

# Overhead values for Ray and LF
lf_overhead = [0.0029, 0.0030, 0.0034, 0.0043]
lf_overhead = [i * 1000 for i in lf_overhead]

ray_overhead = [0.0085, 0.0101, 0.0121, 0.0174]
ray_overhead = [i * 1000 for i in ray_overhead]


# Set the style for the plot
sns.set_style("whitegrid")

# Plot Ray overhead values
plt.plot(actors, ray_overhead, marker='D',
         label='Ray', linestyle='-', color='blue')

# Plot LF overhead values
plt.plot(actors, lf_overhead, marker='o',
         label='LF', linestyle='-', color='red')

# Labeling the axes and giving a title
plt.xlabel('Number of Actors')
ylabel = plt.ylabel('Overhead (millisecond)')
ylabel.set_rotation(90)  # explicitly set rotation to 0 for vertical alignment
plt.title('Mean Overhead of Broadcast and Gather 10MB Object \n with Different Number of Actors')

# Displaying the legend
plt.legend()

# Show the plot
plt.show()
