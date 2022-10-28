
# Найти наиб длину подстроки, где нет 'ZX'
s='XXXYYZXXXXZXYYYYYYYYXXZXX'
k=1
s1='XYYYYYYYYXXZ'
max=0
for i in range(1,len(s)):
    if (s[i]!='X' or s[i-1]!='Z'):
        k+=1
    else:
        if k>max:
            max=k
        print(k)
        k=1
    
print(max)
#print(len(s1))


with open('27-8a.txt') as f:
    n=int(f.readline())
    a=[]
    min=1000000000
    minSum=1000000000
    for i in range(5):
        a.append(int(f.readline()))
    for i in range(n-5):
        x=int(f.readline())
        if a[0]<min:
            min=a[0]
        if (min**2+x**2)<minSum:
            minSum=min**2+x**2
        a.pop(0)
        a.append(x)
print(minSum)


with open('27-8a.txt') as f:
    n=int(f.readline())
    a=[]
    minch=100000000
    minnech=100000000
    minSum=100000000
    for i in range(6):
        a.append(int(f.readline()))
    for i in range(n-6):
        x=int(f.readline())
        if a[0]%2==0 and a[0]<minch:
            minch=a[0]
        if a[0]%2!=0 and a[0]<minnech:
            minnech=a[0]
        if x%2==0 and x+minnech<minSum:
            minSum=x+minnech
        if x%2!=0 and x+minch<minSum:
            minSum=minch
        a.pop(0)
        a.append(x)
print(minSum)
    






































