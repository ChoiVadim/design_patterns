# Strategy Pattern - Example 2: Sorting Algorithms

## Problem Description

A data visualization application needs to sort large datasets using different algorithms based on the data characteristics. QuickSort works well for random data, MergeSort for linked lists, and BubbleSort for nearly-sorted data. The Strategy pattern allows switching algorithms without changing the sorting interface.

**Real-world usage**: Used in data analysis tools (Pandas, NumPy), database query optimizers, spreadsheet applications (Excel, Google Sheets), and sorting libraries.

## Class Diagram

```
                    ┌─────────────────────┐
                    │  SortStrategy       │
                    │  (Interface)        │
                    ├─────────────────────┤
                    │ + sort(data)        │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌────▼──────┐ ┌────▼──────────┐
    │ QuickSortStrategy│ │MergeSort  │ │BubbleSort     │
    │                  │ │Strategy   │ │Strategy       │
    ├──────────────────┤ ├───────────┤ ├───────────────┤
    │ + sort(data)     │ │ + sort()  │ │ + sort()      │
    └──────────────────┘ └───────────┘ └───────────────┘
                │              │              │
                └──────────────┼──────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  DataSorter         │
                    ├─────────────────────┤
                    │ - strategy          │
                    │ + setStrategy()     │
                    │ + sortData()        │
                    └─────────────────────┘
```

