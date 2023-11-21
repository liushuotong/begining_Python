from numpy import append

def chickenCout():
    """
    This function iterates through all possible combinations of the number of chickens and roosters to find a combination that satisfies the given conditions. It prints the numbers of chickens, roosters, and ducks that satisfy the condition (total of 100 animals and a total cost of 100 dollars).

    Parameters:
    None

    Returns:
    None
    """
    n = int(0)
    for x in range(1,21):
        #chickens
        for y in range(1,34):
            #roosters
            z = 100 - x - y
            #ducks
            if z > 0 and x*5 + y*3 + z*0.5 == 100:
                '''                
                5 dollars for each chicken, 
                3 dollars for each rooster, 
                and 0.5 dollars for each duck
                '''
                n= n + 1
                #count, start from 0, add 1
                print(n,">chickens: ",x,"    roosters: ",y,"    ducks: ",z)
                #chickens,roosters,ducks
            else:
                continue#continue the loop

def Finbonici():
    """
    This function prints the first 20 numbers of the Fibonacci sequence.
    Parameters:
    None
    Returns:
    None
    """
    Finbonici = []
    #create an empty list
    Finbonici.append(1)
    Finbonici.append(1)
    #add the first two numbers to the list
    for i in range(2,20):
        #start from 2,stop at 20,step by 1
        next_number = Finbonici[i-1] + Finbonici[i-2]
        #next number is the sum of the previous two numbers
        Finbonici.append(next_number)
        #add the next number to the list
    for Finbonici in Finbonici:
        '''
        在Python中，可以使用print函数的end参数来实现不换行。
        将end参数设置为空字符串''即可。例如：
        '''
        print(Finbonici,end = " ")


if __name__ == '__main__':
    chickenCout()
    Finbonici()
    """
    2023/11/16 21:35:38
    """
