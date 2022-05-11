'''
1046. Last Stone Weight
Easy

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

=========================================================================
'''

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        '''
        # Example of smashing rocks.  Recall largest 2 rocks are smashed together
        [2, 7, 4, 1, 10, 1]
        [2, 4, 1, 1, 3]
        [2, 1, 1, 1]
        [1, 1, 1]
        [1]
        1 is the return
        '''
        
        # Ensure input is a list
        if not isinstance(stones, list):
            return None
        
        # Ensure input is not empty
        if len(stones) == 0:
            return None
        
        # Ensure input is one dimensional
        if isinstance(stones[0], list):
            return None
        
        # Ensure all inputs are integers (would normally check float too, but problem states ints only)
        for thisStone in stones:
            if not isinstance(thisStone, int):
                return None
        
        # If only provided one stone, return the stone
        if len(stones) == 1:
            return stones[0]
        
        # Continually smash stones until the list of stones is of length 1 or less
        while len(stones) > 1:
            
            stoneLeft = 0
            stoneRight = 0
            stoneLeftIndex = None
            stoneRightIndex = None
                
            # Search through stones for two heaviest stones
            for ii in range(len(stones)):
                
                thisStone = stones[ii]

                # If thisStone is larger than the left or right stone, replace one with thisStone
                # Formulate it such that rightStone is the larger stone
                # SAMPLE STONE ADDITIONS EXAMPLE: 
                # left, right; thisStone
                # 0, 0; 3
                # 0, 3; 9
                # 3, 9; 8
                # 8, 9; 9
                # 9, 9; 10
                # 9, 10
                if thisStone > stoneLeft:
                    if thisStone > stoneRight:
                        # If thisStone is bigger than both the left/right stones, then
                        # shift the stones leftwards.  The left stone goes away, the
                        # right stone becomes the left, and the new stone becomes the right.
                        # That way, the heaviest stone is always on the right.
                        stoneLeft = stoneRight
                        stoneLeftIndex = stoneRightIndex
                        
                        stoneRight = thisStone
                        stoneRightIndex = ii
                    else:
                        # This stone was only heavier than the left stone; replace the left stone only
                        stoneLeft = thisStone
                        stoneLeftIndex = ii
            
            # Smash the two stones together.  Yay!
            newStone = stoneRight - stoneLeft # Dont' need abs() because formulated stoneRight 
                                              # to be >= stoneLeft
            
            # Add the stone to the list of stones if and only if the new stone has a weight of 1 or more
            # A "Stone" of 0 is considered destroyed and does not need to be appended to the list of stones
            if newStone > 0:
                stones.append(newStone)
            
            # Destroy the old stones via pop() starting with the larger index to avoid the new
            # list order from popping the wrong stone.  Indices are guaranteed to be non-equal
            # due to formulation
            if stoneLeftIndex < stoneRightIndex:
                stones.pop(stoneRightIndex)
                stones.pop(stoneLeftIndex)
            else:
                stones.pop(stoneLeftIndex)
                stones.pop(stoneRightIndex)
        
        # Problem states if no rocks remain to return 0, otherwise return the weight of the rock
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
        