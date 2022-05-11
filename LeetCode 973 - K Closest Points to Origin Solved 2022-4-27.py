973. K Closest Points to Origin
Medium
SOLVED - solution is slow due to sort function on a large list.  Solution can be improved by using a small stack which has the "winners" appended/popped as necessary and the sort would only be on the size of K instead of the number of points which is much longer.  


Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104

'''
==================================================
'''

import math
class Solution(object):
    
    def distanceSimple(self, x, y):
        # technically might not have to calculate the square root to compare values since
        # 28 < 29 and sqrt(28) < sqrt(29) regardless so can do that if want quicker code
        #return math.sqrt(x**2 + y**2)
        return x**2 + y**2
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # 2 columns, # rows equal to number of points
        distances = [[0 for col in range(2)] for row in range(len(points))] 
        
        '''
        [
        [0, 0]
        [0, 0]
        [0, 0]
        [0, 0]
        ]
        '''
        
        # Loop through all points
        for ii in range(0, len(points)):
            x = points[ii][0]
            y = points[ii][1]
            # Put distance in first column of the 2d list so it can be sorted with 
            # distances.sort() later on.  Putting it in other columns would require 
            # something like #sorted(distances, key= lambda x:x[1]) which is a lot 
            # harder to read
            distances[ii][0] = self.distanceSimple(x, y)
            distances[ii][1] = ii # store index of the point
            
        #sorted(distances, key= lambda x:x[0])
        distances.sort() # sort on the lowest distance
        ''' Now distances looks something like this:
        If provided [ [2, 2], [1, 1]] then the results look like this: since the [distance, index] are [8, 0] and [2, 1] which then gets sorted to...
        [
        2, 1 
        8, 0
        ]
        '''
        returnList = []
        # Return the first k points in points by finding their indices from the 2nd 
        # column of distances
        for kCounter in range(k):
            pointerIndex = distances[kCounter][1]
            print(pointerIndex)
            returnList.append(points[pointerIndex])
        
        return returnList