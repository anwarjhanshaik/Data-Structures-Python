# Data Structures & Algorithms Library in Python

A high-performance, production-ready, object-oriented library of fundamental data structures implemented from scratch in Python. Each structure features comprehensive boundary-case management, dynamic iterator support, and optimal asymptotic time complexities.

---

## 📁 Repository Structure

This repository uses a flat file structure. All data structure implementations live directly in the root directory:

- `sll.py`   - Singly Linked List with loop repair mechanics.
- `cdll.py`  - Circular Doubly Linked List with bidirectional ring mechanics.
- `cll.py`   - Circular Linked List optimized via a single tail pointer.
- `dll.py`   - Doubly Linked List with tail pointer and external iterator class.
- `stack.py` - LIFO Stack array wrapper.
- `README.md` - Library documentation.

---

## 🛠️ Data Structures Deep-Dive & Time Complexities

### 1. Singly Linked List (`sll.py`)
A forward-linked structural chain managing a single pointer architecture per node.
* **Special Features**: Implements **Floyd’s Cycle-Finding Algorithm** inside `check_and_fix_cycle()`. If a loop exists, it self-heals by severing the invalid link, resetting `fast.next = None`, and dynamically recalculating valid list metrics.
* **Magic Overrides**: Custom `__len__`, a generator-based `__iter__`, and a `__str__` map that prints list shapes (`1 --> 2 --> None`).

### 2. Circular Doubly Linked List (`cdll.py`)
The ultimate configuration linking bidirectional pointers into a closed ring layout.
* **Special Features**: Features an internal state-tracking iterator (`CDLLIterator`) using a safe boolean pass guard (`first_pass`) to loop exactly once through the ring without trapping runtime resources. Includes clean center-node extraction and removal via `find_middle()` and `delete_middle()`.

### 3. Circular Linked List (`cll.py`)
A highly memory-efficient looping ring structured by **retaining only a single `tail` reference pointer**. The head node is elegantly derived as `tail.next`.
* **Special Features**: Leverages zero-null loop traversals using custom pointer rotations. Functions like `insert_at_last` optimize resources by calling `insert_at_start` and shifting the tail one step forward.

### 4. Doubly Linked List (`dll.py`)
A bidirectional linked structure holding explicit `head` and `tail` tracking pins.
* **Special Features**: Employs a dedicated external iterator class (`DllIterator`) for standard pythonic traversal loops. Features an advanced single-pass `deleteEntireInstanceOfElement()` data sweep.
* **Complexities**: Append (`insert_at_last`) runs in **O(1)** due to persistent tail allocation.

### 5. Stack (`stack.py`)
A Last-In, First-Out (LIFO) linear data structure wrapped around a native Python list.
* **Complexities**: `push`, `pop`, `peek`, `is_empty`, and `size` run in **O(1)** time.
* **Safety**: Safely throws a clear `IndexError("Stack is empty")` when attempting illegal actions on an empty stack state.

---

## 📊 Complete Operations Reference Map

| Operation / Method | SLL | CDLL | CLL | DLL | Stack |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Insert at Start** | O(1) | O(1) | O(1) | O(1) | - |
| **Insert at Last** | O(n) | O(1) | O(1) | O(1) | O(1) (`push`) |
| **Insert at Index** | O(n) | O(n) | O(n) | O(n) | - |
| **Remove Start** | O(1) | O(1) | O(1) | O(1) | - |
| **Remove Last** | O(n) | O(1) | O(n) | O(1) | O(1) (`pop`) |
| **Remove Index / Item**| O(n) | O(n) | O(n) | O(n) | - |
| **Find Middle Node** | O(n) | O(n) | O(n) | O(n) | - |
| **Reverse List Layout**| O(n) | O(n) | O(n) | O(n) | - |
| **Cycle Check / Fix** | O(n) | Built-in | Built-in | O(n) | - |

---
