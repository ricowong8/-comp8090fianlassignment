# Task 2: Self-Study Report

## 📖 Overview
This task demonstrates self-study on one new **data structure** and one new **algorithm** not covered in the course.  
Chosen topics:
- Data Structure: **Heap**
- Algorithm: **Heap Sort**

---

## 🗂 Data Structure: Heap
### Abstract Data Type (ADT)
- A **Heap** is a complete binary tree where each parent node is either:
  - **Max Heap**: parent ≥ children
  - **Min Heap**: parent ≤ children
- Operations:
  - `insert(element)`
  - `extract-max/min()`
  - `heapify()`

### Applications
- Priority queues (e.g., scheduling tasks)
- Graph algorithms (e.g., Dijkstra’s shortest path)
- Efficient selection problems (e.g., find k-th largest element)

---

## ⚙️ Algorithm: Heap Sort
### Process
1. Build a max heap from the input array.
2. Repeatedly extract the maximum element and place it at the end.
3. Heapify the remaining elements until sorted.

### Time Complexity
- Build heap: **O(n)**
- Each extraction: **O(log n)**
- Total: **O(n log n)**

### Example
Input: `[4, 10, 3, 5, 1]`  
Output: `[1, 3, 4, 5, 10]`

```python
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
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [4, 10, 3, 5, 1,12,9,8,6,11]
heap_sort(arr)
print(arr)  # [1, 3, 4, 5, 6, 8, 9, 10, 11, 12]
