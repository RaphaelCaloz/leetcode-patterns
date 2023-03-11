'''
Say we have a palindrome X. What is the next palindrome?

Each palindrome of dd digits has a palindromic root, it's first k = (d+1)/2 digits. 
The next palindrome is formed by the next root.

For example, if 123123 is a root for the 5 digit palindrome 1232112321, 
then the next palindrome is 1242112421 with root 124124.

Notice that roots and palindromes are not a bijection, 
as palindromes 123321123321 and 1232112321 have the same root.
'''

# Python3 program to check if a number is Palindrome
 
# Function to check Palindrome
def checkPalindrome(n):
 
    reverse = 0
    temp = n
    while (temp != 0):
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
     
    return (reverse == n) # if it is true then it will return 1;
                   # else if false it will return 0;
 
# driver code
n = 7007
if (checkPalindrome(n) == 1):
    print("Yes")
 
else:
    print("No")