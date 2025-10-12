# you are given a list of interger from 1 to n, but some number are missing. return the missing number as a sorted set.

N = 6
numbers = [1,2,3,5,6,6,7]
result = tuple(sorted({x for x in numbers if numbers.count(x) > 1 or x > N}))
print(result)