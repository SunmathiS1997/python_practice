def largest_arr(Arr):
    Largest=Arr[0]
    for num in Arr[1:]:
        if num>Largest:
            Largest=num

    return Largest

Arr=[10,2,3,50,6]
print('The largest num is:',largest_arr(Arr))