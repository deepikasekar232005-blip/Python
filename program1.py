# store even number between 1 to 100 in one tuple keep only the values that is divisible by 3 or 5 

num = tuple(i for i in range(2, 101, 2)if i % 3 == 0 or i % 5 == 0)
print("The number is divisible by both  3 or 5")
print(num)