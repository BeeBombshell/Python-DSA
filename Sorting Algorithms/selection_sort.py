def selection_sort(list1):
for i in range(0, len(list1) - 1):
smallest = i
for j in range(i + 1, len(list1)):
if list1[j] < list1[smallest]:
smallest = j
list1[i], list1[smallest] = list1[smallest], list1[i]
return list1
