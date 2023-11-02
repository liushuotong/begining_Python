import random

def main():
    x = 1
    while(x == 1):
        random_number = random.randint(1, 10)
        print(random_number)
        x = int(input("EXIT[1_N\\0_Y]:"))
        while(x != 1 and x != 0):
            print("ERROR")
            x = int(input("EXIT[1_N\\0_Y]:"))
    input("Press any key to exit.")

if __name__ == '__main__':
    main()