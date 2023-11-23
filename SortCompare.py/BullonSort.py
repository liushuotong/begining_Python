def BullonSort(list):
    """
    Sorts a given list in ascending order using the Bullon sort algorithm.

    Parameters:
        list (list): The list to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # 定义一个布尔变量，用于记录是否发生了交换
    flag = True
    # 定义一个变量，用于记录已经有序的元素个数
    n = 0
    # 当发生了交换或者还有未排序的元素时，继续循环
    while flag or n < len(list) - 1:
        # 初始化flag为False
        flag = False
        # 遍历列表，从第一个元素到倒数第n+1个元素
        for i in range(len(list) - n - 1):
            # 如果第i个元素大于第i+1个元素
            if list[i] > list[i+1]:
                # 交换两者的位置
                list[i], list[i+1] = list[i+1], list[i]
                # 将flag设为True，表示发生了交换
                flag = True
        # 将n加一，表示有一个元素已经有序
        n += 1
    # 返回排序后的列表
    return list