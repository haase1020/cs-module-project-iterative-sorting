# TO-DO: Complete the selection_sort() function below
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         # Your code here

#         # TO-DO: swap
#         # Your code here

#     return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length - 1):
        for j in range(0, length - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                j+1
        i + 1
    return arr


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


def counting_sort(arr, maximum=None):
    # Your code here

    return arr


# #done as guided project (not part of project for today)
# def insertion_sort(input_list):
#     pass
#     # mark first item as sorted, separated first element?
#     # no code needed here, conceptual
#     for i in range(1, len(input_list)):
#     # for every item starting at the second element
#         #put item in a temp variable
#         current_item = input_list[i]

#         look_left_index = i - 1
#         #look left until we find where it belongs
#         # if not at beginning and
#         # current item is less than sorted
#         while look_left_index > 0 and current_item < input_list[look_left_index]:
#             input_list[look_left_index + 1] = input_list[look_left_index]
#             look_left_index -= 1

#         input_list[look_left_index] = current_item

#     return input_list
#             # insert item
