myarray = [3, 12, 3, 21, 1, 17, 33]
min_val = myarray[0]
for i in myarray:
    if i < min_val:
        min_val = i
print('lowest number in array is : ', min_val)