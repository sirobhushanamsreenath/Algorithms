# Write a function that takes an array of integers and returns a sorted version of array.
# use Merge sort


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1
        return array
    else:
        return array


print(mergeSort([-4, 5, 10, 8, -10, -6, -4, -
                 2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, -8]))
