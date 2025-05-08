                                           # Data types in Python
'''
Data types in Python are the classification or categorization of data items.
# Python has various built-in data types, which can be categorized into several classes.
# The most commonly used data types in Python are:
# 1. Numeric Types: These include integers (int), floating-point numbers (float), and complex numbers (complex).
#    - int: Represents whole numbers, both positive and negative, without decimals.
#    - float: Represents real numbers, which can be positive or negative, and can have decimal points.
#    - complex: Represents complex numbers, which are numbers with a real and imaginary part.
#
# 2. Sequence Types: These include strings (str), lists (list), and tuples (tuple).
#    - str: Represents a sequence of characters, enclosed in single or double quotes.
#    - list: Represents an ordered collection of items, which can be of different data types. Lists are mutable, meaning their contents can be changed.
#    - tuple: Represents an ordered collection of items, similar to lists, but tuples are immutable, meaning their contents cannot be changed after creation.
#
# 3. Mapping Type: This includes dictionaries (dict).
#    - dict: Represents a collection of key-value pairs, where each key is unique and maps to a value. Dictionaries are mutable.
#
# 4. Set Types: These include sets (set) and frozensets (frozenset).
#    - set: Represents an unordered collection of unique items. Sets are mutable.
#    - frozenset: Represents an unordered collection of unique items, similar to sets, but frozensets are immutable.
#
# 5. Boolean Type: This includes boolean values (bool).
#    - bool: Represents one of two values: True or False.
#
#
# 6. None Type: This includes the None type.
#    - None: Represents the absence of a value or a null value.
#
# 7. Binary Types: These include bytes, bytearray, and memoryview.  
#    - bytes: Represents a sequence of bytes, which are immutable.
#    - bytearray: Represents a mutable sequence of bytes.
#    - memoryview: Represents a view of the memory of a bytearray or bytes object, allowing for efficient manipulation of binary data.
#
#
# 8. User-defined Types: Python also allows the creation of user-defined data types using classes.
#    - class: A blueprint for creating objects, which can have attributes (data) and methods (functions) associated with them.
#    - object: An instance of a class, which can have its own state and behavior.
#
# 9. Type Hints: Python supports type hints, which allow developers to specify the expected data types of function parameters and return values.
#    - Type hints are not enforced at runtime but can be used by static type checkers and IDEs to provide better code analysis and suggestions.
#    - Type hints are specified using the syntax: def function_name(parameter_name: data_type) -> return_type:
#    - Example: def add_numbers(a: int, b: int) -> int:
#               return a + b
'''


# Numeric Types
# Numeric types in Python are used to represent numbers. There are three main numeric types in Python:
# integers (int), floating-point numbers (float), and complex numbers (complex).
#
# 1. Integer (int): Represents whole numbers, both positive and negative, without decimals.
#    - Example: 5, -10, 0
#    - Integers can be of arbitrary size, limited only by the available memory.
#    - Python automatically handles large integers, so you don't need to worry about overflow.
#    - Integers can be represented in different bases, such as decimal (base 10), binary (base 2), octal (base 8), and hexadecimal (base 16).

#    - Example:
a=10
b=20
c=a+b
print(c)
# # Output: 30
print(type(c))
# # Output: <class 'int'>
# # The type() function returns the type of the variable 'c', which is an integer.
# # The output shows that 'c' is of type 'int'.
# # You can also perform various arithmetic operations with integers, such as addition, subtraction, multiplication, and division.

# 2. Floating-point number (float): Represents real numbers, which can be positive or negative, and can have decimal points.
#    - Example: 3.14, -0.5, 2.0
#    - Floating-point numbers are represented in Python using the IEEE 754 double-precision format.

#    - Example:
a=3.14
b=2.0
c=a+b
print(c)
# # Output: 5.14
print(type(c))
# # Output: <class 'float'>
# # The type() function returns the type of the variable 'c', which is a floating-point number.
# # The output shows that 'c' is of type 'float'.
# # You can also perform various arithmetic operations with floating-point numbers, such as addition, subtraction, multiplication, and division.

