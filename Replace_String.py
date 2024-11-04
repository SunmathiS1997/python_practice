# # Removes all the 'o' from the string
# S1='Hello World'
# New_String=S1.replace('o',' ')
# print(New_String)

S1='Hello World'
New_String=S1.translate(str.maketrans('o,W','i,s'))
print(New_String)

