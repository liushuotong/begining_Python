def MergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        # 分割，确定中间位置
        left = list[:mid]
        right = list[mid:]# 分割
        MergeSort(left)
        MergeSort(right)# 递归
        i = j = k = 0
        # 初始化
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
                # 左边的数小于右边的数，将左边的数放入list
            else:
                list[k] = right[j]
                j += 1
                # 右边的数小于左边的数，将右边的数放入list
            k += 1
            # 将剩余的数放入list
        while i < len(left):# 左边或者右边有剩余的数
            list[k] = left[i]
            i += 1
            k += 1
            # 将剩余的数放入list
        while j < len(right):# 左边或者右边有剩余的数
            list[k] = right[j]
            j += 1
            k += 1
            # 将剩余的数放入list
    return list