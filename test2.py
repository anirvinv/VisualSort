def insertion_sort(arr):
    array = arr.copy()

    for i in range(1, len(array)):
        for j in range(len(array)):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
    return array


# print(insertion_sort([5, 4, 5, 7, 3, 1, 1, 3]))


def lightUpIndices(arraySizes):
    sizes = arraySizes.copy()
    indices = []
    # indices.append([i for i in range(sizes[0])])
    count = 0
    for size in sizes:
        indices.append([i + count for i in range(size)])
        count += size
    return indices


print(lightUpIndices([4, 4, 4, 4, 3]))
