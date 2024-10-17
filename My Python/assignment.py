#write a program that ask the user for a number and print even if even or odd if odd
def even_odd():
    
    if number % 2==0:
        print("Even")
    else :
        print('Odd')

number= int(input('Enter any number:  '))
even_odd()

#write a program that takes three numbers as input and prints the largest one
def largest_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
num1= float(input('Enter first number: '))
num2= float(input('Enter second number: '))
num3= float(input('Enter third number: '))
print(largest_num(num1, num2, num3))

#Create a basic calculator that asks the user for two numbers and an operator (+, -, *, or /). Perform the operation and print the result.
def calculator():

    num1=float(input('Enter first number: '))
    operator=input('Enter operator: ')
    num2=float(input('Enter second number: '))

    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1-num2)
    elif operator == '*':
        print(num1*num2)
    elif operator == '/':
        print(num1/num2)
    else:
        print('Invalid operator')
calculator()

#Write a program that asks for a word and counts the number of characters in it.
def word():
    Word= input('Enter a word: ')
    print(len(Word))
word()

#Write a program that counts the number of vowels in a given string.
def vowel_count(string):
    
    vowel='AEIOUaeiou'
    count=0
    for char in string:
        if char in vowel:
            count =+ 1
            print (count)
user_input=input(str('Enter any word: '))
vowel_count(user_input)
