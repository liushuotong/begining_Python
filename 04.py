'''
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

'''
def test():
    """
    This function calculates the sum of all even numbers from 0 to 100.

    Parameters:
    - None

    Returns:
    - None
    """
    sum = 0
    for i in range(101):
        if i%2==0:
            sum += i
        else:
            continue
    print(sum)

def FlowerNums():
    """
    This function prints all the Flower Numbers between 100 and 999.
    There are numbers that satisfy the condition (a^3 + b^3 + c^3 = abc),
    where a, b, and c are the digits of the number.
    This function does not take any parameters and does not return any value.
    """
    for i in range(100, 1000):
        if (i//100)**3+(i//10%10)**3+(i%10)**3==i:
            print(i)
        else:
            continue

def YangHuiSanJiao():
    """
    Generates Yang Hui San Jiao triangle with the given number of rows.
    
    Parameters:
        None
        
    Returns:
        None
    """
    rows = 20#杨辉三角的行数
    triangle = []#存储杨辉三角
    for i in range(rows):
        row = []#存储每行的数据
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)#第一行和最后一行都是1
            else:
                # 上一行的左上角和右上角元素之和
                num = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(num)#其他元素就是左上角和右上角元素之和

                '''
append(num)是一个列表（List）对象的方法，用于在列表的末尾添加一个元素。在上面的代码示例中，row是一个列表对象，append(num)用于将变量num添加到row列表的末尾。

具体来说，append(num)将num作为一个新的元素添加到列表row的最后一个位置。这样就可以逐行构建杨辉三角的每一行，并将每一行作为一个列表添加到triangle列表中。

例如，在第一行中，我们将1添加到空的row列表中，然后在第二行中，我们将两个1添加到row列表中，以此类推。最后，triangle列表将包含杨辉三角的所有行。
                '''

        triangle.append(row)#将第i行的数据添加到杨辉三角中
    '''
    为啥定义row变量，
    然后将它添加到triangle列表中呢？
    因为我们需要在杨辉三角中存储每一行的数据，而每一行的数据是一个列表。
    便于在后面使用for循环遍历杨辉三角的每一行。
    '''
    for row in triangle:
        for num in row:#打印杨辉三角
            print(num, end=" ")
        print()#换行
        '''
        
        你提供的代码片段是一个嵌套循环，它遍历了triangle列表，该列表表示杨辉三角的每一行。

        对于triangle列表中的每一行，内部循环遍历该行中的数字。
        
        对于每个数字，print(num, end=" ")语句打印该行中的每个数字，它们之间用空格分隔。

        end=" ", 它的作用是在打印每个数字之后添加一个空格。

        在打印完一行的所有数字后，print()语句用于打印换行符，将光标移动到下一行。

        在这个过程对triangle列表中的每一行都重复执行，从而打印出完整的杨辉三角。

        '''

YangHuiSanJiao()
if __name__ == '__main__':
    test()
    FlowerNums()
    YangHuiSanJiao()