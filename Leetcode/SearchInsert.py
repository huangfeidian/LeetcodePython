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
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.lower_bound(nums,0,len(nums),target);
instance=Solution();
print instance.searchInsert([1,3,5,6], 0);