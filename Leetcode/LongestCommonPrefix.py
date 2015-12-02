class Solution(object):
    def common (self,str1,str2):
        len_min=min(len(str1),len(str2));
        for i in range(len_min):
            if(str1[i]!=str2[i]):
                return str1[0:i];
        return str1[0:len_min];
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(not strs):
            return "";

        common_str=strs[0][:];
        for i in strs:
            common_str=self.common(common_str,i);
        return common_str;
        