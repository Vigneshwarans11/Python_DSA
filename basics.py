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
numbers = [34, 67, 23, 89, 12, 55, 91, 44]
largest_num=numbers[0]
index=1
while index<len(numbers):
    if numbers[index]>largest_num:
        largest_num=numbers[index]
    index=index+1
print(largest_num)
    



