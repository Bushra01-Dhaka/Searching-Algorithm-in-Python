# Searching-Algorithm-in-Python

## Binary Search:
Binary search is an efficient algorithm used to find the position of a target value in a sorted array. It works by repeatedly dividing the search interval in half:
Start with the middle element of the array.
If the middle element equals the target, return its position.
If the target is smaller, search the left half; if larger, search the right half.
Repeat until the target is found or the interval is empty.
The time complexity is O(log n), making it faster than linear search for large datasets.

```python
def binary_search(sequence, item):
    start_index = 0
    end_index = len(sequence) - 1

    while start_index <= end_index:
        mid_point = start_index + (end_index - start_index) // 2
        mid_point_value = sequence[mid_point]
        if mid_point_value == item:
            return mid_point
        elif item < mid_point:
            end_index = mid_point - 1
        else:
            start_index = mid_point + 1

    return None

sequence_a = [2,4,6,8,10,16,23,30,45]
item_a = 23
print("Item is present at index: ", binary_search(sequence_a,item_a))
```
