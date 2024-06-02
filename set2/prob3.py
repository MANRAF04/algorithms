# Names:    Balamotis Panagiotis    Raftopoulos Emmanouil
# AEM:      03726                   03735
 

def printItems(K,W,n):
    w = W
    for i in range(n,0,-1):
        if K[i][w] != K[i-1][w]:
            print(f"Item {i} with weight {weight[i-1]} and value {profit[i-1]}")
            w = w - weight[i-1]

def printArray(K):
    print()
    print()
    
    for i in range(len(K[0])):
        print("%03d "% (i),end=' ')
    print()
    for i in K:
        for j in i:
            print("%03d "% (j),end=' ')
        print()

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
        printArray(K)
    return K


# Driver code
if __name__ == '__main__':
    profit = [8,5,7,3,11]
    weight = [12,9,5,5,8]
    W = 25
    n = len(profit)
    K = knapSack(W, weight, profit, n)
    print(K[n][W])
    printItems(K,W,n)