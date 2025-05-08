                          
                                # Variable syntax in Python

# In Python, a variable is a name that refers to a value.
# A variable is created when a value is assigned to it using the assignment operator '='.
# The syntax for creating a variable is as follows:
# variable_name = value
# where 'variable_name' is the name of the variable and 'value' is the value to be assigned to it.
# The variable name can be any valid identifier, which means it can contain letters, numbers, and underscores.
# However, it cannot start with a number and cannot be a reserved keyword in Python.
# The value can be any valid Python object, such as a number, string, list, tuple, dictionary, set, or any other object.
# The variable name is case-sensitive, so 'a' and 'A' are different variables.
# Variable names should be descriptive and meaningful, so that the code is easy to read and understand.
# For example:
# my_variable = 10
# In this example, 'my_variable' is the name of the variable and '10' is the value assigned to it.
# The variable 'my_variable' now refers to the value '10'.
# The value can be changed by assigning a new value to the variable.
# For example:
# my_variable = 20
# In this example, the value of 'my_variable' is changed from '10' to '20'.
# The variable can also be reassigned to a different value of a different type.

# Variable assignment in Python
# Variable assignment in Python is done using the '=' operator.
# The variable name is on the left side of the '=' operator, and the value to be assigned is on the right side.
# The variable name can be any valid identifier, and the value can be any valid Python object.
# The value can be a number, string, list, tuple, dictionary, set, or any other object.
# The variable name can also be a combination of letters, numbers, and underscores, but it cannot start with a number.
# Variable names are case-sensitive, so 'a' and 'A' are different variables.
# Variable names should be descriptive and meaningful, so that the code is easy to read and understand.

a=6
print(a)
# 6

'''
b,c=7
print(b,c)
 TypeError: cannot unpack non-iterable int object
'''

b,c=7,9
print(b,c)
# 7 9

a=b=c=10
print(a,b,c)
# 10 10 10

d='vamsi'   
print(a)
# vamsi

e="Krishna"
print(e)
# Krishna




