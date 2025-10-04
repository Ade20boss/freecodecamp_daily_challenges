def tribonacci_sequence(arr, n):
    if n == 0:
        return []
    elif n == 1:
        return [arr[0]]
    elif n == 2:
        return [arr[0], arr[1]]
    elif n == 3:
        return arr
    else:
        if len(arr) < 3:
            difference = 3 - len(arr)
            for i in range(difference):
                arr.append(0)
        new_arr = arr.copy()
        for i in range(n-len(arr)):
            tribonacci = arr[0] + arr[1] + arr[2]
            new_arr.append(tribonacci)
            arr.append(tribonacci)
            arr.remove(arr[0])
    return new_arr

print(tribonacci_sequence([123, 456, 789], 8))

