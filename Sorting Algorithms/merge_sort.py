import random


def merge(arr: list[int], low:int, mid:int, high:int) -> list[int]:
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[low + i + j] = left[i]
            i += 1
        else:
            arr[low + i + j] = right[j]
            j += 1
    while i < len(left):
        arr[low + i + j] = left[i]
        i += 1
    while j < len(right):
        arr[low + i + j] = right[j]
        j += 1
    print("Merge of array", arr[low:high + 1])
    return arr


def merge_sort(arr: list[int], low:int, high:int) -> list[int]:
    print("Divide of array", arr[low:high + 1])
    if low < high:
        mid=(low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
    return arr


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        arr.append(random.randint(-10000, 10000))

    print("Unsorted array:", arr)

    merge_sort(arr, 0, n - 1)
    print("Sorted array:", arr)
