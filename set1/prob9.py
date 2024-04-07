def find_pair_of_sum(arr: list, n: int):
  map = {}

  for i in range(n):
    for j in range(i + 1, n):
      sum = arr[i] * arr[i] + arr[j] * arr[j]
      diff = arr[i] * arr[i] - arr[j] * arr[j]

      if (sum in map and map[sum] < 0) or (diff in map and map[diff] > 0):
        return 1
      else:
        map[sum] = sum
        map[diff] = -diff

  return 0


# Driver code
if __name__ == "__main__":
  arr = [15,112,113,140]
  n = len(arr)
  res = find_pair_of_sum(arr, n)
  print(res)
