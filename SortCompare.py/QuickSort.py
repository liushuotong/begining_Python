def QuickSort(list):
    # 定义一个辅助函数，用于划分列表
    def partition(list, low, high):
        # 选择最后一个元素作为基准
        pivot = list[high]
        # 初始化左右指针
        i = low - 1
        j = low
        # 遍历列表，将小于基准的元素放到左边，大于基准的元素放到右边
        while j < high:
            if list[j] < pivot:
                # 交换list[i]和list[j]
                i += 1
                list[i], list[j] = list[j], list[i]
            j += 1
        # 交换list[i+1]和list[high]，将基准放到正确的位置
        list[i+1], list[high] = list[high], list[i+1]
        # 返回基准的索引
        return i + 1
    # 定义一个辅助函数，用于递归排序
    def sort(list, low, high):
        # 如果列表有至少两个元素
        if low < high:
            # 划分列表，得到基准的索引
            pivot_index = partition(list, low, high)
            # 对左边的子列表进行快速排序
            sort(list, low, pivot_index - 1)
            # 对右边的子列表进行快速排序
            sort(list, pivot_index + 1, high)
    # 调用辅助函数，对整个列表进行快速排序
    sort(list, 0, len(list) - 1)
    # 返回排序后的列表
    return list