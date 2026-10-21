import random


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        if arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    return arr


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        arr.append(random.randint(-10000, 10000))

    print("Unsorted array:", arr)

    insertion_sort(arr)
    print("Sorted array:", arr)

#Time Complexity:
# Best case: O(n) - when the array is already sorted
# Average case: O(n^2) - when the array elements are in random order
# Worst case: O(n^2) - when the array is sorted in reverse order

# Is insertion sort stable?
'''Yes. Equal values are not shifted across each other because the shift condition uses arr[position] > key, not arr[position] >= key. Equal values keep original relative order.'''

# Is insertion sort adaptive?
'''Yes. Nearly sorted arrays need fewer shifts. An already sorted array needs only one failed comparison for each key value, so the best-case time is linear.'''

# Why can insertion sort perform well on small arrays?
'''Insertion sort has low overhead, simple loops, and in-place updates. Many hybrid sorting algorithms use insertion sort for small subarrays after a faster divide-and-conquer method has reduced the problem size.'''

# Can binary search make insertion sort run in O(n log n) time?
'''No for array insertion sort. Binary search can reduce comparisons needed to find the insertion position, but shifting values still costs up to O(n) per key. The overall time remains O(n^2) in the worst case.'''