#15. 3Sum
#Medium
#
#Share
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#Notice that the solution set must not contain duplicate triplets.
#
#Example 1:
#
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Example 2:
#
#Input: nums = []
#Output: []
#Example 3:
#
#Input: nums = [0]
#Output: []
# 
#
#Constraints:
#
#0 <= nums.length <= 3000
#-105 <= nums[i] <= 105

=======================================================================

class Solution(object):
    # Done via brute force exhaustion; too slow to be accepted as an answer
    
    def checkIfInSolution(self, mySolution, solutionSet):
        isInSolution = False
        for thisSolution in solutionSet:
            #if mySolution[0] in thisSolution and mySolution[1] in thisSolution and mySolution[2] in thisSolution:
            #if collections.Counter(mySolution) == collections.Counter(thisSolution)
                #isInSolution = True
            
            if len(thisSolution) != len(mySolution):
                isInSolution = False
            else:
                numMatchingAddends = 0
                for addend in mySolution:
                    if mySolution.count(addend) == thisSolution.count(addend):
                        numMatchingAddends = numMatchingAddends + 1
                if numMatchingAddends == len(mySolution):
                    isInSolution = True
                    return isInSolution
        return isInSolution

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutionSet = []
        
        for ii in range(0, len(nums)):
            a = nums[ii]
            
            for jj in range(0, len(nums)):
                b = nums[jj]
                if jj == ii:
                    continue
                for kk in range(0, len(nums)):
                    c = nums[kk]
                    if kk == ii:
                        continue
                    if kk == jj:
                        continue
                    
                    if a + b + c == 0:
                        thisSolution = [a, b, c]
                        if self.checkIfInSolution(thisSolution, solutionSet):
                            pass
                        else:
                            solutionSet.append(thisSolution)
        return solutionSet