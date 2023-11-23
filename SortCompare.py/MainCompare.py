from randomSet import randomSet
from SelectionSort import SelectionSort
from BucketSort import BucketSort
from BullonSort import BullonSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from SortAndPrint import SortAndPrint
import time
def main():
    """
	Compare the given function.

	Args:
	    fuction: The function to be compared.

	Returns:
	    None
	"""
    def compareFuntion(fuction):
        """
        Compare the given function.

        Args:
            fuction: The function to be compared.

        Returns:
            None
        """
        print(fuction.__name__ + "Start")
        # Print the name of the given function followed by "Start"
        SortAndPrint(fuction)
        # Call SortAndPrint with the given function as an argument
        input("Press Enter to continue...")
        # Prompt the user to press Enter to continue
        '''
        This code defines a function called compareFunction that takes a function as an argument.
        It prints the name of the given function followed by "Start",
        then calls a function called SortAndPrint with the given function as an argument.
        Finally, it prompts the user to press Enter to continue.
        '''
# Compare this snippet from SortCompare.py/SelectionSort.py:
    compareFuntion(SelectionSort)
# Compare this snippet from SortCompare.py/BucketSort.py:
    compareFuntion(BucketSort)
# Compare this snippet from SortCompare.py/BullonSort.py:
    compareFuntion(BullonSort)
# Compare this snippet from SortCompare.py/MergeSort.py:
    compareFuntion(MergeSort)
# Compare this snippet from SortCompare.py/QuickSort.py:
    compareFuntion(QuickSort)
# Compare finished
    print("Sort END!")
    input("Press Enter to continue...")
    '''
    This code defines a main function that compares different sorting functions.
    It prompts the user to press Enter to continue,
    and then compares each sorting function by calling the compareFunction function and passing in the sorting function as an argument.
    After comparing all the sorting functions, it prints "Sort END!" and prompts the user to press Enter to continue again.
    '''
if __name__ == '__main__':
    main()