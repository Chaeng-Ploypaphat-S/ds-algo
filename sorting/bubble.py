#!/usr/bin/env

def sort_bubble(arr: list[int]) -> None:
    n = len(arr)
    for _ in range(n):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    print("Original array:", arr)
    sort_bubble(arr)
    print("Sorted array:", arr)