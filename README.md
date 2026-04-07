# COMP8090SEF / COMP S209W — Course Project

> **Hong Kong Metropolitan University**
> Data Structures and Algorithms — 2026 Spring

---

## 📁 Repository Structure

```
comp8090-project/
├── task1/                        # Task 1 — Individual Programming Project
│   ├── app.py                    # Entry point: AppController, QApplication launch
│   ├── login.py                  # LoginDialog (PySide6 QDialog, max-attempt lock)
│   ├── models.py                 # Item (ABC), Product, Inventory — core data models
│   ├── inventory_service.py      # InventoryService, ServiceResult — business logic
│   └── gui.py                    # KpiCard (QFrame), InventoryApp (QMainWindow)
│
├── task2/                        # Task 2 — Self-Study Report
│   ├── heap_example.py           # Max-Heap ADT (insert, extract_max, build_heap …)
│   └── heapsort_example.py       # Heap Sort algorithm + 8 test cases
│
└── README.md
```

---

## ✅ Task 1 — Inventory Management System

### Description

A desktop **Inventory Management System** built with **Python** and **PySide6**.  
It demonstrates core Object-Oriented Programming (OOP) principles including
abstraction, inheritance, encapsulation, polymorphism, properties, dataclasses,
and Qt Signals/Slots.

### Features

- 🔐 **Role-based login** — Admin (full access) and Viewer (read-only); locks after 3 failed attempts
- 📦 **Product management** — Add, edit, remove products with real-time input validation
- 📊 **Dashboard** — Live KPI cards (total items, low-stock alerts, total value) + category pie chart
- 🔍 **Search & sort** — Filter by name/category; sort by any column
- 🎨 **GUI** — PySide6 QMainWindow with tab navigation, styled KPI cards, and Matplotlib charts

### OOP Concepts Used

| Concept | Location |
|---|---|
| Abstraction | `Item` (ABC) with `@abstractmethod get_info()` in `models.py` |
| Inheritance | `Product(Item)`, `InventoryApp(QMainWindow)`, `LoginDialog(QDialog)` |
| Encapsulation | `_quantity` private attr + `@property` setter with validation in `models.py` |
| Polymorphism | `__repr__` delegates to overridden `get_info()` dynamically |
| Dataclass | `@dataclass ServiceResult` in `inventory_service.py` |
| Composition | `AppController` holds `InventoryApp` + `LoginDialog` in `app.py` |
| Signals/Slots | Qt `Signal` for inter-component communication in `gui.py` / `login.py` |

### Prerequisites

```
Python 3.10+
PySide6
matplotlib
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ricowong8/-comp8090fianlassignment.git
cd comp8090fianlassignment/task1

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install PySide6 matplotlib
```

### Run

```bash
python app.py
```

### Login Credentials

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| Viewer | `viewer` | `viewer123` |

---

## ✅ Task 2 — Self-Study: Max-Heap & Heap Sort

### Description

A self-study implementation of the **Max-Heap** data structure and the **Heap Sort**
algorithm — topics not covered in the course curriculum.  
All sift operations are implemented **iteratively** to avoid Python recursion depth limits.

### Files

| File | Description |
|---|---|
| `heap_example.py` | `Heap` class with `insert`, `extract_max`, `peek`, `build_heap`, `__len__`, `__repr__` |
| `heapsort_example.py` | Iterative `heapify` + `heap_sort` + 8-case test suite |

### Complexity Summary

| Operation | Time | Space |
|---|---|---|
| `insert` / `extract_max` | O(log n) | O(1) |
| `build_heap` (Floyd's) | O(n) | O(1) |
| `heap_sort` (full) | O(n log n) | O(1) |

### Run

```bash
cd task2

# Run Max-Heap demo
python heap_example.py

# Run Heap Sort + test suite (8/8 expected PASS)
python heapsort_example.py
```

### Expected Output (heapsort_example.py)

```
=======================================================
  Heap Sort  —  Demonstration & Test Suite
=======================================================

  [PASS]  random numbers
  [PASS]  with duplicates
  [PASS]  negative numbers
  [PASS]  already sorted
  [PASS]  reverse sorted
  [PASS]  all identical
  [PASS]  single element
  [PASS]  empty list

=======================================================
  Result: 8/8 test cases passed  ✓ All good!
=======================================================
```

---

## 🎬 5-Minute Introduction Video

[Insert video link here]

---

## 👤 Author

| Field | Detail |
|---|---|
| Name | WONG CHEUK YU|
| Student ID | 14154269 |
| Programme | MSc in Computing (MCOMP) |
| Institution | Hong Kong Metropolitan University |

---

## 📚 References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Python Software Foundation. (2024). *heapq — Heap queue algorithm*. https://docs.python.org/3/library/heapq.html
3. Qt for Python / PySide6 Documentation. https://doc.qt.io/qtforpython/
4. GeeksforGeeks. (2024). *Heap Sort*. https://www.geeksforgeeks.org/heap-sort/
5. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.

---

*COMP8090SEF / COMP S209W — 2026 Spring Semester*
