class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result="1";
        for i in range(n-1):
            pre=result[0];
            temp_result="";
            count=1;
            for j in range(1,len(result)):
                if(result[j]==pre):
                    count+=1;
                else:
                    temp_result+=(str(count)+str(pre));
                    pre=result[j];
                    count=1;
            temp_result+=(str(count)+str(pre));
            count=1;
            result=temp_result;
        return result;
          
instance=Solution();
print instance.countAndSay(3);