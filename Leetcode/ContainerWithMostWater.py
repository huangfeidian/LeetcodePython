class Solution:
    # @return an integer
    def maxArea(self, height):
        left = 0; right = len(height)-1
        res = 0
        while left < right:
            water = min(height[left], height[right]) * (right-left)
            if water > res: res = water
            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1
        return res
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        current_max=height[0];
        max_area=0;
        max_vector=[(height[0],0),];
        for i in range(1,len(height)):
            if(height[i]>current_max):
                max_vector.append((height[i],i));
                current_max=height[i];
            else:
                for j in range(len(max_vector)):
                    max_area=max(min(max_vector[j][0],height[i])*(i-max_vector[j][1]),max_area);
        if(len(max_vector)>=2):
            for i in range(len(max_vector)):
                max_area=max(max_vector[i][0]*(max_vector[-1][1]-max_vector[i][1]),max_area);
        return max_area;
instance =Solution();
print instance.maxArea([1,2]);