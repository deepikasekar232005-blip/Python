num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num ,"is Not Prime")
            # directly stop program with return/exit
            exit()
    print(num," is Prime")
