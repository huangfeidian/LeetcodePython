class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[["",]];
        for i in range(1,n+1):
            temp_result=[];
            for j in range(0,i):
                for k in result[j]:
                   for  v in result[i-j-1]:
                        temp_result.append("("+k+")"+v);
            result.append(temp_result);
        return result[n];
instance =Solution();
print instance.generateParenthesis(1);
