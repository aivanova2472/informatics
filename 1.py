answer=0
for i in range(100000, 1000000):
    string=bin(i)[2:]
    if not ('111' in string) and not ('000' in string):
        answer+=1
print(answer)
