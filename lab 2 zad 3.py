def bubbleSort(arr):
    n = len(arr)


    for i in range(n):


        for j in range(0, n - i - 1):


            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]

    bubbleSort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])

import sys

A = [64, 25, 12, 22, 11]

for i in range(len(A)):


    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i], end=" , ")