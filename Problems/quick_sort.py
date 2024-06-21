'''
Bubble sort practice

'''
import numpy as np

sorted_array = []


def quick_sort(arr):
    
    print(arr)
    return arr


if __name__ == '__main__':

    array = np.random.randint(0, 100, 20)
    print('Original array:', array)

    sorted_array = quick_sort(array)
    print('Sorted array:', sorted_array)