# 3. Complex number (complex): Represents complex numbers, which are numbers with a real and imaginary part.
#    - Example: 2 + 3j, -1 - 4j
#    - Complex numbers are represented in Python using the 'j' suffix for the imaginary part.
#    - Example:
a=2+3j
b=1-4j
c=a+b
print(c)
# # Output: (3-1j)
print(type(c))
# # Output: <class 'complex'>
# # The type() function returns the type of the variable 'c', which is a complex number.
# # The output shows that 'c' is of type 'complex'.
# # You can also perform various arithmetic operations with complex numbers, such as addition, subtraction, multiplication, and division.
# # The real and imaginary parts of a complex number can be accessed using the 'real' and 'imag' attributes.
#    - Example:
a=2+3j
print(a.real)  # Output: 2.0
# print(a.imag)  # Output: 3.0
# # The 'real' attribute returns the real part of the complex number, and the 'imag' attribute returns the imaginary part.
# # You can also convert between different numeric types using type conversion functions, such as int(), float(), and complex().
#    - Example:

a=3.14
b=int(a)
print(b)  # Output: 3
# # The int() function converts the floating-point number 'a' to an integer.
# # The output shows that 'b' is now an integer.
# # You can also convert integers to floating-point numbers and complex numbers using the float() and complex() functions, respectively.
#    - Example:

a=5
b=float(a)
print(b)  # Output: 5.0
# # The float() function converts the integer 'a' to a floating-point number.
# # The output shows that 'b' is now a floating-point number.
# # You can also convert floating-point numbers to integers and complex numbers using the int() and complex() functions, respectively.
#    - Example:


a=3.14
b=complex(a)
print(b)  # Output: (3.14+0j)
# # The complex() function converts the floating-point number 'a' to a complex number.
# # The output shows that 'b' is now a complex number with a real part of 3.14 and an imaginary part of 0.
# # You can also convert complex numbers to integers and floating-point numbers using the int() and float() functions, respectively.
#    - Example:


a=2+3j
b=int(a)
print(b)  # Output: 2
# # The int() function converts the complex number 'a' to an integer.
# # The output shows that 'b' is now an integer with a value of 2.
# # Note that the imaginary part is discarded when converting a complex number to an integer.
#    - Example:


a=2+3j
b=float(a)
print(b)  # Output: 2.0
# # The float() function converts the complex number 'a' to a floating-point number.
# # The output shows that 'b' is now a floating-point number with a value of 2.0.
# # Note that the imaginary part is discarded when converting a complex number to a floating-point number.
#    - Example:


a=2+3j
b=complex(a)
print(b)  # Output: (2+3j)
# # The complex() function converts the complex number 'a' to a complex number.
# # The output shows that 'b' is still a complex number with the same value as 'a'.
# # Note that the complex() function does not change the value of the complex number.

# 4. Type conversion: Python provides built-in functions to convert between different numeric types.
#    - Example:
a=5
b=float(a)
print(b)  # Output: 5.0
# # The float() function converts the integer 'a' to a floating-point number.
# # The output shows that 'b' is now a floating-point number.
# # You can also convert floating-point numbers to integers and complex numbers using the int() and complex() functions, respectively.
#    - Example:


a=3.14
b=int(a)
print(b)  # Output: 3
# # The int() function converts the floating-point number 'a' to an integer.
# # The output shows that 'b' is now an integer.
# # Note that the decimal part is discarded when converting a floating-point number to an integer.
#    - Example:


a=3.14
b=complex(a)
print(b)  # Output: (3.14+0j)
# # The complex() function converts the floating-point number 'a' to a complex number.
# # The output shows that 'b' is now a complex number with a real part of 3.14 and an imaginary part of 0.
# # You can also convert complex numbers to integers and floating-point numbers using the int() and float() functions, respectively.

