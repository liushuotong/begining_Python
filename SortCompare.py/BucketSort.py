from SelectionSort import SelectionSort
def BucketSort(list):
    """
    Sorts a given list using the bucket sort algorithm.

    Args:
        list (List[int]): The list to be sorted.

    Returns:
        List[List[int]]: The sorted list.
    """
    # maxElement = max(list)
    # minElement = min(list)
    # 由于我们要比较不同算法的运行速度，调用函数会对结果造成影响
    # 所以这里取最大值和最小值的范围，我们要用擂台法找到最值
    maxElement = list[0] # 初始化最大值
    minElement = list[0] # 初始化最小值
    for i in range (1,len(list)): # 从第二个元素开始遍历
        if list[i] > maxElement: # 如果当前元素大于最大值
            maxElement = list[i] # 更新最大值
        if list[i] < minElement: # 如果当前元素小于最小值
            minElement = list[i] # 更新最小值
    # 计算最大值和最小值
    if maxElement == minElement: # 如果最大值和最小值相等
        return list # 直接返回列表，无需排序
    else:
        sumIndex = len(list)//100 + 1 # 计算桶的个数，向上取整
        listRange = round((maxElement - minElement)/sumIndex) # 计算桶的大小，使用整数
        listBucket = [[] for _ in range(sumIndex)]
        # 初始化桶
        for i in range (0,len(list)):
            listBucket[(list[i] - minElement)//listRange].append(list[i]) # 将元素放入正确的桶中，不使用round()函数
        for i in range(sumIndex):
            SelectionSort(listBucket[i]) # 对每个桶进行排序
        list = []
        for i in range(sumIndex):
            list.extend(listBucket[i]) # 将桶中的元素扁平化
    return list