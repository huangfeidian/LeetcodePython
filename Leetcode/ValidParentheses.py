class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        content=[];
        for c in s:
            if(c=='(' or c=='{' or c=="["):
                content.append(c);
            else:
                if(not content):
                    return False;
                if( c==")"):
                    if(content[-1]!="("):
                        return False;
                    else:
                        content.pop();
                        continue;
                if( c=="]"):
                    if(content[-1]!="["):
                        return False;
                    else:
                        content.pop();
                        continue;
                if( c=="}"):
                    if(content[-1]!="{"):
                        return False;
                    else:
                        content.pop();
                        continue;
        if(content):
            return False;
        else:
            return True;