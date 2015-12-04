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
            return False;
        for x in reversed(range(cliff,len(nums))):
            if(nums[x]>nums[cliff-1]):
                nums[cliff-1],nums[x]=nums[x],nums[cliff-1];
                nums[cliff:]=sorted(nums[cliff:]);
                return True;
    def permuteUnique(self, num):
        num.sort();
        result=[];
        result.append(num[:]);
        while(self.nextPermutation(num)):
            result.append(num[:]);
        return result;
instance=Solution();
print instance.permuteUnique([1,1,2]);