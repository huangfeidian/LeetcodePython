from string import join
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows<=1):
            return s;
        str_vec=["",]*numRows;
        for index,char in enumerate(s):
            remain=index%(2*numRows-2);
            if(remain<numRows):
                str_vec[remain]+=char;
            else:
                str_vec[2*numRows-2-remain]+=char;
        return join(str_vec,"");

instance=Solution();
print instance.convert("PAYPALISHIRING", 3)