import random


def selection_sort(arr : list[int]) -> list[int]:
    n=len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    arr=[]
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        arr.append(random.randint(-10000, 10000))

    print("Unsorted array:", arr)

    selection_sort(arr)
    print("Sorted array:", arr)

# Time Complexity:
# Best case: O(n^2) - when the array is already sorted
# Average case: O(n^2) - when the array elements are in random order
# Worst case: O(n^2) - when the array is sorted in reverse order


# Can selection sort handle duplicate elements properly?
'''Yes, selection sort can handle duplicate elements effectively. It correctly places all elements, including duplicates, in sorted order. However, standard selection sort is not stable, so it does not guarantee preservation of the relative order of equal elements.'''

# What happens if the array is already sorted? Is it still efficient?
'''Selection sort doesn’t check if the array is already sorted—it always performs O(n2) comparisons because the algorithm doesn’t adapt to sorted inputs. While no swaps may occur if the array is sorted, the comparisons in the inner loop are still executed, making it inefficient for pre-sorted data.'''

# Is selection sort stable?
'''No, selection sort is not stable. Stability in sorting algorithms means that equal elements retain their relative order after sorting. Since selection sort may swap non-adjacent elements, it can change the relative order of equal elements, making it unstable.'''

# Selection sort has O(n2) time complexity. Can you identify a scenario where selection sort might still be a preferred choice?
'''1. Selection sort works in-place and uses O(1) extra memory. For systems with strict memory limitations, it is a viable choice. 2. For small arrays (e.g., fewer than 10 elements), the simplicity of selection sort can outweigh its inefficiency. The overhead of more complex algorithms, like merge sort or quicksort, might not be justified. Example: Sorting [5, 2, 1] in embedded systems with limited RAM can efficiently use selection sort.'''

# How does selection sort compare to insertion sort in terms of performance and use cases? Can you analyze and contrast them?
'''Time Complexity: Both have O(n^2) worst-case time complexity. However, insertion sort can outperform selection sort for nearly sorted arrays because it minimizes shifts, while selection sort always performs n−1 comparisons in the inner loop, regardless of the array's state. Swaps vs. Shifts: Selection sort minimizes swaps (n−1 swaps in total), making it suitable for situations where swap costs are high (e.g., flash memory). Insertion sort involves more shifts, especially for large unsorted portions. Example: For an array like [2, 3, 4, 5, 1], insertion sort will quickly sort it with fewer operations because most elements are already in place. In contrast, selection sort performs the same number of comparisons regardless of the initial order, making it less efficient in this case.'''