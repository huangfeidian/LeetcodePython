class Solution(object):

    def twoSumClosest(self, num,left,right, target):
        total=num[left]+num[left+1];
        result_left=left;
        result_right=left+1;
        while(left<right):
            if(abs(target-total)>abs(num[left]+num[right]-target)):
                total=num[left]+num[right];
                result_left=left;
                result_right=right;
            if(num[left]+num[right]==target):
                return (num[result_left],num[result_right]);
            if(num[left]+num[right]<target):
                left+=1;
            else:
                right-=1;
        return (num[result_left],num[result_right]);

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort();
        length=len(nums);
        result=[];
        differ=100000;
        if(length<3):
            return [];
        for i in range(length-2):
           temp_result=self.twoSumClosest(nums,i+1,length-1,target-nums[i]);
           new_differ=abs(target-nums[i]-temp_result[0]-temp_result[1]);
           if(differ>new_differ):
               differ=new_differ;
               result=[nums[i],temp_result[0],temp_result[1]];
           if(differ==0):
               return sum(result);
        return sum(result);
instance=Solution();
print instance.threeSumClosest([-1,2,1,-4],1);

