# Task 2 User Guide

## Environment
- Python 3.10+ recommended
- No third-party package is required

## Run Commands
From repository root:

```bash
python3 task2/heap_example.py
python3 task2/heapsort_example.py
```

## What Each Script Shows

### 1) `heap_example.py`
Demonstrates Max Heap ADT operations:
- Build heap from a list
- Check max value with `peek()`
- Insert new value with `insert()`
- Remove max repeatedly with `extract_max()`
- Boundary behavior on empty heap

Expected output pattern:
- Shows heap content after each key operation
- Final extraction result should be in descending order
- Empty heap calls should return `None`

### 2) `heapsort_example.py`
Demonstrates Heap Sort with multiple input categories:
- random numbers
- duplicate values
- already sorted list
- reverse sorted list
- single-element list
- empty list

Expected output pattern:
- For each case: Input, Output, Expected, PASS/FAIL
- All cases should show `PASS`

## Common Issues
- `python: command not found`: use `python3` instead
- Wrong folder: make sure you run commands at repository root
- Modified code behavior: compare with README complexity and expected flow

## How to Use Results in Report
- Screenshot one or two representative PASS cases
- Explain why each case is useful (edge case / normal case)
- Add complexity analysis from `README.md`
