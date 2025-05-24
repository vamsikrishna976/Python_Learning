
                                                         # List in Python

# A list is a collection of items that can be of different types, including numbers, strings, and other lists.
# Lists are mutable, meaning you can change their content without changing their identity.
# Lists are defined using square brackets [] and can contain any number of items.
# Example of a list
list = ['H','e','l','l','o']
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

# Negative indexing in Python lists
# Negative indexing allows you to access elements from the end of the list.
# The last element is accessed with index -1, the second last with -2, and so on.
l1 = [1,2,3,4,5]
#  -5,-4,-3,-2,-1

print(l1[-4])
print(l1[-3])
print(l1[-2])
print(l1[-1])
print(l1[-5])

# Slicing in Python lists
# Slicing allows you to access a range of elements in a list.
# The syntax for slicing is list[start:stop:step], where:
# - start is the index of the first element to include (default is 0)
# - stop is the index of the first element to exclude (default is the length of the list)
# - step is the number of elements to skip (default is 1)
l2 = [1,2,3,4,5,6]
print(l2[0:5:2])

l2 = [1,2,3,4,5,6,7,7]
print(l2[0:7:3])

