# Sorting

## 1. Bubble Sort

Bubble sort repeatedly steps through a slice and compares adjacent elements, eswapping them if they are out of order. jit continues to loop over the slice until the while list is completely sorted.

```
1. set `swapping` to `True`
2. set `end` to the length of the input list
3. While `swapping` is `True`
    a. set `swapping` to `False`
    b. for `i` from the 2nd element to `end`:
        - if the `(i - 1)`th element of the input list is greater than the `i`th element:
            - swap the `(i - 1)`th element and the `i`th element
            - set `swapping` to `True`
    c. Decrement `end` by one
4. return the sorted list

```

```python
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

```

## 2. Merge Sort

Merge sort is a recursive sorting algorithm that uses divide and conquer:
- Divide: divide the large problem into smaller problems, and recursively solve the smaller problems
- Conquer: combine the results of the smaller problems to solve the larger problem

```python

def merge_sort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    sorted_left = merge_sort(nums[:mid])
    sorted_right = merge_sort(nums[mid:])
    return merge(sorted_left, sorted_right)

def merge(first, second):
    merged = []
    i = j = 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    merged.extend(first[i:])
    merged.extend(second[j:])

    return merged
```

## 3. Insertion Sort

Insertion sort builds a sorted list one item at a time.

```python
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >=0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
```

## 4. Quick Sort

Quick sort is an efficient sorting algorithm that's widely used in production sorting implementations. Like merge sort, quick sort is a recursive divide and conquer algorithm.

```python
def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)
    return nums

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

```

## 5. Selection Sort

Similar to bubble sort, selection sort works through the list repeatedly swapping items in a list. It's slightly more efficient than bubble sort because it only makes one swap per iteration.

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
```
