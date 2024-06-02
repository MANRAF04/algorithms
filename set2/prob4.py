# Names:    Balamotis Panagiotis    Raftopoulos Emmanouil
# AEM:      03726                   03735
 
gains = [
    [1.5, 3.0, 4.2, 5.0, 5.6],
    [1.4, 2.6, 3.8, 4.8, 5.9],
    [1.6, 3.0, 4.0, 4.3, 5.0],
]

def max_gain(i, gain, j):
    if j < 0 or i >= len(gains):
        print (f"Leaving recursion {i}") 
        return 0
    for k in range(j, -1, -1):
        gain = max(gain , gains[i][k] + max(max_gain(i+1, 0, j-k-1), max_gain(i+2, 0, j-k-1)))
        print("gain", gain, "k", k)
    return gain
gain = 0    
gain = max_gain(0, gain, 4)
print("Optimal Flight Schedule:", gain)
