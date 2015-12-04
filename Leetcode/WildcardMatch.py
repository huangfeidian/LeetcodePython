class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    # @good solution! use 'aaaabaaaab' vs 'a*b*b' as an example
    def isMatch(self, s, p):
        pPointer=sPointer=ss=0; star=-1
        while sPointer<len(s):
            if pPointer<len(p) and (s[sPointer]==p[pPointer] or p[pPointer]=='?'):
                sPointer+=1; pPointer+=1
                continue
            if pPointer<len(p) and p[pPointer]=='*':
                star=pPointer; pPointer+=1; ss=sPointer;
                continue
            if star!=-1:
                pPointer=star+1; ss+=1; sPointer=ss
                continue
            return False
        while pPointer<len(p) and p[pPointer]=='*':
            pPointer+=1
        if pPointer==len(p): return True
        return False
class Solution2:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    # @good solution! use 'aaaabaaaab' vs 'a*b*b' as an example
    def short(self,p):
        result=[];
        if(len(p)==0):
            return result;
        pre=p[0];
        for i in range(1,len(p)):
            if(pre=="*" and p[i]=="*"):
                continue;
            resull.append(pre);
            pre=p[i];
        return result;
    def isMatch2(self, s, p):
        lens=len(s);
        lenp=len(p);
        if(lens==0):
            for i in range(lenp):
                if(p[i]!="*"):
                    return False;
            return True;
        if(lenp==0):
            return False;
        s_index=0;
        p_index=0;
        while(s_index!=lens and p_index!=lenp):
            if(s[s_index]==p[p_index] or p[p_index]=="?"):
                s_index+=1;
                p_index+=1;
                continue;
            if(p[p_index]=="*"):
                for j in range(s_index,lens+1):
                    if(self.isMatch2(s[j:],p[p_index+1:])):
                       return True;
                return False;
            return False;
        if(s_index!=lens):
            return False;
        if(p_index!=lenp):
            return self.isMatch2("",p[p_index:]);
        return True;
    def isMatch(self,s,p):
        p=self.short(p);
        return self.isMatch2(s,p);
instance=Solution2();
print instance.isMatch2("a","aa");

