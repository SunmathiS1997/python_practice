List = [56,20,10]
largest = List[0]
def main():
        global largest
        for Numbers in List:
            if Numbers > largest:
                largest=Numbers
print("The largest number is:", largest)

if __name__ == "__main__":
    main()
