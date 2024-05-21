import matplotlib.pyplot as plt

def calculate_average(file_path):
    data = {}
    counts = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            level, iter, value = line.strip().split()
            key = (int(level), int(iter))
            data[key] = data.get(key, 0) + float(value)
            counts[key] = counts.get(key, 0) + 1
    
    averages = {}
    for key in data:
        averages[key] = data[key] / counts[key]
    
    return averages

file_path = 'USAcpls.txt'
averages = calculate_average(file_path)
print(averages)
print()
# Sort the averages dictionary by level and iteration
sorted_averages = dict(sorted(averages.items(), key=lambda x: x[0]))
print(sorted_averages)
# sorted_averages = sorted(averages.items(), key=lambda x: (int(x[0][0]), int(x[0][1])))

# # Extract the x and y values from the sorted averages
x_values = [f"{level}{iter}" for (level, iter) in sorted_averages.keys()]
y_values = list(sorted_averages.values())

# # Plot the line graph
plt.plot(x_values, y_values)

# # Set the labels for x and y axes
plt.xlabel('Level and Iteration')
plt.ylabel('Averages')

# # Show the plot
plt.show()