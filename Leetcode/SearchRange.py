class Solution(object):

    def lower_bound(self,nums,left,right,target):
        count=right-left;
        it=0;
        step=0;
        while(count>0):
            it=left;
            step=count/2;
            it=it+step;
            if(nums[it]<target):
                left=it+1;
                count-=step+1;
            else:
                count=step;
        return left;

    def upper_bound(self,nums,left,right,target):
        count=right-left;
        left=0;
        right=count;
        it=0;
        step=0;
        while(count>0):
            it=left;
            step=count/2;
            it=it+step;
            if(not (target<nums[it])):
                left=it+1;
                count-=step+1;
            else:
                count=step;
        return left;
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_result=self.lower_bound(nums,0,len(nums),target);
        right_result=self.upper_bound(nums,0,len(nums),target);
        if(left_result==right_result):
            return [-1,-1];
        else:
            return [left_result,right_result-1];