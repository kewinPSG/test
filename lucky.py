# # # from itertools import permutations
# # # lp= list(permutations(['+','-']))
# # # a=list(powerset("121"))
# # # print a
# # # m=lp[0]
# # # a=int(m[1]+a[0])
# # # b=int(m[0]+a[1])
# # # c=a+b 
# # # print a,b,c
# # # # while i in lp:
# # # # 	print lp[i]
# # import itertools
# # S=["abc"]
# # def findsubsets(S,m):
# #     return set(itertools.combinations(S, m))
# # print m
# from itertools import chain, combinations

# def powerset(iterable):
#   xs = list(iterable)
#   # note we return an iterator rather than a list
#   return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )
# a=list(powerset("++"))
# b=list(powerset("121"))
# del a[0]
# del b[0]
# c=a+b
from itertools import product
# for roll in product(c, repeat = 2):
# 	print(roll)
for x in product('1+2-1', repeat=5):
    w = ''.join(x)
    print w
    if w.lower() == 'crack': break
