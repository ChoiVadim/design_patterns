"""
Strategy Pattern - Sorting Algorithms Example
Real-world usage: Data analysis tools, database optimizers, spreadsheet apps
"""

from abc import ABC, abstractmethod
from typing import List
import time


class SortStrategy(ABC):
    """Strategy interface for sorting algorithms"""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """Sort the data and return sorted list"""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Return algorithm name"""
        pass


class QuickSortStrategy(SortStrategy):
    """QuickSort algorithm - efficient for random data"""
    
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)
    
    def get_name(self) -> str:
        return "QuickSort"


class MergeSortStrategy(SortStrategy):
    """MergeSort algorithm - stable, good for linked lists"""
    
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def get_name(self) -> str:
        return "MergeSort"


class BubbleSortStrategy(SortStrategy):
    """BubbleSort algorithm - simple, good for nearly-sorted data"""
    
    def sort(self, data: List[int]) -> List[int]:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
    def get_name(self) -> str:
        return "BubbleSort"


class DataSorter:
    """Context class that uses sorting strategies"""
    
    def __init__(self, strategy: SortStrategy = None):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        """Change sorting strategy at runtime"""
        self._strategy = strategy
    
    def sort_data(self, data: List[int]) -> List[int]:
        """Sort data using current strategy"""
        if not self._strategy:
            raise ValueError("No sorting strategy set")
        return self._strategy.sort(data)
    
    def get_strategy_name(self) -> str:
        """Get current strategy name"""
        return self._strategy.get_name() if self._strategy else "None"


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Strategy Pattern - Sorting Algorithms Example")
    print("=" * 60)
    print()
    
    # Test data
    test_data = [64, 34, 25, 12, 22, 11, 90, 5, 77, 50]
    print(f"Original data: {test_data}")
    print()
    
    sorter = DataSorter()
    
    # Test QuickSort
    print("1. Using QuickSort Strategy:")
    print("-" * 60)
    sorter.set_strategy(QuickSortStrategy())
    start = time.time()
    sorted_data = sorter.sort_data(test_data.copy())
    elapsed = (time.time() - start) * 1000
    print(f"Algorithm: {sorter.get_strategy_name()}")
    print(f"Sorted: {sorted_data}")
    print(f"Time: {elapsed:.4f} ms")
    print()
    
    # Test MergeSort
    print("2. Using MergeSort Strategy:")
    print("-" * 60)
    sorter.set_strategy(MergeSortStrategy())
    start = time.time()
    sorted_data = sorter.sort_data(test_data.copy())
    elapsed = (time.time() - start) * 1000
    print(f"Algorithm: {sorter.get_strategy_name()}")
    print(f"Sorted: {sorted_data}")
    print(f"Time: {elapsed:.4f} ms")
    print()
    
    # Test BubbleSort
    print("3. Using BubbleSort Strategy:")
    print("-" * 60)
    sorter.set_strategy(BubbleSortStrategy())
    start = time.time()
    sorted_data = sorter.sort_data(test_data.copy())
    elapsed = (time.time() - start) * 1000
    print(f"Algorithm: {sorter.get_strategy_name()}")
    print(f"Sorted: {sorted_data}")
    print(f"Time: {elapsed:.4f} ms")
    print()
    
    print("=" * 60)
    print("Key Benefit: Can switch algorithms based on data characteristics")
    print("without modifying the DataSorter class!")
    print("=" * 60)

