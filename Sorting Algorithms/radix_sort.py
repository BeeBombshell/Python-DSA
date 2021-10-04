def countingSort(inputArray):
    maxEl = max(inputArray)

    countArrayLength = maxEl+1
    countArray = [0] * countArrayLength

    for el in inputArray: 
        countArray[el] += 1

    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray

inputArray = [2,2,0,6,1,9,9,7]
print("Input array = ", inputArray)

sortedArray = countingSort(inputArray)
print("Counting sort result = ", sortedArray)
