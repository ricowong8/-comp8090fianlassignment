"""
heap.py
-------
Max-Heap Data Structure — COMP8090SEF / COMP S209W Task 2
HKMU 2026 Spring Semester

A Max-Heap is a complete binary tree stored as a Python list where every
parent node is greater than or equal to both its children.  The maximum
element is always at index 0 (the root).

Array index relationships for a node at index i
────────────────────────────────────────────────
    Parent      : (i - 1) // 2
    Left child  :  2 * i + 1
    Right child :  2 * i + 2
"""


class Heap:
    """
    Max-Heap ADT implemented with a Python list as the backing store.

    The max-heap property guarantees:
        data[parent(i)] >= data[i]  for every node i > 0

    Supported operations
    ────────────────────
    insert(value)        O(log n)  – add a new element
    extract_max()        O(log n)  – remove and return the maximum
    peek()               O(1)      – read the maximum without removing
    build_heap(values)   O(n)      – replace contents with a new iterable
    is_empty()           O(1)      – check whether the heap is empty
    size() / len()       O(1)      – return the number of elements
    """

    def __init__(self, values=None):
        """
        Initialise the heap.

        Args:
            values (iterable, optional): Initial elements.  When provided,
                build_heap() is called so the structure is valid in O(n).
        """
        self.data = []
        if values:
            self.build_heap(values)

    # ── Private helpers ───────────────────────────────────────────────

    def _heapify_up(self, index: int) -> None:
        """
        Restore the max-heap property by moving the node at *index*
        upward until it is no longer greater than its parent.

        Called after insert() to fix a potential violation at the
        newly appended position.

        Time complexity : O(log n)  — traverses at most the tree height.
        Space complexity: O(1)      — iterative, no call-stack growth.

        Args:
            index: Position of the element to sift upward.
        """
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index] <= self.data[parent]:
                break                           # Heap property holds
            # Swap child with parent and continue upward
            self.data[index], self.data[parent] = (
                self.data[parent], self.data[index]
            )
            index = parent

    def _heapify_down(self, index: int) -> None:
        """
        Restore the max-heap property by moving the node at *index*
        downward until it is no longer smaller than both children.

        Called after extract_max() and build_heap() to fix potential
        violations from the root (or any interior node) downward.

        Time complexity : O(log n)  — traverses at most the tree height.
        Space complexity: O(1)      — iterative, no call-stack growth.

        Args:
            index: Position of the element to sift downward.
        """
        size = self.size()
        while True:
            largest = index
            left    = 2 * index + 1
            right   = 2 * index + 2

            # Find the largest value among node and its children
            if left < size and self.data[left] > self.data[largest]:
                largest = left
            if right < size and self.data[right] > self.data[largest]:
                largest = right

            if largest == index:
                break                           # Subtree is valid

            # Swap current node with the larger child and continue down
            self.data[index], self.data[largest] = (
                self.data[largest], self.data[index]
            )
            index = largest

    # ── Public interface ──────────────────────────────────────────────

    def insert(self, value) -> None:
        """
        Insert a new value into the Max-Heap.

        Steps:
            1. Append *value* to the end of the backing list.
            2. Sift it upward until the heap property is restored.

        Time complexity : O(log n)
        Space complexity: O(1)

        Args:
            value: The element to add (must support comparison operators).
        """
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def extract_max(self):
        """
        Remove and return the maximum element (root of the heap).

        Steps:
            1. Record the root value (the current maximum).
            2. Overwrite the root with the last element and pop the end.
            3. Sift the new root downward to restore the heap property.

        Time complexity : O(log n)
        Space complexity: O(1)

        Returns:
            The maximum value, or None if the heap is empty.
        """
        if self.is_empty():
            return None
        if self.size() == 1:
            return self.data.pop()

        max_val = self.data[0]          # Save the maximum (root)
        self.data[0] = self.data.pop()  # Move last element to root
        self._heapify_down(0)           # Restore heap property
        return max_val

    def peek(self):
        """
        Return the maximum element without removing it.

        Time complexity : O(1) — the maximum is always at index 0.
        Space complexity: O(1)

        Returns:
            The maximum value, or None if the heap is empty.
        """
        return self.data[0] if not self.is_empty() else None

    def build_heap(self, values) -> None:
        """
        Replace the heap contents with *values* using Floyd's bottom-up
        heapify method.

        Algorithm:
            1. Copy all elements into self.data (a flat list).
            2. Starting from the last non-leaf node (index n//2 - 1),
               call _heapify_down on each node moving toward the root.
               Each node is already above valid sub-heaps, so one
               sift-down call is sufficient per node.

        Time complexity : O(n)        — more efficient than n insertions
        Space complexity: O(1) extra  — operates on the list in-place

        Args:
            values (iterable): Elements to build the heap from.
        """
        self.data = list(values)
        # Last non-leaf is at index (n // 2) - 1; leaves need no action
        for i in range((self.size() // 2) - 1, -1, -1):
            self._heapify_down(i)

    def is_empty(self) -> bool:
        """
        Return True if the heap contains no elements, False otherwise.

        Time complexity: O(1)
        """
        return len(self.data) == 0

    def size(self) -> int:
        """Return the number of elements currently stored in the heap."""
        return len(self.data)

    def __len__(self) -> int:
        """Support the built-in len() function."""
        return len(self.data)

    def __repr__(self) -> str:
        """Return an unambiguous string representation of the heap."""
        return f"MaxHeap(size={self.size()}, root={self.peek()}, data={self.data})"


# ── Demo / manual test ────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Max-Heap ADT  —  Demonstration")
    print("=" * 55)

    # ── Build from list ───────────────────────────────────────────────
    print("\n[1] Build heap from [10, 4, 15, 20, 7]")
    heap = Heap([10, 4, 15, 20, 7])
    print("  Heap array :", heap.data)
    print("  peek()     :", heap.peek(),   "  (expected: 20)")
    print("  size()     :", heap.size(),   "  (expected: 5)")

    # ── Insert ────────────────────────────────────────────────────────
    print("\n[2] Insert 30")
    heap.insert(30)
    print("  Heap array :", heap.data)
    print("  peek()     :", heap.peek(),   "  (expected: 30)")
    print("  len()      :", len(heap),     "  (expected: 6)")

    # ── Extract all (descending order) ───────────────────────────────
    print("\n[3] Extract all — should be descending")
    extracted = []
    while not heap.is_empty():
        extracted.append(heap.extract_max())
    print("  Extracted  :", extracted,     "  (expected: [30,20,15,10,7,4])")

    # ── Edge cases ────────────────────────────────────────────────────
    print("\n[4] Edge cases on empty heap")
    empty = Heap()
    print("  peek()       :", empty.peek(),        "  (expected: None)")
    print("  extract_max():", empty.extract_max(), "  (expected: None)")
    print("  is_empty()   :", empty.is_empty(),    "  (expected: True)")

    print("\n[5] Single-element heap")
    single = Heap([42])
    print("  peek()       :", single.peek(),        "  (expected: 42)")
    print("  extract_max():", single.extract_max(), "  (expected: 42)")
    print("  is_empty()   :", single.is_empty(),    "  (expected: True)")
