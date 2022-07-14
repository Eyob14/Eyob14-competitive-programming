def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j+1] < num[j]:
                num[j], num[j+1] = num[j+1], num[j]
    return num
def insertion_sort(num):
    for i in range(1, len(num)): # assume that the first element of the array is in the right order
        pivot = num[i]       # take the second element of the array as a pivot point to compare with the others
        j = i - 1           # store the index of index of the sorted array
        while (j >= 0) and pivot < num[j]:   # iterate as long as the index becomes 0 and all elements in the sorted direction are properly sorted
            num[j+1] = num[j]
            j -= 1
        num[j+1] = pivot
    return num

def selection_sort(num):
    for i in range(len(num)):
        min_index = i
        for j in range(min_index+1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num


# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * (max(array)+1)

    # Store the count of each elements in count array
    for i in array:
        count[i] += 1

    # Store the cummulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)





print(bubble_sort([4,3,5,7,1,3,8]))
print(insertion_sort([4,3,5,7,1,3,8]))
print(selection_sort([4,3,5,7,1,3,8]))