class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        int_max=2147483647;
        int_min=-2147483648;
        result=0;
        carry=1;
       
        if(divisor==1):
            return dividend;
        if(divisor==-1):
            if(dividend==int_min):
                return int_max;
            else:
                return -1*dividend;
        if((dividend<0)^(divisor<0)):
            sign=-1;
        else:
            sign=1;
        dividend=abs(dividend);
        divisor=abs(divisor);
        new_divisor=divisor;
        while(new_divisor<=dividend):
            new_divisor=new_divisor<<1;
            carry=carry<<1;
        carry>>=1;
        new_divisor>>=1;
        while(dividend>=divisor):
            if(dividend>=new_divisor):
                dividend-=new_divisor;
                result+=carry;
            carry>>=1;
            new_divisor>>=1;
        return result*sign;
instance =Solution();
print instance.divide(10,-3);