# Task 2 Study Report Outline (Heap + Heap Sort)

Use this outline to draft the final PDF main content (max 3 pages of text).

## 1. Introduction
- State selected topics:
  - New data structure: Max Heap
  - New algorithm: Heap Sort
- Brief motivation:
  - Heap supports efficient priority management.
  - Heap Sort gives stable worst-case time complexity `O(n log n)`.

## 2. Data Structure: Heap
### 2.1 ADT Definition
- A heap is a complete binary tree represented by an array.
- In max heap, each parent value is greater than or equal to its children.

### 2.2 Core Operations and Complexity
- `insert(x)`: `O(log n)`
- `extract_max()`: `O(log n)`
- `peek()`: `O(1)`
- `build_heap(values)`: `O(n)`

### 2.3 Implementation Notes
- Array index mapping:
  - parent = `(i - 1) // 2`
  - left child = `2 * i + 1`
  - right child = `2 * i + 2`
- Heap property maintained by:
  - heapify up (after insertion)
  - heapify down (after extraction/build)

### 2.4 Application Examples
- Priority queue for scheduling
- Top-k queries
- Foundation for heap-based algorithms

## 3. Algorithm: Heap Sort
### 3.1 Procedure
1. Build max heap from input array.
2. Swap root with last unsorted element.
3. Shrink heap and heapify root.
4. Repeat until sorted.

### 3.2 Complexity Analysis
- Build heap: `O(n)`
- Loop of extraction and heapify: `O(n log n)`
- Overall: `O(n log n)` in best/average/worst cases
- Space: `O(1)` extra (in-place)

### 3.3 Demonstration Cases
- Random input
- Duplicate values
- Already sorted input
- Reverse sorted input
- Single-element input
- Empty input

Include one concise result table in appendix:
- columns: test case, input size, output correctness (PASS/FAIL), remarks

## 4. Discussion and Reflection
- Strengths:
  - clear theoretical guarantee
  - in-place sorting
  - strong connection between ADT and algorithm
- Limitations:
  - not a stable sort
  - practical constants may be larger than some alternatives on small inputs
- Possible improvements:
  - benchmark against quick sort / merge sort
  - add min-heap variation and priority queue use case

## 5. References and Declaration Notes
- List all external references used for learning.
- If AI tools are used, declare usage according to course requirement.
- Ensure explanations are original and not code-only content.
