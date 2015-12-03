class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_short=len(needle);
        length_long=len(haystack);
        if(length_short>length_long):
            return -1;
        for i in range(length_long-length_short+1):
            if(haystack[i:i+length_short]==needle):
                return i;
        return -1;