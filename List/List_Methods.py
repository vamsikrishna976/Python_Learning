
                                             #List Methods in Python

#append, insert, remove, pop, clear, index, count, sort, reverse, copy, extend

#apend
#append() adds an element at the end of the list
list1 = [1,2,3,4,5,6]
print(list1.append(8))

#insert
#insert() adds an element at a specified position in the list
list1 = [1,2,3,4,5,6]
list1.insert(3,8)
print(list1)

#remove
#remove() removes the first occurrence of a specified element from the list
list1 = [1,2,3,4,5,6]
list1.remove(2)
print(list1)

#pop
#pop() removes the element at the specified position in the list and returns it
list1 = [1,2,3,4,5,6]
list1.pop(4)
print(list1)

#clear
#clear() removes all elements from the list
list1 = [1,2,3,4,5,6]
list1.clear()
print(list1)

#index
# The index() method returns the index of the first occurrence of a specified element in the list
list1 = [1,2,3,4,5,6]
print(list1.index(2))

#count
# The count() method returns the number of occurrences of a specified element in the list
list1 = [1,2,3,4,5,6,6,6]
print(list1.count(6))

#sort
# The sort() method sorts the elements of the list in ascending order by default
list1 = ['h', 'e','t','f']
list1.sort()
print(list1)

#reverse
# The reverse() method reverses the order of the elements in the list
list1 = ['h', 'e','t','f']
list1.reverse()
print(list1)

#copy
# The copy() method returns a shallow copy of the list
list2=list1.copy()
print(list2)

#extend
# The extend() method adds the elements of a specified iterable (like another list) to the end of the list
list2=[2,3]
list2.extend(list1)
print(list2)