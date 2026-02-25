#!/usr/bin/env
import insertion

def sort_bucket(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    max_value = max(arr)
    buckets = [[] for _ in range(n)]
    
    for num in arr:
        normalized_index = num / (max_value + 1)
        bucket_index = int(normalized_index * n)
        buckets[bucket_index].append(num)
    
    print("Buckets before sorting:", buckets)
    result = []
    for bucket in buckets:
        if bucket:
            insertion.sort_insertion(bucket)
            result.extend(bucket)
    
    return result

if __name__ == "__main__":
    arr = [57, 1, 4, 12, 8, 3, 22, 4, 5, 6, 7, 19]
    print("Original array:", arr, end="\n")
    a = sort_bucket(arr)
    print("Sorted array using bucket sort:", a)