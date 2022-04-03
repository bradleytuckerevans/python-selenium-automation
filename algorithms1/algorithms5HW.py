#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return sorted(arr, reverse=True)

test_arr = [6, 3, 8, 1, 9, 3]
print(selection_sort(test_arr))



# bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return sorted(arr, reverse=True)

test_num = [5, 6, 2, 9, 11, 3]

print(bubble_sort(test_num))

#insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return sorted(arr, reverse=True)

test_numbs = [4, 2, 6, 2, 8, 9]

print(insertion_sort(test_numbs))


#merge sort


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0

    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue

        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] <= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1

    return sorted(merged_array, reverse=True)

test_case = [4, 8, 2, 1, 9]
print(merge_sort(test_case))



""""" difference is sort and sorted
list_numbers = [1, 6, 1, 9, 2]
sorted_list_numbers = sorted(list_numbers)

print(list_numbers)
print(sorted_list_numbers)

list_numbers.sort()

print(list_numbers)


list_words = ['banana', 'apple', 'orange', 'book', 'cat']
print(sorted(list_words))
print(sorted(list_words, key=len))
print(sorted(list_words, key=len, reverse=True))
"""