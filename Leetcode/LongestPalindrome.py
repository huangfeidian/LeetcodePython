from string import join
from string import replace
class Solution(object):
    def manacher(self,s):

        #global center;
        #global end;
        length=len(s);
        rad=[0]*length;
       # global width;
        width=0;
        center=1;
        max_length=0;
        max_center=0;
        while(center<length):
            while(center-width-1>=0 and center+width+1<length and s[center-width-1]==s[center+width+1]):
                width+=1;
            rad[center]=width;
            if(width>max_length):
                max_length=width;
                max_center=center;
            global k ;
            k=1;
            while(k<=rad[center] and rad[center-k]!=rad[center]-k):
                rad[center+k]=min(rad[center-k],rad[center]-k);
                k+=1;
            width=max(width-k,0);
            center+=k;
        return s[max_center-max_length:max_center+max_length+1];


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s="#"+join(s,"#")+"#";
        temp_result=self.manacher(new_s);
        return replace(temp_result,"#","");
instance =Solution();
print instance.longestPalindrome("walawalawa");
