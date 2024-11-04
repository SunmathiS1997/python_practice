s='Programming'
l=[]
l1=[]
for letter in s:
    if letter not in l:
        l.append(letter)
    else:
        l1.append(letter)

print(''.join(l1))