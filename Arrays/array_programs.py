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


# user_input = input('enter list of arrays: ')
# user_input = user_input.replace(',', ' ')
# arr = list(map(int, user_input.split()))
# arr = [int(x) for x in user_input.split()]
# result = largest_index(arr)
# # print('third  largest element is: ',result)
# if result == float('-inf'):
#     print("Third largest element does not exist")
# else:
#     print("Third largest element is:", result)
# arr = [2,4,25,36,24,255,233, 2023]
# print(largest_index(arr))


# import heapq

# def kth_largest(arr, k):
#     heap = []

#     for num in arr:
#         heapq.heappush(heap, num)

#         if len(heap) > k:
#             heapq.heappop(heap)

#     return heap[0]


# arr = [7,2,9,4,1,8]
# k = 3
# print(k,"rd largest:", kth_largest(arr, k))
#kth larges unique element in an array:

# import heapq

# def kth_element(arr, k):
#     heap = []
#     for num in set(arr):
#         heapq.heappush(heap, num)

#         if len(heap) > k:
#             heapq.heappop(heap)
#     return heap[0]

# k = int(input('enter kth index: '))

# user_input = input('enter array elements: ')

# arr = [int(x) for x in user_input.split()]

# result = kth_element(arr, k)
# print(result)

import heapq

def kth_smallest(arr, k):
    heap = arr[:]          # copy array
    heapq.heapify(heap)    # convert into min-heap

    for _ in range(k - 1):
        heapq.heappop(heap)
        """heapq.heappop(heap)
two things happen automatically:

The smallest element is removed

The heap is rearranged internally
 so that the next smallest element moves to heap[0]"""

    return heap[0]


k = int(input("Enter k: "))
user_input = input("Enter array elements: ")

arr = [int(x) for x in user_input.split()]

result = kth_smallest(arr, k)
print(f"{k}th smallest element:", result)
