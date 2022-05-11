'''
125. Valid Palindrome
Easy
Runtime: 40 ms, faster than 81.02% of Python online submissions for Valid Palindrome.
Memory Usage: 14.6 MB, less than 59.46% of Python online submissions for Valid Palindrome.
*NEED TO REDO THIS WITH A TWO POINTER SOLUTION

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        
        for thisCharacter in string.punctuation:
            s = s.replace(thisCharacter, "")
        
        s = s.replace(" ", "")
        
        if s == s[::-1]:
            return True
        else:
            return False