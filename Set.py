n = int(input())
arr = list(map(int,input().split()))
set1 = set(arr)
m = int(input())
arr2 = list(map(int,input().split()))
set2 = set(arr2)
res = list((set1.difference(set2)).union(set2.difference(set1)))
ff = sorted(res)
for i in ff:
    print(i,end="\n")
