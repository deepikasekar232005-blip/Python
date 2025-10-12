# you are given two integer lists list1 and list2. your task is to return a sorted lis containing all the numbers that appear in both lists.

set1 = (1,2,3,4,5)
set2 = (4,5,6,7,8)
set1 = set(set1)
set2 = set(set2)
common = set1 & set2
result = tuple(sorted(common))
print(result)