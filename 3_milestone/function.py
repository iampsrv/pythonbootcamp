# def greet():
#     print("Hello, there!")

# def add_numbers(a, b):
#     return a + b

# def subtract_numbers(a, b):
#     return b-a

# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# result = add_numbers(3, 5)
# print(result)
# print(subtract_numbers(2,8))

# def greet_person(name="Anonymous"):
#     print("Hello, " + name + "!")
# greet_person() # Output: Hello, Anonymous!
# greet_person("John") # Output: Hello, John!

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
# result = multiply(2)
# print(result) # Output: 24