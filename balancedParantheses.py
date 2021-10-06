"""
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

"""


  
# Function to check parentheses
def checkBalancedParantheses(ip_str):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in ip_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
  
  
string = "{[]{()}}"
print(string,"-", checkBalancedParantheses(string))
  
string = "[{}{})(]"
print(string,"-", checkBalancedParantheses(string))
  
string = ")()("
print(string,"-",checkBalancedParantheses(string))