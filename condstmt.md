## **write a program to check wether a person is eligible for voting or not.(accept age from user)**
Input Function Syntax:

input("enter a value") should not be inside int[]. The input function is used to get user input as a string, and you need to convert it to an integer using int(). The correct syntax is int(input("Enter a value: ")).
Comparison Operator:

The original code uses <= 18, which means the person is considered not eligible if they are 18 or younger. If you want to consider eligibility based on being 18 or older, you should use < 18 to check if they are under 18.
Indentation:

Ensure that the print statements are properly indented inside the if and else blocks. Python relies on indentation to define blocks of code.
Summary
Use int(input("...")) to correctly handle user input and conversion.
Ensure the comparison operator aligns with your eligibility criteria.
Maintain proper indentation for code blocks in Python.
Here’s a quick summary of how it works:

x = int(input("Enter a value: ")): Takes input from the user, converts it to an integer, and assigns it to x.
if x < 18:: Checks if the value is less than 18.
print("Person is not eligible"): Outputs if the person is not eligible.
print("Person is eligible"): Outputs if the person is eligible
![preview](images.png/image1.png)




## **write a program to check whether a number entered by user is even or odd.** 
![preview](images.png/image2.png)
## Explanation:
### 1.Read input

x = int(input("enter a value"))

Gets a number from the user and converts it to an integer.

### 2.Check Even or Odd:


if x % 2 == 0:

 Checks if the number is divisible by 2 with no remainder (i.e., it's even).


 ### 3.print result

 print("even")

 if the number is even it prints "even"

 print("odd")

if the number is not even it prints "odd"


## **write a program to check whether a number is divisible by 7 or not**

## Explanation:
![preview](images.png/image3.png)

### 1.Read input


x = int(input("enter a value"))

Takes a number from the user and converts it to an integer.

### 2.Check Divisibility:

if x % 7 == 0:

x % 7 == 0: Checks if the number is divisible by 7 without any remainder.
### 3.Print Result:

print("yes it divisible")

If the number is divisible by 7, it prints "yes it divisible".

print("it does not divisible")

If the number is not divisible by 7, it prints "it does not divisible".

## **write a program to display "hello"if a number entered by user is a multiple of five,otherwise print "bye"**
## Explanation:
![preview](images.png/image4.png)
### 1.Input Value:


x = int(input("enter a value"))


This line prompts the user to enter a number. The input function gets the input as a string, and int converts it to an integer.

### 2.Condition Check:


if x*5==0:

This line checks if x multiplied by 5 is equal to 0.

### 3.Output Based on Condition:


If the condition is true (i.e., x is 0 because 0 multiplied by 5 is 0), it prints

print("hello")

If the condition is false (i.e., x is any value other than 0), it prints

print("bye")


## **write a program to display the last digit of a number**
## Explanation:
![preview](images.png/image5.png)
### 1.Input Value:

x = int(input("enter a value"))
This line asks the user to enter a number. The input function gets the input as a string, and int converts it to an integer.
### 2.Check Last Digit:

if x % 10:

This line uses the modulus operator % to get the remainder when x is divided by 10. The remainder is the last digit of the number.

If the remainder is not zero, this means the last digit is not zero.

3.Print Result:

If the last digit is not zero (i.e., x % 10 is not zero), it prints:

print("yes it last digit")

If the last digit is zero (i.e., x % 10 is zero), it prints:

print("not last digit")

## **write a program to check whether the last digit of a number(entered by usr)is divisible by 3 or not**
## Explanation:
![preview](images.png/image6.png)

### 1.Input Value:

x = int(input("enter a value"))

This line prompts the user to enter a number. The input is taken as a string and then converted to an integer using int.
### 2.Check Divisibility by 3:


if x % 3:

The % operator calculates the remainder when x is divided by 3.
If x % 3 is not zero, it means x is not evenly divisible by 3.
### 3.Print Result:

If the remainder is not zero (i.e., x % 3 is not zero), the program prints:
print("yes it is divisible")

If the remainder is zero (i.e., x % 3 is zero), the program prints:
print("does not divisible by 3")


























