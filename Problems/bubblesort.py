'''
Bubble sort practice

'''
import numpy as np

sorted_array = []


def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if (arr[i]) > (arr[i + 1]):
                b = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = b
    print(arr)
    return arr


if __name__ == '__main__':

    array = np.random.randint(0, 100, 20)
    print('Original array:', array)

    sorted_array = bubble_sort(array)
    print('Sorted array:', sorted_array)
