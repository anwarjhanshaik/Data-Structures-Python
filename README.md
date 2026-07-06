# Data Structures & Algorithms Library in Python

A high-performance, production-ready, object-oriented library of fundamental data structures implemented from scratch in Python. Each structure features comprehensive boundary-case management, dynamic iterator support, and optimal asymptotic time complexities.

---

## 📁 Repository Structure

```text
├── data_structures/         # Complete custom implementations
│   ├── stack.py             # LIFO Stack array wrapper
│   ├── sll.py               # Singly Linked List with loop repair
│   ├── dll.py               # Doubly Linked List with tail pointer & iterator
│   ├── cll.py               # Circular Linked List optimized via single tail pointer
│   └── cdll.py              # Circular Doubly Linked List with bidirectional ring mechanics
│
├── tests/                   # Automated unit testing suite
│   ├── test_stack.py
│   ├── test_sll.py
│   ├── test_dll.py
│   ├── test_cll.py
│   └── test_cdll.py
│
└── README.md                # Library documentation
```

---

## 🛠️ Data Structures Deep-Dive & Time Complexities

### 1. Stack (`stack.py`)
A Last-In, First-Out (LIFO) linear data structure wrapped around a native Python list.
* **Complexities**: `push`, `pop`, `peek`, `is_empty`, `size` -> **O(1)**
* **Safety**: Safely throws a clear `IndexError("Stack is empty")` when attempting illegal actions on a clean stack state.

### 2. Singly Linked List (`sll.py`)
A forward-linked structural chain managing a single pointer architecture per node.
* **Special Features**: Implements **Floyd’s Cycle-Finding Algorithm** inside `check_and_fix_cycle()`. If a loop exists, it self-heals by severing the invalid link, resetting `fast.next = None`, and dynamically recalculating valid list metrics.
* **Magic Overrides**: Custom `__len__`, a generator-based `__iter__`, and a `__str__` map that prints list shapes (`1 --> 2 --> None`).

### 3. Doubly Linked List (`dll.py`)
A bidirectional linked structure holding explicit `head` and `tail` tracking pins.
* **Special Features**: Employs a dedicated external iterator class (`DllIterator`) for standard pythonic traversal loops. Features an advanced single-pass `deleteEntireInstanceOfElement()` data sweep.
* **Complexities**: Append (`insert_at_last`) -> **O(1)** due to persistent tail allocation.

### 4. Circular Linked List (`cll.py`)
A highly memory-efficient looping ring structured by **retaining only a single `tail` reference pointer**. The head node is elegantly derived as `tail.next`.
* **Special Features**: Leverage zero-null loop traversals using custom pointer rotations. Functions like `insert_at_last` optimize resources by calling `insert_at_start` and shifting the tail one step forward.

### 5. Circular Doubly Linked List (`cdll.py`)
The ultimate configuration linking bidirectional pointers into a closed ring layout.
* **Special Features**: Features an internal state-tracking iterator (`CDLLIterator`) using a safe boolean pass guard (`first_pass`) to loop exactly once through the ring without trapping runtime resources. Includes clean center-node extraction and removal via `find_middle()` and `delete_middle()`.

---

## 📊 Complete Operations Reference Map

| Operation / Method | Stack | SLL | DLL | CLL | CDLL |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Insert at Start** | - | O(1) | O(1) | O(1) | O(1) |
| **Insert at Last** | O(1) (`push`) | O(n) | O(1) | O(1) | O(1) |
| **Insert at Index** | - | O(n) | O(n) | O(n) | O(n) |
| **Remove Start** | - | O(1) | O(1) | O(1) | O(1) |
| **Remove Last** | O(1) (`pop`) | O(n) | O(1) | O(n) | O(1) |
| **Remove Index / Item**| - | O(n) | O(n) | O(n) | O(n) |
| **Find Middle Node** | - | O(n) | O(n) | O(n) | O(n) |
| **Reverse List Layout**| - | O(n) | O(n) | O(n) | O(n) |
| **Cycle Check / Fix** | - | O(n) | O(n) | Built-in | Built-in |

---

## 🚀 Architectural Syntax Examples

### Working with your Singly Linked List (`sll.py`)
```python
from data_structures.sll import SLL

sll = SLL()
sll.insert_at_start(30)
sll.insert_at_start(10)
sll.insert_at_index(1, 20)  
sll.insert_at_last(20)

sll.delete_duplicates()     # Drops trailing 20 using an internal hash set
print(sll)                  # Output: 10 --> 20 --> 30 --> None
```

### Running your Circular Doubly Linked List (`cdll.py`)
```python
from data_structures.cdll import CDLL

cdll = CDLL()
cdll.insert_at_last("A")
cdll.insert_at_last("B")
cdll.insert_at_start("HeadElement")

print(cdll)                 # Output: HeadElement <--> A <--> B <--> (Head)
```

---

## 🧪 Running the Test Suites

All structures are verified via structural verification unit tests matching individual components. Run the entire verification framework via your system console terminal from the root path:

```bash
python -m unittest discover tests
```
