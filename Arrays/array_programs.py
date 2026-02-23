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

# def largest_index(arr):
#     first = second = third = float('-inf')

#     for i in set(arr):
#         if i > first:
#             third = second
#             second = first
#             first = i
#         elif i > second:
#             third = second
#             second = i
#         elif i > third:
#             third = i
#     return third


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
        # The heap will maintain the k largest unique elements seen so far.
        #  If the heap exceeds size k, 
        # the smallest element (the root of the min-heap) is removed, 
        # ensuring that only the k largest unique elements remain in the heap.

        # if len(heap) > k:
#             heapq.heappop(heap)
#     return heap[0]

# k = int(input('enter kth index: '))

# user_input = input('enter array elements: ')

# arr = [int(x) for x in user_input.split()]

# result = kth_element(arr, k)
# print(result)



# kth smallest element in an array:
# import heapq

# def kth_smallest(arr, k):
    # heap = arr[:]          # copy array
    # heapq.heapify(heap)   # convert into min-heap

#     for _ in range(k - 1):
#         heapq.heappop(heap)
#         """heapq.heappop(heap)
# two things happen automatically:

# The smallest element is removed

# The heap is rearranged internally
#  so that the next smallest element moves to heap[0]"""

#     return heap[0]


# k = int(input("Enter k: "))
# user_input = input("Enter array elements: ")

# arr = [int(x) for x in user_input.split()]

# result = kth_smallest(arr, k)
# print(f"{k}th smallest element:", result)




#finding pair sum in unsorted array:
# def pair_sum_unsorted(arr, target):
#     seen = set()

#     for num in arr:
#         complement = target - num

#         if complement in seen:
#             return True

#         seen.add(num)

#     return False


# arr = [4,7,1,9,3]
# target = 10

# print(pair_sum_unsorted(arr, target))



#finding pair sum in sorted array:
# def finding_pair(arr, target):
#     left , right = 0, len(arr)-1

#     while left < right:
#         current_sum = arr[left]+ arr[right]
        
#         if current_sum == target:
#             return {arr[left], arr[right]}
#         elif current_sum < target:
#             left +=1
#         else:
#             right -= 1
#     return "no pair found"
# arr = [1,2,3,4,5,6,7,8,9]
# target = 6
# print(finding_pair(arr, target))



#removing duplicates from sorted array:
def remove_duplicates(arr):
    if not arr: # check if the array is empty 
        return 0# if array is empty return 0 as there are no elements to process

    i = 0  # slow pointer
    # i marks end of Unique Zone.
     # j scans entire array.
    for j in range(1, len(arr)):  # fast pointer
        # logic here is : if the current element at j
        #  is different from the last unique element at i,
         # we have found a new unique element.
         #  We move the slow pointer i forward and copy
        if arr[j] != arr[i]:

            i += 1
            arr[i] = arr[j]

    return i + 1 # cover all the element in unique zone  


# arr = [1,1,2,2,3,4,4,5]
arr = [21, 3, 54]
new_length = remove_duplicates(arr)

# print("New length:", new_length)
print("previous array:", arr)
print("Modified array:", arr[:new_length])
