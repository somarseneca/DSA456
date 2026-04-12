# Part A – SortedTable Analysis

Let n be the number of records in the table.

## insert(self, key, value)
Time Complexity: O(n²)

- Calls search() → O(n)
- Resizing → O(n)
- Bubble sort → O(n²)

Overall: O(n²)

---

## modify(self, key, value)
Time Complexity: O(n)

- Linear search through table

---

## remove(self, key)
Time Complexity: O(n)

- Find element → O(n)
- Shift elements → O(n)

---

## search(self, key)
Time Complexity: O(n)

- Linear search

---

## capacity(self)
Time Complexity: O(1)

- Returns stored variable

---

## __len__(self)
Time Complexity: O(n)

- Loops through entire table counting elements

---

# Inefficiencies

- Uses bubble sort → O(n²)
- Uses linear search despite sorted structure
- __len__ is O(n), used repeatedly
- Inserts at end then sorts instead of placing correctly

---

# Improvements

- Use binary search → O(log n)
- Insert directly in sorted position → O(n)
- Maintain size variable → O(1) length
- Avoid repeated len() calls

---

# Summary

The SortedTable implementation is inefficient due to repeated linear searches and the use of bubble sort after each insertion. This results in O(n²) performance for insert operations. Improvements such as binary search, direct insertion, and maintaining a size variable would significantly improve efficiency.