"""
PROBLEM STATEMENT:
13. Roman to Integer
Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

"""
=====================================================================
SOLUTION
"""

class Solution(object):
    # Future improvements:
    #     - shrink size of string after counting values to lower string length
    #         to speed up for long strings
    #     - replace if statements in beginning with for loop of known subtractive strings
    #     - replace hardcoded subtractive strings with code to calculate the subtractive strings
    #         which would involve letters of the same order of magnitude only
    
    def countSubString(self, subString, bigString):
        count = 0
        #abcd    #this is how I think about the lengths of the strings to compare
        #1234567 #this is how I think about the lengths of the strings to compare
        
        subStringLength = len(subString)
        for counter in range(0, len(bigString) - subStringLength + 1):
            if bigString[counter:counter+subStringLength] == subString:
                count = count + 1
        
        return count
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        total = 0
        
        s = upper(s)
        
        if "CD" in s:
            total = total + 400
            s = s.replace("CD", "")
        elif "CM" in s:
            total = total + 900
            s = s.replace("CM", "")
            
        if "XL" in s:
            total = total + 40
            s = s.replace("XL", "")
        elif "XC" in s:
            total = total + 90
            s = s.replace("XC", "")
        
        if "IV" in s:
            total = total + 4
            s = s.replace("IV", "")
        elif "IX" in s:
            total = total + 9
            s = s.replace("IX", "")
        
        valueDict = {"I": 1, \
                     "V": 5, \
                     "X": 10, \
                     "L": 50, \
                     "C": 100, \
                     "D": 500, \
                     "M": 1000}
        
        for key in valueDict:
            total = total + (self.countSubString(key, s) * valueDict[key])
        
        return total
