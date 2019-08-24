def insertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        k = i
        while k > 0 and temp < array[k-1]:
            array[k] = array[k - 1]
            k -= 1
        array[k] = temp
    return array


print(insertionSort([-4, 5, 10, 8, -10, -6, -4, -
                     2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, -8]))
