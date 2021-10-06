"""
Problem Statement 2#
Write a function that takes a number testVariable and returns a string that is its equivalent binary number.

Input #
A variable testVariable containing the decimal number.

Output #
String variable that contains the equivalent binary number of the input number.

Sample Input #
11
Sample Output #
"1011"
"""

def decimalToBinaryConverter(number):
    number = int(number)
    if number == 0: return ""
    else:
        return decimalToBinaryConverter(number // 2) + str(number % 2)

number = input("Enter decimal number: ")
print(decimalToBinaryConverter(number))