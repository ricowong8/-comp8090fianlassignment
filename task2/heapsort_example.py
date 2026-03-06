def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # create max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step by step extract elements from heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1,12,9,8,6,11]
    print("Original array:", arr)
    heap_sort(arr)
    print("Sorted array:", arr)
