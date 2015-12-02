from string import strip
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max=2147483647;
        int_min=-2147483648;
        new_str=strip(str);
        sign=1;
        i=0;
        if(len(str)==0):
            return 0;
        if(new_str[0]=="-" or new_str[0]=="+"):
            i=1;
        if(i==1 and new_str[0]=="-"):
            sign=-1;

        total=0;
        while(i<len(new_str)):
            if(new_str[i]<"0" or new_str[i]>"9"):
                return sign*total;
            total=total*10+int(new_str[i]);
            if(total>int_max):
                if(sign==1):
                    return int_max;
                else:
                    return int_min;
            i+=1;
        return sign*total;
instance=Solution();
print instance.myAtoi("-2147483648");
