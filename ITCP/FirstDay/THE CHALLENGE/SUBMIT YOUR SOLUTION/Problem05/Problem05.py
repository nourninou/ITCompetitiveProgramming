import math

def GetDistance(px1,py1,px2,py2):
    return math.sqrt(((px1-px2)*(px1-px2)) + ((py1-py2)*(py1-py2)))


n = int(input())


x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())


x = [x1, x2]
y = [y1, y2]


SmallDistance = GetDistance(x1,y1,x2,y2)




for i in range(int(n) - 2):
    x.append(float(input()))
    y.append(float(input()))

for k in range(0, n):
    for l in range(k + 1, n):
        if GetDistance(x[k],y[k],x[l],y[l]) < SmallDistance:
            SmallDistance = GetDistance(x[k],y[k],x[l],y[l])

print(SmallDistance)

'''

a = [1 , 2 , 5 , 8]

a.append(55)
print(a)
'''


