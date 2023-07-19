from itertools import product
answer=0
glasn ='ОЕ'
soglasn = 'МРГН'
for dlina in range(3,7):
    for j in product('МОРГЕН',repeat=dlina):
        word=''.join(j)
        if (word[0] in glasn) and (word[-2] in soglasn):
            answer+=1
print(answer)
