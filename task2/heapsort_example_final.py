"""
heapsort_example.py
-------------------
Heap Sort Algorithm — COMP8090SEF / COMP S209W Task 2
HKMU 2026 Spring Semester

Heap Sort is a two-phase, in-place, comparison-based sorting algorithm.

Phase 1  Build a Max-Heap from the input array in O(n) using Floyd's
         bottom-up heapify (more efficient than n individual insertions).

Phase 2  Repeatedly move the root (current maximum) to the end of the
         unsorted region, shrink the heap boundary by 1, and call
         heapify to restore the Max-Heap property.  After n-1 swaps
         the array is sorted in ascending order.

Complexity summary
──────────────────
    Time  : O(n log n) — best, average, and worst case (guaranteed)
    Space : O(1)       — fully in-place, no auxiliary array
    Stable: No         — equal elements may change their relative order
"""


def heapify(arr: list, heap_size: int, root_index: int) -> None:
    """
    Ensure the subtree rooted at *root_index* satisfies the max-heap rule.

    Assumes both the left and right subtrees are already valid max-heaps.
    Implemented iteratively to avoid Python's default recursion depth limit
    (~1 000 frames), which would fail on large inputs if implemented recursively.

    Time complexity : O(log n)  — traverses at most the subtree height.
    Space complexity: O(1)      — no additional memory allocated.

    Args:
        arr        : The list representing the heap, modified in-place.
        heap_size  : Number of elements in the active heap region.
                     Elements at index >= heap_size are already sorted.
        root_index : Index of the subtree root to sift downward.
    """
    while True:
        largest     = root_index
        left_child  = 2 * root_index + 1
        right_child = 2 * root_index + 2

        # Is the left child inside the heap and larger than current largest?
        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child

        # Is the right child inside the heap and larger than current largest?
        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child

        if largest == root_index:
            break                               # Subtree already satisfies heap rule

        # Swap the root with its largest child and continue sifting down
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        root_index = largest                    # Move focus to the swapped position


def heap_sort(arr: list) -> None:
    """
    Sort *arr* in ascending order using Heap Sort (in-place).

    The list is modified directly; no value is returned.

    Algorithm
    ─────────
    Phase 1 — Build Max-Heap  (O(n))
        Iterate from the last non-leaf node down to index 0.
        Calling heapify on each node bottom-up builds a valid Max-Heap.
        Last non-leaf node is at index n // 2 - 1.

    Phase 2 — Repeated extraction  (O(n log n))
        For each position from the last index down to 1:
            - Swap arr[0] (current max) with arr[end] → max is now in place.
            - Shrink the heap boundary (heap_size = end).
            - Call heapify(arr, end, 0) to restore Max-Heap on the remainder.

    Time complexity : O(n log n) — Phase 1: O(n) + Phase 2: O(n log n)
    Space complexity: O(1)       — sorting is done entirely within arr

    Args:
        arr: The list to sort.  Modified in-place.
    """
    n = len(arr)

    if n <= 1:
        return      # Nothing to sort for empty or single-element lists

    # ── Phase 1: Build Max-Heap using Floyd's bottom-up method ────────
    # Leaves (index >= n // 2) are trivially valid heaps.
    # Start from the last non-leaf and work toward the root.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # ── Phase 2: Extract the maximum one element at a time ────────────
    # After each iteration the sorted region at the right grows by 1.
    for end in range(n - 1, 0, -1):
        # Move the current maximum (root) to its final sorted position
        arr[0], arr[end] = arr[end], arr[0]

        # Restore Max-Heap property for the unsorted region [0, end)
        heapify(arr, end, 0)


# ── Test helper ───────────────────────────────────────────────────────

def run_test_case(name: str, values: list) -> bool:
    """
    Run one test case and print a formatted result line.

    Args:
        name  : Descriptive label for the test.
        values: Input list (will be sorted in-place by heap_sort).

    Returns:
        True if the result matches Python's built-in sort, False otherwise.
    """
    original = list(values)         # Keep a copy for display
    expected = sorted(values)       # Reference answer
    heap_sort(values)               # Sort in-place
    passed = (values == expected)

    status = "PASS" if passed else "FAIL"
    print(f"  [{status}]  {name}")
    print(f"         Input   : {original}")
    print(f"         Output  : {values}")
    if not passed:
        print(f"         Expected: {expected}")
    print()
    return passed


# ── Demo / test suite ─────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Heap Sort  —  Demonstration & Test Suite")
    print("=" * 55)
    print()

    test_cases = [
        ("random numbers",       [4, 10, 3, 5, 1, 12, 9, 8, 6, 11]),
        ("with duplicates",      [7, 3, 7, 2, 9, 2, 1]),
        ("negative numbers",     [0, -3, 15, -99, 42, -1]),
        ("already sorted",       [1, 2, 3, 4, 5, 6]),
        ("reverse sorted",       [9, 8, 7, 6, 5, 4, 3]),
        ("all identical",        [5, 5, 5, 5]),
        ("single element",       [42]),
        ("empty list",           []),
    ]

    results = [run_test_case(name, vals) for name, vals in test_cases]

    total  = len(results)
    passed = sum(results)
    print("=" * 55)
    print(f"  Result: {passed}/{total} test cases passed"
          + ("  ✓ All good!" if passed == total else "  ✗ Check failures above."))
    print("=" * 55)
