from numpy import append
import time

def Merge(a,start,mid,end):
    """
    Merge function to merge two sorted subarrays of array a.
    
    Args:
        a (list): The main array containing the subarrays to be merged.
        start (int): The starting index of the first subarray.
        mid (int): The ending index of the first subarray.
        end (int): The ending index of the second subarray.
    
    Returns:
        None: The function modifies the original array in place.
    """
    tmp = []
    l = start
    r  = mid + 1
    while l <= mid and r <= end:
        if a[l] <= a[r]:
            tmp.append(a[l])
            l += 1
        else:
            tmp.append(a[r])
            r += 1
    # 将剩余的元素加入到tmp
    tmp = append(tmp,a[l:mid+1])
    tmp = append(tmp,a[r:end+1])
    # 将tmp拷贝回原数组
    a[start:end+1] = tmp

def MergeSort(a,start,end):
    """
    Sorts a given list `a` using the Merge Sort algorithm.

    Parameters:
        a (list): The list to be sorted.
        start (int): The starting index of the sublist to be sorted.
        end (int): The ending index of the sublist to be sorted.

    Returns:
        None
    """
    if start >= end:
        return
    # 分割
    mid = (start + end) // 2
    # 递归
    MergeSort(a,start,mid)
    MergeSort(a,mid+1,end)
    # 合并
    Merge(a,start,mid,end)


a_1 = [8,5,6,4,3,7,10,2,9,1]
a_2 = [8,5,6,4,3,7,10,2,9,1]

def BullonSort(a):
    """
    Sorts a list of integers using the Bubble Sort algorithm.

    Parameters:
        a (list[int]): The list of integers to be sorted.

    Returns:
        None
    """
    for i in range (1,len(a)):
        for j in range (0,len(a)-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

def main():
    """
    Executes the main function.

    This function measures the time taken to execute MergeSort on the list `a_1` and prints the sorted list and the time taken.
    It then measures the time taken to execute BullonSort on the list `a_2` and prints the sorted list and the time taken.

    Parameters:
        None

    Returns:
        None
    """
    start = time.time()
    for i in range(1000):
        MergeSort(a_1,0,len(a_1)-1)
    end = time.time()
    
    print(a_1)
    print((end - start)/1000)

    start = time.time()
    for i in range(1000):
        BullonSort(a_2)
    end = time.time()

    print(a_2)
    print((end - start)/1000)

if __name__ == '__main__':
    main()