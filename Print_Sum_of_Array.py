def array_sum(Arr):
    Total=0
    for num in Arr:
        Total=Total+num

    return Total
Arr=[10,20,30,40,50]
print('Sum of an array is:',array_sum(Arr))