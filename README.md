
```markdown
# Django Machine Test – Flight Routes System ✈️

This project is a Django-based application to manage and analyse airport routes using a **binary tree structure**.

Each airport is treated as a node, and routes between airports are represented using parent–child relationships.

---

## Basic Idea

- Each **Airport** is a node in a binary tree  
- Each airport can have **maximum two children**:
  - Left child
  - Right child
- **Duration** represents the **distance from parent airport to current airport**
- Root airport has **no parent**, so its duration should be saved as **0**

---

## Important Note (Please Read)

👉 **While adding the root airport, always set `duration = 0`**

Reason:
- Duration is the distance between **two airports**
- Root has no parent, so distance is considered `0`
- This keeps the logic consistent for calculations

---

## Features Implemented

### 1. Add Airport
- Add airports one by one
- Select parent airport (optional)
- Select position (Left / Right) if parent is selected
- Tree structure updates automatically

---

### 2. Find Nth Left / Right Airport
- Select a starting airport
- Choose direction (Left or Right)
- Enter N value
- System finds the Nth node in that direction

---

### 3. Find Longest Route
- Finds the airport which has the **maximum distance from its parent**
- This represents the **longest route segment**

---

### 4. Find Shortest Route Between Two Airports
- Select two airports
- System finds the **path between them**
- From that path, it returns the **shortest distance segment**
- Root node is ignored since it has no incoming route

---

## Tree Visualisation

- The current airport tree is displayed on **every page**
- Left side shows the tree
- Right side shows the active page (form / result)
- Helps to clearly understand structure while testing

---

## Project Structure (Important Files)

```

airplane/
├── models.py        # Airport model (tree structure)
├── forms.py         # Forms for input and validation
├── views.py         # Core logic and routing
├── templates/
│   └── airplane/
│       ├── base.html
│       ├── tree.html
│       ├── add_airport.html
│       ├── nth_node.html
│       ├── longest_node.html
│       └── shortest_between.html

````

---

## Tech Stack Used

- Python
- Django
- Django Templates
- SQLite (default DB)

---

## Assumptions Made

- Binary tree (only one left and one right child allowed)
- Duration is stored on **child node** as distance from parent
- Root node duration is always `0`
- No frontend frameworks used (plain HTML + CSS)

---

## How to Run

```bash
python manage.py migrate
python manage.py runserver
````

Then open:

```
http://127.0.0.1:8000/add/
```

---

## Final Note

This project focuses more on **logic and correctness** than UI.
Code is intentionally kept simple and readable.

Thanks 🙂

```
