#!/usr/bin/env

def sort_counting(arr: list[int]) -> list[int]:
    """counting sorting algorithm that supports
       both negative and positive integers.
    """
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    freq = [0] * (max_val - min_val + 1)
    for num in arr:
        freq[num - min_val] += 1
        
    sorted_arr = []
    for i, count in enumerate(freq):
        sorted_arr.extend([i + min_val] * count)
    return sorted_arr

if __name__ == "__main__":
    arr = [5, -1, 4, 2, 8, 3, 2, -4, -5, 6, 7, 9]
    print("Original array:", arr)
    a = sort_counting(arr)
    print("Sorted array using counting sort:", a)