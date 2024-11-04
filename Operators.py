def Add(a):
    Add=a+b
    return Add

def Sub(a,b):
    Sub=a-b
    return Sub

def Mul(a,b,c):
    Mul=a*b*c
    return Mul
def main():
    a = int(input("Enter the first value:"))
    b = int(input("Enter the second value:"))
    c = int(input("Enter the third value:"))
    Answer = Add(a, b)
    Answer1 = Sub(a, b)
    Answer2 = Mul(a, b, c)
    print("the sum is:", Answer)
    print("the sub is:", Answer1)
    print("the Mul is:", Answer2)

if __name__ == "__main__":
   main()

