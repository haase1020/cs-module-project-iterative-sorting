# TO-DO: Complete the selection_sort() function below
arr = [3, 1, 5, 4, 2]
cur_index = 0
smallest_index = cur_index


# def selection_sort(arr):
#     # from CS30
#     # # loop through n-1 elements
#     # i = 0
#     # while i < len(arr):
#     #     min = arr[i]
#     #     index = i
#     #     for j in range(i+1, len(arr)):
#     #         if arr[j] < min:
#     #             index = j
#     #             min = arr[j]
#     #     arr[i], arr[index] = arr[index], arr[i]
#     #     i += 1

#     # return arr

#     # Tim's solution from CS34
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         for n in range(cur_index, len(arr)):
#             if arr[n] < arr[smallest_index]:
#                 smallest_index = n
#         arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
#     return arr


# print(selection_sort(arr))


# def bubble_sort(arr):
#     length = len(arr)
#     for i in range(0, length - 1):
#         for j in range(0, length - 1):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#                 j+1
#         i + 1
#     return arr
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for idx in range(len(arr) - 1):
            num1 = arr[idx]
            num2 = arr[idx + 1]
            if num1 > num2:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swapped = True
    return arr


print(bubble_sort(arr))

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


# def counting_sort(arr, maximum=None):
#     # Your code here

#     return arr
