class Solution(object):
    def recur_sum(self,candidates,target):
            if(not candidates):
                return [];
            if(target<candidates[0]):
                return [];
            result=[];
            for i in range(target/candidates[0]+1):
                pre_result=[ candidates[0] for j in range(i)];
                if(target-i*candidates[0]==0):
                    result.append(pre_result);
                    break;
                temp_result= self.recur_sum(candidates[1:],target-i*candidates[0]);
                if(temp_result):
                    
                    for j in temp_result:
                        result.append(pre_result+j);
            return result;
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort();
        
        return self.recur_sum(candidates,target);
class Solution2(object):
    def recur_sum2(self,candidates,target):
            if(not candidates):
                return [];
            if(target<candidates[0]):
                return [];
            if(target==candidates[0]):
                return [[candidates[0]],];
            result=[];
            zero_result=self.recur_sum2(candidates[1:],target);
            for x in zero_result:
                result.append(x);
            one_result=self.recur_sum2(candidates[1:],target-candidates[0]);
            pre_result=[candidates[0]];
            for i in one_result:
                result.append(pre_result+i);
            return result;
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort();
        
        temp_result=self.recur_sum2(candidates,target);    
        temp_result.sort();
        return temp_result[0:self.removeDuplicates(temp_result)];
          
instance=Solution2();
print instance.combinationSum2([10,1,2,7,6,1,5],8);