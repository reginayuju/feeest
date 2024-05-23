'''
Bubble sort practice

'''
import numpy as np


def bubble_sort(arr):

    return arr


if __name__ == '__main__':
    np.random.seed(0)
    array = np.random.randint(0, 100, 10)
    print('Original array:', array)

    sorted_array = bubble_sort(array)
    print('Sorted array:', sorted_array)
