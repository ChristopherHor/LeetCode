#5. Longest Palindromic Substring
#Medium
#
#Given a string s, return the longest palindromic substring in s.
#
#Example 1:
#
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
#Example 2:
#
#Input: s = "cbbd"
#Output: "bb"
# 
#
#Constraints:
#
#1 <= s.length <= 1000
#s consist of only digits and English letters.
#
#======================================================================
#SOLUTION - Assuming centers of palindromes
# Solved, but had to look up the algorithm then recreate it how I would type it (without looking)

class Solution(object):
    def longestPalindrome(self, s):
        
        longestPalindrome = ""
        longestPalindromeLength = 0
        
        for i in range(0, len(s)):
            # Given a character, assume it's the center of an odd length palindrome
            # Then expand left/right to see if it's still a palindrome
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                thisPalindrome = s[left:right+1] #Recall that string[0:0] returns empty, not the first chracter! so add 1
                #print(thisPalindrome)
                if len(thisPalindrome) > longestPalindromeLength:
                    longestPalindrome = thisPalindrome
                    longestPalindromeLength = len(longestPalindrome)
                left -= 1
                right += 1
                #print("left = ", left, " right = ", right)
            
            # Repeat, but this time assume an even length palindrome,
            # such as "abba".  Need to shift the right index by 1 basically (all code identical)
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                thisPalindrome = s[left:right+1] #Recall that string[0:0] returns empty, not the first chracter! so add 1
                if len(thisPalindrome) > longestPalindromeLength:
                    longestPalindrome = thisPalindrome
                    longestPalindromeLength = len(longestPalindrome)
                left -= 1
                right += 1
            
        return longestPalindrome