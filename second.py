import math
import re

M = [[1,2,3],[4,5,6],[7,8,9]]
print(M[1][2])
L = [row[2] for row in M]
print(L)
P = [M[i][0] for i in [0,1,2]]
print(P)
base = 'base'
doubles = [c * 2 for c in ['s', 'a']]
print(doubles)

print(range(10))
print(list(range(10)))
print[[x ** 2, x ** 3] for x in range(4)]


print{i: sum(M[i]) for i in range (3)}