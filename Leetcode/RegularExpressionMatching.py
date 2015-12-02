class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if(len(p)==0):
            return not s;
        if(len(p)==1):
            if (len(s)==1):
                if(p[0]=="."):
                    return True;
                else:
                    return s[0]==p[0];
            else:
                return False;
        if(p[0]=="."):
            if(p[1]=="*"):
                for i in range(len(s)+1):
                    if(self.isMatch(s[i:],p[2:])):
                       return True;
                    else:
                       continue;
                return False;
            else:
                return (self.isMatch(s[1:],p[1:]));
        else:
            if(p[1]=="*"):
                if(self.isMatch(s,p[2:])):
                    return True;
                for i in range(len(s)):
                    if(s[i]==p[0]):
                        if(self.isMatch(s[i+1:],p[2:])):
                            return True;
                    else:
                       break;
                return False;
            else:
                return (p[0]==s[0] and self.isMatch(s[1:],p[1:]));
instance =Solution();
print instance.isMatch("aab", "c*a*b");



            
        

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]

            
        