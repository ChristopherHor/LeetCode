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
    # Done with more elegant checked dictionary instead of brute force; to slow too be accepted as an answer (due to the checkIfInSolution being slow, not the dictionary which is about the fastest possible
    
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
    
#    def twoSum(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: List[int]
#        """
#        for counter in range(0, len(nums)):
#            thisNumber = nums[counter]
#            targetAddend = target - thisNumber
#
#            # Check if the difference between this number and the target is in the array
#            try:
#                checkNumber = nums.index(targetAddend)
#                
#                # Ensure we do not select the same number twice
#                if checkNumber == counter: # the target was in the array, but I've already selected it once
#                    checkNumber = nums.index(targetAddend, start=counter+1)
#                    
#                return [counter, checkNumber]
#            except:
#                pass
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutionSet = []
        checked = {} #holds the values we've checked thus far
        
        for ii, a in enumerate(nums):
            # Given first term, want its opposite to be what the other terms sum to (target) so altogher they sum to 0
            target = -a
            for jj, b in enumerate(nums):
                if jj == ii: # skip if using the same index number
                    continue
                else:
                    c = target - b #Given 2nd term, 3rd term can be calculated from the target (distance between b and a)
                    
                    if c in checked:
                        kk = checked[c]
                        thisSolution = [a, b, c]
                        
                        # Ensure we are not using the same elements
                        if ii != jj and jj != kk and ii != kk:
                            if self.checkIfInSolution(thisSolution, solutionSet):
                                pass
                            else:
                                solutionSet.append(thisSolution)
                    else:
                        checked[b] = jj
                        #checked[0] = 1
                        #b = 1
                        #target = 1.  1 - 1 = 0
                        #c = 1 - 1 = 0 which is in checked
                        #kk = 1

        return solutionSet