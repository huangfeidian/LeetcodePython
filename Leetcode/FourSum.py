class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        numLen, res, dict = len(num), set(), {}
        if numLen < 4: return []
        num.sort()
        for p in range(numLen):
            for q in range(p+1, numLen): 
                if num[p]+num[q] not in dict:
                    dict[num[p]+num[q]] = [(p,q)]
                else:
                    dict[num[p]+num[q]].append((p,q))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target-num[i]-num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j: res.add((num[i],num[j],num[k[0]],num[k[1]]))
        return [list(i) for i in res]

class Solution2(object):
    def twoSum(self,nums,left,right,target):
        result=[];
        while(left<right):
            if(nums[left]+nums[right]==target):
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
                for j in temp_result:
                    result.append([nums[i],j[0],j[1]]);
        return result;
    def fourSumHehe(self,nums,left,right,target):
        result=[];
        for i in range(left,right-2):
            temp_result=self.threeSumHehe(nums,i+1,right,target-nums[i]);
            if(temp_result):
                for j in temp_result:
                    result.append([nums[i],j[0],j[1],j[2]]);
        return result;
    def fourSum(self,nums,target):
        nums.sort();
        temp_result=self.fourSumHehe(nums,0,len(nums)-1,target);
        result=[];
        for k in temp_result:
            if k not in result:
                result.append(k);
        return result;
    def threeSum(self,nums):
        nums.sort();
        return self.threeSumHehe(nums,0,len(nums)-1,0);
       
instance=Solution();
print instance.fourSum([-2,0,1,0,-1,2],0);


