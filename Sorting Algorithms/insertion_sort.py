def Insertion_Sort(list1):
  for i in range(1,len(list1)):
    temp = list1[i]
    j = i-1
  while j>=0 and list1[j] > temp:
    list1[j+1] = list1[j]
    j = j-1
    list1[j+1] = temp
  return list1
