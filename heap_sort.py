def heapify(items, size, index, compare):
    """Пирамидальная перестройка подкучи."""
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and compare(items[left], items[largest]):
        largest = left

    if right < size and compare(items[right], items[largest]):
        largest = right

    if largest != index:
        items[index], items[largest] = items[largest], items[index]
        heapify(items, size, largest, compare)


def heap_sort(items, compare):
    """Пирамидальная сортировка списка."""
    size = len(items)
    for index in range(size // 2 - 1, -1, -1):
        heapify(items, size, index, compare)
    for index in range(size - 1, 0, -1):
        items[0], items[index] = items[index], items[0]
        heapify(items, index, 0, compare)
