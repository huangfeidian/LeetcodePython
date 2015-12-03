class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cliff=len(nums);
        for x in reversed(range(1,cliff)):
            if(nums[x-1]<nums[x]):
                cliff=x;
                break;
        if(cliff==len(nums)):
            nums.sort();
            return ;
        for x in reversed(range(cliff,len(nums))):
            if(nums[x]>nums[cliff-1]):
                nums[cliff-1],nums[x]=nums[x],nums[cliff-1];
                nums[cliff:]=sorted(nums[cliff:]);
                return;
instance=Solution();
nums=[1,2,3,6,4,7,5];
instance.nextPermutation(nums);
print nums;