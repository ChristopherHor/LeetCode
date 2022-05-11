'''
704. Binary Search
Easy
Runtime: 231 ms, faster than 56.32% of Python online submissions for Binary Search.
Memory Usage: 14.6 MB, less than 54.97% of Python online submissions for Binary Search.

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''

# SOLUTION
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #----------------------------------------------------------
        # Raise errors for bad inputs
        if not isinstance(nums, list):
            raise ValueError("nums must be a 1D list")
        
        if not isinstance(target, int):
            raise ValueError("target must be an integer")
        
        for thisElement in nums:
            if not isinstance(thisElement, int):
                raise ValueError("all elements of nums must be integers")
            
        #----------------------------------------------------------
        # Inputs are as expected; begin processing
        
        # Try a binary search solution, dividing the search portions into shrinking halves
        
        def midPoint(indexLeft, indexRight):
            return indexLeft + ((indexRight - indexLeft) // 2)
        
        # Check left side of nums
        indexLeft = 0
        indexLeftOld = -1 # initialize old value to a different value to force first
        left = nums[indexLeft]
        if target == left:
            # Target is on the left side of the array; return the index of the left side of the list (0)
            return indexLeft
        elif target < left:
            # Target has a value less than the lowest value in the list; therefore the target is not
            # in the list.  Return -1 to signify target wasn't found
            return -1
        
        # Check right side of nums
        indexRight = len(nums) - 1
        indexRightOld = indexRight + 1 # initialize old value to an impossible value
        right = nums[indexRight]
        if target == right:
            return indexRight
        elif target > right:
            # Target has a value greater than the larget value in the list; therefore the target is not
            # in the list.  Return -1 to signify target wasn't found.
            return -1
        
        # Initialize indexMid before it's used in the while statement
        indexMid = midPoint(indexLeft, indexRight)
        
        # Prevent infinite loop by checking that the left and right bounds have changed.
        # If the bounds have not changed, break the loop.
        while indexLeft != indexLeftOld and indexRight != indexRightOld:
            indexMid = midPoint(indexLeft, indexRight)
            mid = nums[indexMid]
            print(mid)
            if target == mid:
                return indexMid
            elif target < mid: # target is to the left of mid
                indexRightOld = indexRight
                indexRight = indexMid
            else: # target is to the right of mid
                indexLeftOld = indexLeft
                indexLeft = indexMid
        
        # If got to this point, then we could not find the target
        return -1
       
        #=================================================================
        # Sample Iterations
        #
        # SIMPLE FOUND
        # 0123
        #  1 = Target
        # left = 0
        # right = 3
        # mid = 1
        #
        # REALISTIC FOUND
        # 0 1 2 3 4 5 6 7 8 9 10 11
        # Target = 7
        # left = 0, right = 11, mid = 5
        # left = 5, right = 11, mid = 8
        # left = 5, right = 8, mid = 6
        # left = 6, right = 8, mid = 7 = Target --> Return indexMid
        #
        # SAME AS ABOVE BUT WITH FORMULAS FOR MID, LEFT, RIGHT
        # 0 1 2 3 4 5 6 7 8 9 10 11
        # Target = 7
        #
        # left = 0
        # right = 11
        # mid = 5
        #
        # 7 > 5 so
        # left = mid = 5
        # right = 11
        # mid = ((right - left) // 2) + left = 8
        #
        # 7 < 8 so
        # left = left = 5
        # right = mid = 8
        # mid = 6
        #
        # 7 > 6 so
        # left = mid = 6
        # right = right = 8
        # mid = 7 = Target return mid
        
        #===================================================================
        # Check cases where the target will NOT be found
        #
        # 0, 1, 2, 3
        # target = -5 
        # Target is less than lowest value in array (leftmost) so return -1 not found
        #
        # 0, 1, 2, 3
        # target = 99
        # Greater than last value in list so return -1 not found
        #
        # 0, 1, 2, 3
        # target 2.9 (technically fractional numbers not allowed, but elicits same behavior
        #             while keeping the indices easy to count)
        # left = 0, right = 3, mid = 1
        # left = 1, right = 3, mid = 2
        # left = 2, right = 3, mid = 2
        #
        # Target 7 Will Not Be Found
        # 0 1 2 3 4 5 6   8 9 10 11
        # Target = 7
        # left = 0, right = 10 (value 11), mid = 5
        # left = 5, right = 10 (value 11), mid = 8 (value 9)
        # left = 5, right = 8 (value 9), mid = 6
        # left = 6, right = 8 (value 9), mid = 7 (value 8)
        # left = 6, right = 7 (value 8), mid = 6
        # left = 6, right = 7 (value 8), mid = 6