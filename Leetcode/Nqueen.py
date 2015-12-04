from string import join
class Solution(object):
    def __init__(self):
        self.result=[];
        self.stack=[];
    def queen_dfs(self,row,left,right,n):
        mask=(1<<n)-1;
        if(row==mask):
            self.result.append(self.stack[:]);
            return;
        used=left|right|row;
        avail=used^mask;
        temp_row=["." for i in range(n)];
        s=0;
        while(avail):
            right_most=avail&((~avail)+1);
            while((1<<s)!=right_most):
                s+=1;
            temp_row[n-s-1]="Q";
            self.stack.append(join(temp_row,""));
            avail=avail-right_most;
            self.queen_dfs(row|right_most,((left|right_most)>>1)&mask,((right|right_most)<<1)&mask,n);
            temp_row[n-s-1]=".";
            self.stack.pop();

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        used=0;
        left=right=0;
        self.queen_dfs(used,left,right,n);
        return self.result;
class Solution2(object):
    def __init__(self):
        self.count=0;
    def queen_dfs(self,row,left,right,n):
        mask=(1<<n)-1;
        if(row==mask):
            self.count+=1;
            return;
        used=left|right|row;
        avail=used^mask;
        s=0;
        while(avail):
            right_most=avail&((~avail)+1);
            while((1<<s)!=right_most):
                s+=1;
            avail=avail-right_most;
            self.queen_dfs(row|right_most,((left|right_most)>>1)&mask,((right|right_most)<<1)&mask,n);

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        used=0;
        left=right=0;
        self.queen_dfs(used,left,right,n);
        return self.count;




instance=Solution2();
print instance.totalNQueens(4);