#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
def multiplication_or_sum (num1, num2):
    product = num1*num2
    if product<=1000:
        return product 
    else:return num1+num2
result= multiplication_or_sum(20,30)
print (f"The result is {result}")



print(4)

#Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number#
print("Printing current and previous number and their sum in range '10'")
previous_num=0
#loop 1 to 10
for i in range (1,11):
    sum= previous_num + i
    print(f"Current Number: {i}, Previous Number: {previous_num}, Sum: {sum}")
    previous_num = i



#Python code to accept a string from the user and display characters present at an even index number.
word = input ('enter word:')
print("original string:", word)
size=len('word')
print('Printing only even index char:')
for i in range(0, size, 2):
    print("index[", i, "]", word[i])

#write a code that will output hello Alice and Hello John on the display window
def greet(name):
    print(f'hello, {name}!')

def main():
    greet("Alice")
    greet("John")
main()

#find the addition of 10 and 5 as well as the subtraction between 10 and 5
def add(a,b):
    return a+b
def subrtact(a,b):
    return a-b
num1=10
num2=5
addition_result=add(num1, num2)
print(f'the sum of {num1} and {num2} is {addition_result}')
subtraction_result=add(num1,num2)
print(f'the differece of {num1} and {num2} is {subtraction_result}')

#write a code that will out put the multiplication between 10 and 5
def multiply (x,y):
    return x*y
num1=10
num2=5
multiplication_result=multiply(num1,num2)
print(f"multiplication_result of {num1} and {num2} is {multiplication_result}")

#write a code that will miltiply iterated values between 0 and 10