def find_target(arr, target):
    for i in arr:
        for j in arr:
            if arr.index(j) == arr.index(i):
                continue
            if i + j == target:
                return [arr.index(i), arr.index(j)]
            else:
                continue
    return "Target not found"


print(find_target([2, 7, 11, 15], 9))

