S=input('Enter some string to reverse:')
l=S.split()
l1=[]
for word in l:
    l1.append(word[::-1])
    Output=' '.join(l1)
print(Output)