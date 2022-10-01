def CountSort(arr):
    res = [0]*len(arr)
    count = [0]*10
    for i in range(len(arr)):
        count[arr[i]] = count[arr[i]] + 1
    for i in range(1, 10):
        count[i] = count[i] + count[i-1]
    i = len(arr) - 1
    while i >= 0:
        res[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i = i - 1
    return res

arr = input("Enter the list of numbers separated by commas: ")
arr = [int(ele) for ele in arr.split(",")]
print(CountSort(arr))
