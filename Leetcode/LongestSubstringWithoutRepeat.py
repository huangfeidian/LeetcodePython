class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={};
        global begin;
        global length;
        begin=0;
        length=0;
        for index,char in enumerate(s):

            if(char in dict):
                length=max((index-begin),length);
                begin=max(dict[char]+1,begin);
            dict[char]=index;
        length=max(len(s)-begin,length);
        return length;
instance=Solution();
print instance.lengthOfLongestSubstring("abba")