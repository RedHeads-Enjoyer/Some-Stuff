def bucketsort(arr):
    if not len(arr):
        return []
    k = max(arr) + 1
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

# coverage run --branch -m pytest test_p12.py
# coverage report
