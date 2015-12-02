class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total_set=set();
        zero=0;
        negative={};
        nega_vec=[];
        posi_vec=[];
        positive={};
        double_set=set();
        for value in nums:
            total_set.add(value);
            if(value==0):
                zero+=1;
                continue;
            if(value<0):
                
                if(negative.has_key(value)):
                    negative[value]+=1;
                else:
                    negative[value]=1;
                    nega_vec.append(value);
            else:
                
                if(positive.has_key(value)):
                    positive[value]+=1;
                else:
                    positive[value]=1;
                    posi_vec.append(value);
        nega_vec.sort();
        posi_vec.sort();
        result=[];
        if(zero>0):
            if(zero>2):
                result.append([0,0,0]);
            for x in total_set:
                if(x<0 and -x in total_set):
                    result.append([x,0,-x]);
        posi_len=len(posi_vec);
        for i in range(posi_len-1):
            for j in range(i+1,posi_len):
                if(-(posi_vec[i]+posi_vec[j]) in total_set):
                    result.append([-(posi_vec[i]+posi_vec[j]),posi_vec[i],posi_vec[j]]);
        neg_len=len(nega_vec);
        for i in range(neg_len-1):
            for j in range(i+1,neg_len):
                if(-(nega_vec[i]+nega_vec[j]) in total_set):
                    result.append([nega_vec[i],nega_vec[j],-(nega_vec[i]+nega_vec[j])]);
        for i,j in positive.iteritems():
            if(j>1 and -2*i in total_set ):
                result.append([-2*i,i,i]);
        for i,j in negative.iteritems():
           if(j>1 and -2*i in total_set ):
                result.append([i,i,-2*i]);
        return result;
class Solution(object):
    def twoSum(self,nums,left,right,target):
        result=[];
        while(left<right):
            if(nums[left]+nums[right]==target):
                if([nums[left],nums[right]] not in result):
                    result.append([nums[left],nums[right]]);
                left+=1;
                right-=1;
                continue;
            if(nums[left]+nums[right]<target):
                left+=1;
            else:
                right-=1;
        return result;
    def threeSumHehe(self, nums,left,right,target):
        result=[];
        for i in range(left,right-1):
            temp_result=self.twoSum(nums,i+1,right,target-nums[i]);
            if(temp_result):
                for j in [[nums[i],k[0],k[1]] for k in temp_result]:
                    if(j not in result):
                        result.append(j);
        return result;
    def threeSum(self,nums):
        nums.sort();
        return self.threeSumHehe(nums,0,len(nums)-1,0);
       
instance=Solution();
print instance.threeSum([-2,0,1,1,2]);


