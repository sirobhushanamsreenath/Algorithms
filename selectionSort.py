# O(n^2) time | O(1) space
def selectionSort(array):
    for i in range(len(array)-1):
        least = i
        for j in range(i + 1, len(array)):
            if array[j] < array[least]:
                least = j
        swap(i, least, array)
    return array


def swap(x, y, array):
    array[x], array[y] = array[y], array[x]


print(selectionSort([-4, 5, 10, 8, -10, -6, -4, -
                     2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, -8]))
