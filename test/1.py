n=int(input())
s=list(map(int,input().split()))
s1=list(set(s))
a=s1[0:5]
print(a)
for i in s1:
    print(i)
    if s.count(i)>1:
        a.remove(i)
print(a)