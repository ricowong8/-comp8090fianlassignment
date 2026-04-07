# Task 2: Self-Study (Heap + Heap Sort)

## 1) Introduction
This folder demonstrates self-study on:
- New data structure: **Max Heap**
- New algorithm: **Heap Sort**

The implementation includes code, runnable examples, and analysis notes so it can be referenced directly in the study report.

## 2) File Structure
- `heap_example.py`: Max Heap ADT implementation and operation demo
- `heapsort_example.py`: Heap Sort implementation with multiple test cases
- `user_guide.md`: How to run the code and interpret outputs
- `study_report_outline.md`: Report-ready writing structure for the final PDF

## 3) Data Structure: Heap (ADT)
### Definition
A heap is a complete binary tree stored in an array.
For **Max Heap**, each parent node is greater than or equal to its children.

### Core ADT Operations
- `insert(x)`: add a new element and restore heap property
- `extract_max()`: remove and return the maximum value
- `peek()`: return the maximum value without removal
- `is_empty()`: check whether heap contains elements
- `size()`: return number of elements
- `build_heap(values)`: convert an unsorted array into a valid heap

### Time Complexity (Max Heap)
- `peek`, `is_empty`, `size`: **O(1)**
- `insert`: **O(log n)**
- `extract_max`: **O(log n)**
- `build_heap`: **O(n)**

### Example Applications
- Priority queue (job scheduling, event handling)
- Top-k problems (e.g., largest k values)
- Graph algorithms (often with min-heap, e.g., shortest path)

## 4) Algorithm: Heap Sort
### Idea
1. Build a max heap from input array.
2. Swap heap root (maximum) with last unsorted element.
3. Reduce heap size and heapify root.
4. Repeat until the array is sorted.

### Complexity Analysis
- Build max heap: **O(n)**
- Repeated extraction + heapify: **(n - 1) * O(log n)**
- Total: **O(n log n)** (best/average/worst)
- Extra space: **O(1)** for in-place array operations (ignoring recursion call stack)

### Why Heap Sort
- Predictable worst-case complexity: `O(n log n)`
- In-place sorting (no additional array allocation)
- Good educational connection between data structure and algorithm

## 5) Demonstration Coverage
`heapsort_example.py` includes test cases for:
- random numbers
- duplicate values
- already sorted input
- reverse sorted input
- single element
- empty list

Each test prints input, output, expected result, and PASS/FAIL status for easy verification.

## 6) How to Run
Use Python 3:

```bash
python3 task2/heap_example.py
python3 task2/heapsort_example.py
```

See `task2/user_guide.md` for details and expected output style.

## 7) Notes for Final Submission
- In the final report, explain concepts with your own words.
- Include complexity analysis and sample outputs (not code only).
- Acknowledge any external reference used during self-study.
