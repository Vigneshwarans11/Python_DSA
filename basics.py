#Reverse a String
# s="hello"
# print(s[::-1])

# using for loop 
# s="hello"
# rev=""
# for ch in s:
#     rev=ch+rev
# print(rev)

# using functions
# def reverse_string(s):
#     rev=""
#     for ch in s:
#         rev=ch+rev
#     return rev
# s="hello"
# print(reverse_string(s))

# using while loop
# s="hello"
# rev=""
# n=len(s)-1
# while n>=0:
#     rev=rev+s[n]
#     n=n-1
# print(rev)

# Find the Largest Element in an Array
# numbers = [34, 67, 23, 89, 12, 55, 91, 44]
# number1=sorted(numbers)
# print(number1[-1])

# using while loop
# numbers = [34, 67, 23, 89, 12, 55, 91, 44]
# largest_num=numbers[0]
# index=1
# while index<len(numbers):
#     if numbers[index]>largest_num:
#         largest_num=numbers[index]
#     index=index+1
# print(largest_num)

#for loop
# numbers = [34, 67, 23, 89, 12, 55, 91, 44]
# largest_num=numbers[0]
# for num in numbers:
#     if num>largest_num:
#         largest_num=num
# print(largest_num)

# def largest_num(numbers):
#     largest=numbers[0]
#     index=1
#     while index<len(numbers):
#         if numbers[index]>largest:
#             largest=numbers[index]
#         index=index+1
#     return largest

# numbers=[34, 67, 23, 89, 12, 55]
# print(largest_num(numbers))


# Find Largest, Smallest & Position
# def find_large(arr):
#     largest = arr[0]
#     large_pos=0
#     index=1
#     while index < len(arr):
#         if arr[index]>largest:
#             largest = arr[index]
#             large_pos=index
#         index=index+1
#     return largest,large_pos

# def find_small(arr):
#     smallest=arr[0]
#     small_pos=0
#     index=1
#     while index < len(arr):
#         if arr[index]<smallest:
#             smallest = arr[index]
#             small_pos=index
#         index=index+1
#     return smallest,small_pos

# def display_result(arr):
#     largest, large_pos = find_large(arr)
#     smallest, small_pos = find_small(arr)
#     print("Array    :", arr)
#     print(f"Largest  : {largest}   at index {large_pos}")
#     print(f"Smallest : {smallest}   at index {small_pos}")

# numbers = [34, 67, 23, 89, 12, 55, 91, 44]
# display_result(numbers)











        


