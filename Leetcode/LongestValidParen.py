class Solution(object):
    def longestValidParentheses(self, str):
        """
        :type s: str
        :rtype: int
        """
        s=[")"]+list(str);
        dp=[0 for i in range(len(s))];
        for index,char in enumerate(s):
            if(char==')'):
                if(index==0):
                    dp[index]=0;
                    continue;
                if(s[index-1]=="("):
                    dp[index]=2+dp[index-1];
                else:
                    match_index=index-dp[index-1]-1;
                    if(s[match_index]=="("):
                        dp[index]=2+dp[index-1]+dp[index-dp[index-1]-1];
                    else:
                        dp[index]=0;
            else:
                if(s[index-1]==")"):
                    dp[index]=dp[index-1];
                else:
                    dp[index]=0;
        return max(dp);

instance=Solution();
print instance.longestValidParentheses(")()())");
