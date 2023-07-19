from itertools import product

answer=0
k='КРИНЖ'
for j in product('ЖИКНР', repeat=5):
    word=''.join(j)
    answer+=1
    if word==k:
        print(answer,word)
