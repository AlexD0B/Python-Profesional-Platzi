# Union en sets

"""myset1 = {1,2,3}
myset2 = {3,4,5}
myset3 = myset1 | myset2
print(myset3)"""

# Intersección en sets

"""myset1 = {1,2,3}
myset2 = {3,4,5}
myset3 = myset1 & myset2
print(myset3)"""

# Diferencia en sets

"""myset1 = {1,2,3}
myset2 = {2,3,4,5}
myset3 = myset1 - myset2
myset4 = myset2 - myset1
print(myset3)
print(myset4)"""

# Diferencia simetrica en sets

myset1 = {1,2,3}
myset2 = {3,4,5}
myset3 = myset1 ^ myset2
print(myset3)

"""En caso de que quieran hacer operaciones con sets y hacerlo
 de forma más explícita pueden usar los métodos:
set1.union(set2)
set1.symmetric_difference(set2)
set1.difference(set2)
set1.intersection(set2)"""