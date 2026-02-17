# myarray = [3, 12, 3, 21, 1, 17, 33]
# min_val = myarray[0]
# for i in myarray:
#     if i < min_val:
#         min_val = i
# print('lowest number in array is : ', min_val)

# traversing an array:

# array = [2,4,25,36,24,255,6]
# for i  in range(len(array)):
#     print(array[i])


# max val :
# array1 = 
# max_val = array1[0]
# for i in array1:
#      if i > max_val:
#           max_val = i
# print(f' greatest element in array1 is: {max_val}')


# min and max in one:

# array2 = [2,4,25,36,24,255,233, 2023]
# min_val = array2[0]
# max_val = array2[0]

# for i in array2:
#     if i < min_val:
#         min_val = i
#     if i > max_val:
#         max_val = i
# print(f"greatest number : {max_val}")
# print(f'Minimum value is : {min_val}')


#finding second largest element in an array:

def largest_index(arr):
    first = second = third = float('-inf')

    for i in set(arr):
        if i > first:
            third = second
            second = first
            first = i
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i
    return third
# arr = [2,4,25,36,24,255,233, 2023]
# print(largest_index(arr))

user_inp