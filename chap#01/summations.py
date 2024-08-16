from sympy import *

i, n = symbols('i n')

# iterate each element i from 1 to n
# then multiply and sum
summation = Sum(2*i, (i, 1, n))

# specify n as 5
# iterating the numbers from 1 through 5

up_to_5 = summation.subs(n, 5)
print(up_to_5.doit()) #30

# 1.10
# summation = sum(2*i for i in range(1, 6))
# print(summation)

# 1.11 Summations of elements in python
# x = [3, 5, 7, 9]
# n = len(x)

# summation_1 = sum(7*x[i] for i in range(0, n))
# print(summation_1)