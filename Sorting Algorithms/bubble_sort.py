import random


def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        arr.append(random.randint(-10000, 10000))

    print("Unsorted array:", arr)

    bubble_sort(arr)
    print("Sorted array:", arr)

# Time Complexity:
# Best case: O(n) - when the array is already sorted
# Average case: O(n^2) - when the array elements are in random order
# Worst case: O(n^2) - when the array is sorted in reverse order

# Is bubble sort stable?
'''Yes. Equal values are not swapped because the comparison uses > instead of >=. Equal values keep the original relative order after sorting.'''

# Is bubble sort an in-place sorting algorithm?
'''Yes. Standard bubble sort rearranges values inside the same array. Only a temporary value and a few variables are needed.'''

# Why does the largest value reach the end after one pass?
'''Whenever the largest remaining value is compared with a smaller neighbor on the right, a swap moves the largest value one position right. Repeated adjacent comparisons carry the largest value to the right boundary.'''

# Why can optimized bubble sort finish in linear time for a sorted array?
'''A sorted array causes no swaps during the first pass. The swapped flag remains false, so the algorithm stops after n - 1 comparisons.'''

# How does bubble sort differ from selection sort?
'''Bubble sort repeatedly swaps adjacent values and can perform many swaps. Selection sort scans for the minimum value during each pass and usually performs one swap per pass.'''