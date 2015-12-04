class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if( len(height)<3):
            return 0;
        right_high=[0 for i in range(len(height))];
        current_max=right_high[-1]=height[-1];
        
        for i in reversed(range(len(height))):
            right_high[i]=max(height[i],current_max);
            current_max=right_high[i];
        current_max=height[0];
        total=0;
        for i in range(len(height)):
            current_max=max(current_max,height[i]);
            total+=min(current_max,right_high[i])-height[i];
        return total;