SearchingData = [1 , 2 , 5 , 8, 9 , 10 , 100, 10]  

KeyVal = 10
FoundIndex = -1
for i in range(0, len(SearchingData)):
    if SearchingData[i] == KeyVal:
        FoundIndex = i
        break

print(FoundIndex)
