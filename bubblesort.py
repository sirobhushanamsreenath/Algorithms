# Write a function that takes in an array of integers and returns a sorted version of that array.
# Use the bubble sort algorithm to sort the array.

# Example :
# Sample Input : [8,5,2,9,5,6,3]
# Sample Output : [2,3,5,5,6,8,9]

# Test Cases:

# Test case 1:
# Sample Input :[1]
# Sample Output : [1]

# Test case 2:
# Sample Input :[1,2]
# Sample Output : [1,2]

# Test case 3:
# Sample Input :[2,1]
# Sample Output : [1,2]

# Test case 4:
# Sample Input :[1,3,2]
# Sample Output : [1,2,3]

# Test case 5:
# Sample Input :[3,1,2]
# Sample Output : [1,2,3]

# Test case 6:
# Sample Input :[1,2,3]
# Sample Output : [1,2,3]

# Test case 7:
# Sample Input :[-4,5,10,8,-10,-6,-4,-2,-5,3,5,-4,-5,-1,1,6,-7,-6-7,8]
# Sample Output : [-10,-7,-7,-6,6,-5,-5,-4,-4,-4,-2,-1,1,3,5,5,6,8,8,10]

# Test case 8:
# Sample Input :[-7,2,3,8,-10,4,-6,-10,-2,-7,10,5,2,9,-9,-5,3,8]
# Sample Output : [-10,-10,-9,-7,-7,-6,-5,-2,2,2,3,3,4,5,8,8,9,10]


def bubblesort(array):
    i = 0
    isSorted = False
    while i < len(array):
        isSorted = True
        for j in range(0, len(array) - 1, 1):
            if array[j] > array[j + 1]:
                swap(array, j, j+1)
                isSorted = False
        i += 1
    return array

    # for i in range(len(array)):

    # return array


def swap(array, x, y):
    array[x], array[y] = array[y], array[x]


print(bubblesort([-4, 5, 10, 8, -10, -6, -4, -
                  2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]))
