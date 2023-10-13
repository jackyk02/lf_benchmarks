import re
import numpy as np
import scipy.stats as stats

data = """
2023-10-13 03:40:23, CPU: 1.2%, Memory: 3.88%
2023-10-13 03:40:24, CPU: 0.2%, Memory: 3.88%
2023-10-13 03:40:26, CPU: 3.6%, Memory: 3.88%
2023-10-13 03:40:27, CPU: 0.4%, Memory: 3.88%
2023-10-13 03:40:28, CPU: 27.1%, Memory: 3.95%
2023-10-13 03:40:29, CPU: 0.4%, Memory: 3.87%
2023-10-13 03:40:30, CPU: 39.8%, Memory: 6.97%
2023-10-13 03:40:31, CPU: 0.2%, Memory: 3.87%
2023-10-13 03:40:33, CPU: 26.6%, Memory: 6.13%
2023-10-13 03:40:34, CPU: 0.8%, Memory: 3.88%
2023-10-13 03:40:35, CPU: 0.2%, Memory: 3.88%
2023-10-13 03:40:36, CPU: 3.8%, Memory: 3.88%
2023-10-13 03:40:37, CPU: 0.4%, Memory: 3.89%
2023-10-13 03:40:38, CPU: 9%, Memory: 4.04%
2023-10-13 03:40:40, CPU: 3.5%, Memory: 3.81%
2023-10-13 03:40:41, CPU: 43%, Memory: 6.75%
2023-10-13 03:40:42, CPU: 0.2%, Memory: 3.81%
2023-10-13 03:40:43, CPU: 17%, Memory: 5.29%
2023-10-13 03:40:44, CPU: 1.9%, Memory: 3.81%
2023-10-13 03:40:46, CPU: 0.2%, Memory: 3.81%
2023-10-13 03:40:47, CPU: 4.4%, Memory: 4.00%
2023-10-13 03:40:48, CPU: 0.4%, Memory: 3.81%
2023-10-13 03:40:49, CPU: 35.9%, Memory: 7.01%
2023-10-13 03:40:50, CPU: 0%, Memory: 3.80%
2023-10-13 03:40:51, CPU: 21.6%, Memory: 5.53%
2023-10-13 03:40:53, CPU: 1%, Memory: 3.81%
2023-10-13 03:40:54, CPU: 0.4%, Memory: 3.81%
2023-10-13 03:40:55, CPU: 2.5%, Memory: 3.81%
2023-10-13 03:40:56, CPU: 0.2%, Memory: 3.80%
2023-10-13 03:40:57, CPU: 11.5%, Memory: 3.95%
2023-10-13 03:40:58, CPU: 0.2%, Memory: 3.81%
2023-10-13 03:41:00, CPU: 40.3%, Memory: 6.90%
2023-10-13 03:41:01, CPU: 0.2%, Memory: 3.81%
2023-10-13 03:41:02, CPU: 20.2%, Memory: 5.63%
2023-10-13 03:41:03, CPU: 0.2%, Memory: 3.81%
2023-10-13 03:41:04, CPU: 29%, Memory: 6.29%
2023-10-13 03:41:05, CPU: 0.8%, Memory: 3.81%
2023-10-13 03:41:07, CPU: 11.9%, Memory: 4.81%
2023-10-13 03:41:08, CPU: 2.1%, Memory: 3.80%
2023-10-13 03:41:09, CPU: 0.4%, Memory: 3.80%
2023-10-13 03:41:10, CPU: 8.3%, Memory: 3.93%
2023-10-13 03:41:11, CPU: 0.2%, Memory: 3.80%
2023-10-13 03:41:13, CPU: 37.1%, Memory: 6.96%
2023-10-13 03:41:14, CPU: 0%, Memory: 3.80%
2023-10-13 03:41:15, CPU: 18.3%, Memory: 5.32%
2023-10-13 03:41:16, CPU: 0.8%, Memory: 3.80%
2023-10-13 03:41:17, CPU: 0.4%, Memory: 3.80%
2023-10-13 03:41:18, CPU: 2.7%, Memory: 3.79%
2023-10-13 03:41:20, CPU: 0.2%, Memory: 3.80%
2023-10-13 03:41:21, CPU: 16.2%, Memory: 3.90%
2023-10-13 03:41:22, CPU: 0.2%, Memory: 3.80%
2023-10-13 03:41:23, CPU: 39.6%, Memory: 6.76%
2023-10-13 03:41:24, CPU: 0.4%, Memory: 3.80%
2023-10-13 03:41:25, CPU: 12.4%, Memory: 5.07%
2023-10-13 03:41:27, CPU: 0.4%, Memory: 3.80%
2023-10-13 03:41:28, CPU: 21.1%, Memory: 5.46%
"""

# Extract CPU and Memory usage using regex
cpu_usages = np.array([float(value) for value in re.findall(r'CPU: (\d+\.\d+)%', data)])
memory_usages = np.array([float(value) for value in re.findall(r'Memory: (\d+\.\d+)%', data)])

# Calculate the mean
mean_cpu = np.mean(cpu_usages)
mean_memory = np.mean(memory_usages)

# Calculate the standard deviation
std_cpu = np.std(cpu_usages)
std_memory = np.std(memory_usages)

# Calculate the 99% confidence interval
conf_int_cpu = stats.norm.interval(0.99, loc=mean_cpu, scale=std_cpu / np.sqrt(len(cpu_usages)))
conf_int_memory = stats.norm.interval(0.99, loc=mean_memory, scale=std_memory / np.sqrt(len(memory_usages)))

print(f"Mean CPU Usage: {mean_cpu:.2f}%")
print(f"Mean Memory Usage: {mean_memory:.2f}%")
print(f"99% Confidence Interval for CPU Usage: ({conf_int_cpu[0]:.2f}%, {conf_int_cpu[1]:.2f}%)")
print(f"99% Confidence Interval for Memory Usage: ({conf_int_memory[0]:.2f}%, {conf_int_memory[1]:.2f}%)")
