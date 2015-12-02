class Solution:
    # @return a tuple, (index1, index2)
    def twoSumClosest(self, num, target):
        left=0;
        right=len(num)-1;
        total=num[0]+num[1];
        result_left=0;
        result_right=1;
        while(left<right):
            if(abs(target-total)>abs(num[left]+num[right]-target)):
                total=num[left]+num[right];
                result_left=left;
                result_right=right;
            if(num[left]+num[right]<target):
                left+=1;
            else:
                right-=1;
        return (result_left,result_right);
instance=Solution();
print instance.twoSumClosest([0,1,2,3,4,5,6],8);
