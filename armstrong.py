num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3   # cube of digit (works for 3-digit Armstrong numbers)
    temp //= 10

if num == sum:
    print("Yes")
    print(num, "is an Armstrong number.")
else:
    print("No")
    print(num, "is not an Armstrong number.")