#!/usr/bin/env

def partition(arr: list[int], start: int, end: int) -> int:
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        # Move elements smaller than or equal to pivot to the left
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i

def sort_quick(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = partition(arr, 0, len(arr) - 1)
    left = sort_quick(arr[:pivot])
    right = sort_quick(arr[pivot + 1:])
    return left + [arr[pivot]] + right

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8, 3, 2, 4, 5, 6, 7, 9]
    print("Original array:", arr)
    a = sort_quick(arr)
    print("Sorted array using quick sort:", a)