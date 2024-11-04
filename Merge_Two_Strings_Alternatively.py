S1='Sana'
S2='Jothi'
i=0
j=0
Output=' '
while i<len(S1) or j<len(S2):
    if i<len(S1):
        Output=Output+S1[i]
    i=i+1
    if j<len(S2):
        Output=Output+S2[j]
    j=j+1
print(Output)
