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


def binary_search(find_num, sorted_array):
    L = 0
    R = len(sorted_array) - 1
    while L <= R:
        m = int(L + (R - L) / 2)
        if sorted_array[m] < find_num:
            L = m + 1
        if sorted_array[m] > find_num:
            R = m - 1
        if sorted_array[m] == find_num:
            print("yes")
            break
            
        if L > R:
            break
        print("no")


    # print("yes or no")


if __name__ == '__main__':
    # array = np.random.randint(0, 100, 20)
    array = [5, 28, 30, 40, 22, 45, 78, 98, 33, 45, 66, 77]
    print('Original array:', array)

    sorted_array = bubble_sort(array)
    print('Sorted array:', sorted_array)

    find_num =34
    binary_search(find_num, sorted_array)
