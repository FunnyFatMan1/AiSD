def binary_search(L, Y):
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = L[mid]

        if guess == Y:
            return mid
        if guess > Y:
            high = mid - 1
        else:
            low = mid + 1
    return None
