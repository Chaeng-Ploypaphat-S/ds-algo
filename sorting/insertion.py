#!/usr/bin/env

def sort_insertion(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        val = arr[i]
        if val < arr[i - 1]:
            j = i - 1
            while j >= 0 and arr[j] > val:
                arr[j + 1] = arr[j]
                j -= 1
            # Place the value in its correct position
            arr[j + 1] = val

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8, 11, 0, 3, 6, 7, 9]
    print("Original array:", arr)
    sort_insertion(arr)
    print("Sorted array:", arr)