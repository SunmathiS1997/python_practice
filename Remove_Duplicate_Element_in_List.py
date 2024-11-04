
def remove_duplicates(my_list):
    unique_numbers=[]
    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers


my_list=[10,20,30,10,52,30]
remove_duplicate=remove_duplicates(my_list)
print("Removed the duplicate elements:",remove_duplicate)