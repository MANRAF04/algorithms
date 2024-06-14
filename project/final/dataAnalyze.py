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

def getMax(file_path):
    max_nodes = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            # print(line.strip())
            level, nodes = line.strip().split()
            level = int(level)
            nodes = int(nodes)
            
            if level in max_nodes:
                max_nodes[level] = max(max_nodes[level], nodes)
            else:
                max_nodes[level] = nodes
    
    return max_nodes

file_path = 'karatecpls.txt'
# averages = calculate_average(file_path)
# sorted_averages = dict(sorted(averages.items(), key=lambda x: x[0]))

file_path = 'max_erdos.txt'
# max_nodes = getMax(file_path)
# print(max_nodes)

# Extract the x and y values from the max_nodes dictionary
# x_values = list(max_nodes.keys())
# y_values = list(max_nodes.values())

# # Plot the line graph
# plt.plot(x_values, y_values, marker='.', linestyle='')

# # Set the labels for x and y axes
# plt.xlabel('Level')
# plt.ylabel('Max Nodes')

# # Show the plot
# plt.show()
# # Extract the x and y values from the sorted averages
# x_values = [f"{level}{iter}" for (level, iter) in sorted_averages.keys()]
# y_values = list(sorted_averages.values())

# # # Plot the line graph
# plt.plot(x_values, y_values, marker='.', linestyle='')

# # # Set the labels for x and y axes
# plt.xlabel('Level and Iteration')
# plt.ylabel('Averages')

# # plt.figure(figsize=(12, 6))  # Adjust figure size as needed
# plt.subplots_adjust(bottom=0.15)  # Adjust space for x-axis labels

# # # Show the plot
# plt.show()

KarateTime = 0.0066258907318115234
USATime = 91.77580571174622
Erdos = 7122.201397180557
x_values = [34, 4941, 6927]
y_values = [KarateTime, USATime, Erdos]

# Plot the line graph
plt.plot(x_values, y_values, linestyle='-')

# Set the labels for x and y axes
plt.xlabel('Nodes')
plt.ylabel('Time (s)')

# Show the plot
plt.show()