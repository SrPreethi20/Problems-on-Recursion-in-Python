# Problems-on-Recursion-in-Python
Recursion problems in Python

Problem Statement 1#
Implement a function that takes an array testVariable containing opening ( and closing parenthesis ) and determines whether or not the brackets in the array are balanced. The function also takes startIndex = 0 and currentIndex = 0 as parameters.

What does “Balanced Parenthesis” Mean? #
Balanced parentheses mean that each opening bracket ( has a corresponding closing bracket ). Also, the pairs of parentheses are properly nested.

Consider the following correctly balanced parentheses:

()
(())
(())()
((()))((()))
Now take a look at some incorrectly balanced parentheses:

(
)()(
((()()()()
((())))((((()
Input #
An array testVariable containing opening and closing parentheses.

testVariable = ["(", ")", "(", ")"]
Output #
true if the parentheses in the input array are balanced. false if the parentheses in the input array are imbalanced.







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
Problem Statement 3#
Implement a function that takes two numbers, testVariable1 and testVariable2 and returns their greatest common divisor.

What is the Greatest Common Divisor? #
The Greatest Common Divisor of two or more integers is the largest positive integer that divides each of the integers.

For example, take two numbers 42 and 56.

42 can be completely divided by 1, 2, 3, 6, 7, 14, 21 and 42.

56 can be completely divided by 1, 2, 4, 7, 8, 14, 28 and 56.

Therefore, the greatest common divisor of 42 and 56 is 14.

Input #
Two variables testVariable1 and testVariable2 containing numbers.

Output #
The greatest common divisor of testVariable1 and testVariable2.

Sample Input #
6, 9
Sample Output #
3
