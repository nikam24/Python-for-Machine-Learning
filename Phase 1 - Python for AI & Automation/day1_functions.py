def greet(name = "Guest"): 
    print(f"Hello {name}, welcome to Python!") 

def add(a, b): 
    return a + b 

def math_ops(a, b): 
    return a+b, a-b, a*b, a/b, a//b, a%b, a**b 

# result = add(5, 10) 
# print(f"The sum is: {result}") 

result = math_ops(10, 3)
print(f"Addition: {result[0]}, Subtraction: {result[1]}, Multiplication: {result[2]}, Division: {result[3]}, Floor Division: {result[4]}, Modulus: {result[5]}, Exponentiation: {result[6]}")

greet("Pratham") 

# greet() 