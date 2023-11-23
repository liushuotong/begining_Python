from randomSet import randomSet
import time
def SortAndPrint(fuction):
    sumTime = 0
    for i in range(1,11):
        list = randomSet(10000)
        start = time.time()
        fuction(list)
        end = time.time()
        sumTime += end - start
        print(i,"finished:",end - start,"s")
    print("Average",sumTime/10,"s")