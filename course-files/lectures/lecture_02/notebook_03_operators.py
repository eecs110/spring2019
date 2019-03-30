
# # ----------------------------------------------------------------
# # Course: EECS 110, Northwestern University
# # Term: Winter 2019
# # Autogenerated from: "../lectures/lecture_02/03. Operators.ipynb"
# # 
# # Note: Each example is commented out. To uncomment, highlight
# # the area you want to uncomment and type "cmd /" (which both adds
# # and removes comments).
# # ----------------------------------------------------------------




# # --------------------------------------------------------------------------------
# # # OPERATORS
# # Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand (e.g. a, b, and c below). Operators do different things depending on the **data type** of the operand. In this section, we will go over four kinds of operators:
# # 
# # 1. [Arithmetic Operators](#1.-Arithmetic-Operators)
# # 2. [Comparison Operators](#2.-Comparison-Operators)
# # 3. [Logical Operators](#3.-Logical-Operators)
# # 4. [Assignment Operators](#4.-Assignment-Operators)
# # --------------------------------------------------------------------------------




# # --------------------------------------------------------------------------------
# # ## 1. Arithmetic Operators
# # Arithmetic operators help you to perform mathematical calculations, and always return a value (or an error):
# # 
# # | Operator | Name | Description |
# # |--|--|--|
# # | + | Addition | Adds values on either side of the operator |
# # | - | Subtraction | Subtracts right hand operand from left hand operand |
# # | * | Multiplication |	Multiplies values on either side of the operator |
# # | / | Division | Divides left hand operand by right hand operand	|
# # | % | Modulus | Divides left hand operand by right hand operand and returns remainder |
# # | \*\* | Exponent | Performs exponential (power) calculation on operators	|
# # | // | Floor Division | The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) |

# # --------------------------------------------------------------------------------




# # --------------------------------------------------------------------------------
# # ### 1.1. Numbers
# # --------------------------------------------------------------------------------

# # initialize variables for demo:
# a = 20
# b = 10
# c = 25
# print(a + b)    # addition
# print(a - b)    # subtraction
# print(a * b)    # multiplication
# print(b / a)    # division (notice the result is a float)
# print(c % a)    # modulus  25 / 20 = 1 with 5 left over (remained = 5)
# print(c // a)  # quotient  25 / 20 = 1 with 5 left over (quotient = 1)
# print(a ** b)  # exponent
# print(c ** (1/2))  # square root (notice the result is a float)



# # --------------------------------------------------------------------------------
# # ### 1.2. Strings
# # --------------------------------------------------------------------------------

# print('34' + '34')  # in the context of a string, the + sign concatenates two strings
# # Note: not all operators work with all datatypes. 
# # Uncomment the line below to see what happens.
# # print('34' - '34')
# print('34' * 100)  # but multiplication does work. In the context of a string, the * sign repeats the string n times.
# # Note: again, not all operators work with all datatypes. 
# # Uncomment the line below to see what happens.
# # print('34' * '34')



# # --------------------------------------------------------------------------------
# # ### 1.3. Booleans
# # --------------------------------------------------------------------------------

# # True implicitly converted to 1, False implicitly converted to 0.
# # same as: 1 + 1 + 0 + 0 + 1
# print(True + True + False + False + True)
# # Uncomment the line below to see what happens:
# # True / False  # you can't divide by zero!
# print(True * False)
# print(True * True)
# # wierd: why is this 200?
# print((('aa' == 'aa') + ('bb' == 'bb')) * 100)
# 
# # same as:
# #  (True + True) * 100
# #  (1 + 1) * 100
# #  (2) * 100
# #  200
# # even wierder. Why is this 0? 
# print(('aa' == 'aa' + 'bb' == 'bb') * 100) 
# 
# # Because addition gets evaluated before comparison operators (reviewed below)
# # same as: 
# #  ('aa' == ('aa' + 'bb') == 'bb') * 100 
# #  ('aa' == 'aabb' == 'bb') * 100
# #  (False) * 100
# #  (0) * 100
# #  0



# # --------------------------------------------------------------------------------
# # ## 2. Comparison Operators
# # Comparison operators compare two operands according to a comparison rule and evaluate to either True or False (boolean). They always return a boolean value. They are useful for branching logic: if some condition is True, then do something. Otherwise, do something else. 
# # 
# # | Operator | Description |
# # |--|--|
# # | == | If the values of two operands are equal, then the condition becomes true. |
# # | != | If values of two operands are not equal, then condition becomes true. |
# # | > | If the value of left operand is greater than the value of right operand, then condition becomes true. |
# # | < | If the value of left operand is less than the value of right operand, then condition becomes true. |
# # | >= | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. |
# # | <= | If the value of left operand is less than or equal to the value of right operand, then condition becomes true.|
# # --------------------------------------------------------------------------------




# # --------------------------------------------------------------------------------
# # ### 2.1. Numbers
# # --------------------------------------------------------------------------------

# a = 10
# b = 20
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)



