def fibonacci_sequence(arr, n):
    if n == 0:
        return []
    elif n == 1:
        return [arr[0]]
    elif n == 2:
        return [arr[0], arr[1]]
    else:
        if len(arr) < 2:
            difference = 2 - len(arr)
            for i in range(difference):
                arr.append(0)
        new_arr = arr.copy()
        for i in range(n-len(arr)):
            fibonacci = arr[0] + arr[1]
            new_arr.append(fibonacci)
            arr.append(fibonacci)
            arr.pop(0)
    return new_arr
