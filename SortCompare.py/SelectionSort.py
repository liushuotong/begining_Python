def SelectionSort(list):
    """
    Sorts a list of elements using the Selection Sort algorithm.

    Parameters:
    - list (list): The list to be sorted.

    Returns:
    - list: The sorted list in ascending order.
    """
    for i in range(0,len(list)-1):
        # 从第一个元素到倒数第二个元素
        for j in range(i+1,len(list)):
            # 如果第i个元素大于第j个元素
            if list[i]>list[j]:
                # 交换两者的位置
                list[i],list[j]=list[j],list[i]
                # 将i加一，表示已经有一个元素有序
    return list
    # 返回排序后的列表