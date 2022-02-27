import random as r


def copy(source, dest):
    dest.clear()
    for value in source:
        dest.append(value)


def populate(arr, n):
    arr.clear()
    for i in range(0, n):
        arr.append(r.randint(0, n - 1))


def populate_reverse(arr, n):
    arr.clear()
    for i in range(n - 1, -1, -1):
        arr.append(i)


def exch(arr, j, k):
    temp = arr[j]
    arr[j] = arr[k]
    arr[k] = temp


def bubble(arr):
    for i in range(0, len(arr) - 1):
        swap = False
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                exch(arr, j, j + 1)
                swap = True
        if not swap:
            return


def insertion(arr):
    for i in range(1, len(arr)):
        pos = i
        value = arr[pos]
        while pos > 0 and value < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = value


def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)

        l_pos = 0
        r_pos = 0
        pos = 0

        while l_pos < len(left) and r_pos < len(right):
            if left[l_pos] < right[r_pos]:
                arr[pos] = left[l_pos]
                l_pos += 1
            else:
                arr[pos] = right[r_pos]
                r_pos += 1
            pos += 1

        while l_pos < len(left):
            arr[pos] = left[l_pos]
            l_pos += 1
            pos += 1

        while r_pos < len(right):
            arr[pos] = right[r_pos]
            r_pos += 1
            pos += 1


def quick(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range (1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick(left) + [pivot] + quick(right)


