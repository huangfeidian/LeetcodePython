class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums=map(lambda x:x-1,nums);
        length=len(nums);
        for i in range(length):
            while(nums[i]!=i and nums[i]>=0 and nums[i] <length and nums[i]!=nums[nums[i]]\
                ):
                temp=nums[nums[i]];
                nums[nums[i]]=nums[i];
                nums[i]=temp;
               # nums[i],nums[nums[i]]=nums[nums[i]],nums[i];
        for i in range(length):
            if(nums[i]!=i):
                return i+1;
        return length+1;
          
instance=Solution();
print instance.firstMissingPositive([-10,-3,-100,-1000,-239,1]);