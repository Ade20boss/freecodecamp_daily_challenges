def second_largest(arr):
    largest = max(arr)
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    arr = new_arr
    arr.pop(arr.index(largest))
    second_largest = max(arr)
    return second_largest

second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0])