# # --------------------------------------------------------------------------------
# # ### 2.2. Strings
# # You can use ( > , < , <= , <= , == , !=  ) to compare two strings. Python compares string lexicographically i.e using ASCII value of the characters.
# # 
# # Suppose you have str1  as "Mary"  and str2  as "Mac" . The first two characters from str1  and str2 ( M  and M ) are compared. As they are equal, the second two characters are compared. Because they are also equal, the third two characters ( r  and c ) are compared. And because 'r'  has greater ASCII value than 'c' , str1  is greater than str2.
# # 
# # **Source:** https://thepythonguru.com/python-strings/
# # --------------------------------------------------------------------------------

# # Even though Mary is longer than max, 'x' comes after 'r' in 
# # ASCII and is therefore bigger. This makes sense if you're thinking
# # about sorting a list of names in alphabetical order (smallest to
# # largest). 
# print('Mary' > 'Max')
# # wierd: case matters! Capital 'X' comes before lowercase 'r' in ASCII
# # Note: ord() is a built-in Python function for getting the ASCII (numeric) 
# # value of a character.
# print('Mary' > 'MaX')
# print('ASCII values for \'X\'', ord('X'))
# print('ASCII values for \'r\'', ord('r'))
# print('ASCII values for \'x\'', ord('x'))



# # --------------------------------------------------------------------------------
# # ### 2.3 Booleans
# # Like in the arithmetic operators examples, just act as if True is 1 and False is 0 and do comparisons just like numeric comparisons.
# # --------------------------------------------------------------------------------

# print(True > False)
# print(True == True)
# print(True < False)



# # --------------------------------------------------------------------------------
# # ## 3. Logical Operators
# # Logical operators allow a program to make a decision based on multiple conditions. For example, consider a game controller with 2 buttons. If both buttons are pressed (both are True) then the Ninja does a jump kick. If only the left button is pressed, then the Ninja does a forward kick. If only the right button is pressed, the Ninja does a punch. Checking whether one or more things is True or False is a fundamental part of computer programming.
# # 
# # | Operator | Description |
# # |--|--|
# # | and | if both operands are True then the expression evaluates to True. Otherwise, the expression evaluates to False |
# # | or | If either or both operands are True then the expression evaluates to True. Otherwise, the expression evaluates to False |
# # | not| If the operand is False than the expression evaluates to True (and vice versa) |
# # 
# # ### Truth Table
# # The table below, which is called a *Truth Table*, shows what happens in a variety of different scenarios for `v1` and `v2`.
# # 
# # | row num. | b1 | b2 | b1 and b2 | b1 or b2 | not b1 | not b2 | not (b1 and b2) | b1 and not b2 | b2 and not b1 |
# # |--|--|--|--|--|--|--|--|--|--|
# # | 1. | True | True | True | True | False| False | False | False | False |
# # | 2. | True | False | False | True | False | True | True | True | False |
# # | 3. | False | True | False | True | True | False | True | False | True |
# # | 4. | False | False | False | False | True|  True | True | False | False |
# # --------------------------------------------------------------------------------

# # let's walk through row #2, where b1 is True and b2 is False:
# b1 = True    # button 1 is pressed
# b2 = False   # button 2 is not pressed
# print(b1 and b2)
# print(b1 or b2)
# print(not b1)
# print(not b2)
# print(not (b1 and b2))
# print(b1 and not b2)
# print(b2 and not b1)



# # --------------------------------------------------------------------------------
# # ## 4. Assignment Operators
# # Assignment operators are a way of saying: "put the results of the expression stored in the right operand into the left operand." Unlike the three kinds of operators described above, assignment operators are meant to be used with variables.
# # 
# # | Operator | Description |
# # |--|--|
# # | =	| Assigns values from right side operands to left side operand |
# # | += | It adds right operand to the left operand and assign the result to left operand |
# # | -= | It subtracts right operand from the left operand and assign the result to left operand |
# # | *= | It multiplies right operand with the left operand and assign the result to left operand |
# # | /= | It divides left operand with the right operand and assign the result to left operand |
# # --------------------------------------------------------------------------------




# # --------------------------------------------------------------------------------
# # ### Examples of numbers, strings, and booleans
# # --------------------------------------------------------------------------------

# # initialize variables for demo:
# a = 20
# b = 10
# c = 25
# c = a + b  # assigns the value of a + b into c
# print(c)
# c = c + a  # assigns the current value stored in 'c' and the value stored in 'a' to 'c' (c gets replaced)
# print(c)
# c += a  #  equivalent to c = c + a
# print(c)
# c -= a  # equivalent to c = c - a
# print(c)
# c *= a  # equivalent to c = c * a
# print(c)
# c /= a  # equivalent to c = c / a
# print(c)
# 
# bool1 = True
# bool2 = False
# str1 = 'hello '
# bool1 = True
# int1 = 123
# # str1 += bool1     # throws an error if you don't convert it to a string first
# # str1 += int1      # ditto: throws an error if you don't convert it to a string first
# str1 += str(bool1)
# str1 += str(int1)
# print(str1)
