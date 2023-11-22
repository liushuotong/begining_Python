from randomSet import randomSet
from SelectionSort import SelectionSort
# from BucketSort import BucketSort
from BullonSort import BullonSort
from MergeSort import MergeSort
# from QuickSort import QuickSort
import time
def main():
    """
    This function executes a series of sorting algorithms and compares their execution time.
    It first generates a random list of 10,000 elements using the randomSet() function.
    It then measures the time it takes to execute the SelectionSort() function and prints the result.
    Next, it measures the time it takes to execute the BucketSort() function and prints the result.
    After that, it measures the time it takes to execute the BullonSort() function and prints the result.
    Finally, it measures the time it takes to execute the MergeSort() function and prints the result.
    Each sorting algorithm is executed on the same random list, allowing for fair comparison of their execution times.
    """

    list = randomSet(10000)
    start = time.time()
    SelectionSort(list)
    end = time.time()
    print(end - start)
# Compare this snippet from SortCompare.py/QuickSort.py:
    '''
    list = randomSet(10000)
    start = time.time()
    BucketSort(list)
    end = time.time()
    print(end - start)
    '''
# Compare this snippet from SortCompare.py/BullonSort.py:
    list = randomSet(10000)
    start = time.time()
    BullonSort(list)
    end = time.time()
    print(end - start)
# Compare this snippet from SortCompare.py/MergeSort.py:
    list = randomSet(10000)
    start = time.time()
    MergeSort(list)
    end = time.time()
    print(end - start)
# Compare this snippet from SortCompare.py/QuickSort.py:
    '''
    list = randomSet(10000)
    start = time.time()
    QuickSort(list)
    end = time.time()
    print(end - start)
# Compare this snippet from SortCompare.py/BullonSort.py:
    '''
    input("Press Enter to continue...")
if __name__ == '__main__':
    main()