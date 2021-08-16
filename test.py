import random


def merge_sort(array):

    if len(array) == 1:
        return array

    middle = (len(array))//2

    L = array[:middle]
    R = array[middle:]

    left = merge_sort(L)
    right = merge_sort(R)

    return merge(left, right)


def merge(*arrays):
    # accepts only 1 array or two arrays

    if len(arrays) == 1:
        print("only one array passed")
        return arrays

    arr1 = arrays[0].copy()
    arr2 = arrays[1].copy()
    final_length = len(arr1) + len(arr2)

    merged = []

    while not len(merged) == final_length:
        if len(arr1) == 0:
            merged += arr2
            break
        elif len(arr2) == 0:
            merged += arr1
            break

        if arr1[0] <= arr2[0]:
            merged += [arr1.pop(0)]
        else:
            merged += [arr2.pop(0)]

    return merged


def iterative_merge_sort(array):
    copy = [[i] for i in array]
    copy1 = []
    i = 0
    while i < len(copy) - 1:
        copy1 += [merge(copy[i], copy[i + 1])]
        i += 2
    if not len(copy) % 2 == 0:
        copy1 += [copy[-1]]

    n = len(array)
    group_size = 2

    while group_size < n:
        copy2 = []
        j = 0
        while j < len(copy1) - 1:
            copy2 += [merge(copy1[j], copy1[j+1])]
            group_size = len(copy2[0])
            j += 2
        if not len(copy1) % 2 == 0:
            copy2 += [copy1[-1]]
        copy1 = []
        k = 0
        while k < len(copy2) - 1:
            copy1 += [merge(copy2[k], copy2[k+1])]
            group_size = len(copy1[0])
            k += 2
        if not len(copy2) % 2 == 0:
            copy1 += [copy2[-1]]

    return copy1[0]


l = [random.randint(1, 20) for i in range(22)]

print(l)
print()
print(merge_sort(l))
print(iterative_merge_sort(l))
