
a = [0 , 2 , 4 , 6 , 8]
b = [1 , 3 , 5 , 7]

alen = len(a)
blen = len(b)

for i in range(0, alen):
    for j in range(0, blen -1):
        
        if b[j] < a[i]:
            x = b[j]
            b[j] = a[i]
            a[i] = x
        

for k in range(0, blen - 1):
    for l in range(k + 1, blen -1):
        if b[l] < b[k]:
            x = b[l]
            b[l] = b[k]
            b[k] = x

print(a)
print(b)
