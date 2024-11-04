# print fruit name that don't have a in it

List=["apple", "banana", "Kiwi"]
for Fruits in List:
    if len(Fruits)==6:
        spl=Fruits[:2]
        spl1=Fruits[2:4]
        spl2=Fruits[4:]
        print(spl,spl1,spl2)
    else:
        pass