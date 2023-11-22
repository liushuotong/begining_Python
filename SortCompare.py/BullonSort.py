def BullonSort(list):
    for i in range(0,len(list)):
        for j in range(i-2,len(list)-1):
            if list[j] >= list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list