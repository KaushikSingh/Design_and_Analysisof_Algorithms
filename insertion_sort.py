Insertion Sort:


import time
import random
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
L = []
for i in range(20):
    L.append(int(input("Enter a number")))
start = time.clock()
insertionSort(L)
end = time.clock()
print("Sorted array is:")
print L
print("The program ran for ",end-start," seconds")




