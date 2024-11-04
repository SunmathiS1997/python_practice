#Using slice operator
# S=input(str("Enter the string to reverse"))
# output=S[::-1]
# print("Reversed string is:", output)
#Using reversed() function
# S=input(str("Enter the string to reverse"))
# R=reversed(S)
# for ch in R:
#     print(ch)
#OR
# S=input(str("Enter the string to reverse"))
# R=reversed(S)
# Output=''.join(R)
# print(Output)
#Using while loop
S=input(str("Enter the string to reverse"))
i=len(S)-1
Output = ''
while i>=0:
    Output=Output+S[i]
    i=i-1
print(Output)
