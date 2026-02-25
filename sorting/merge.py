#!/usr/bin/env

def sort_merge(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    al = sort_merge(arr[:mid])
    ar = sort_merge(arr[mid:])

    merged, i, j = [], 0, 0
    while i < len(al) and j < len(ar):
        if al[i] <= ar[j]:
            merged.append(al[i])
            i += 1
        else:
            merged.append(ar[j])
            j += 1

    merged.extend(al[i:])
    merged.extend(ar[j:])

    return merged

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    print("Original array:", arr)
    a = sort_merge(arr)
    print("Sorted array:", a)