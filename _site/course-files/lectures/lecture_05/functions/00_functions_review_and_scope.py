# ## Example 1:
## What's wrong with this function? Please fix it!
def print_message(name):
    print('Hello, name!')

print_message('Jelani')
print_message('Merissa')
## End Example 1




# ## Example 2:
# ## What's wrong with this function? Please fix it!
# def sum(num1, num2):
#     num1 + num2

# result = sum(5, 7)
# print('The sum is:', result)
# ## End Example 2




## Example 3:
## What's wrong with this function? Please fix it!
def sum_1(num1, num2):
    return num1 + num2

a = input('Enter the first number: ')
b = input('Enter the second number: ')
print('The difference is: ' + sum_1(a, b))
## End Example 3





# ## Example 4: Scope Demo 1: local variable takes precedent over global variable
# ## What will print to the screen?
# ## Walter or Lindsay?
# name = 'Lindsay'

# def scope_demo_1(name):
#    print(name)

# scope_demo_1('Walter')
# ## End Example 4





# ## Example 5: Scope Demo 2: global variables can be accessed from within functions 
# ## (though this is not recommended). Best practice is to pass in all the variables
# ## the function needs via parameters
# name1 = 'Lindsay'

# def scope_demo_2(name):
#    print(name)
#    print(name1)

# scope_demo_2('Walter')
# ## End Example 5




# ## Example 6: Scope Demo 3: local variables that are defined within function blocks
# ## cannot be accessed outside of them

# def scope_demo_3(name):
#    greeting = 'Welcome, '
#    print(greeting + name)

# scope_demo_3('Jimmy')
# # print(greeting)  # throws an error because greeting was defined inside of a function
# # ## End Example 6
