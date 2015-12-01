class Solution1:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1,i+1);
            dict[x] = i
        

class Solution2:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index = []
        numtosort = num[:]; numtosort.sort()
        i = 0; j = len(numtosort) - 1
        while i < j:
            if numtosort[i] + numtosort[j] == target:
                for k in range(0,len(num)):
                    if num[k] == numtosort[i]:
                        index.append(k)
                        break
                for k in range(len(num)-1,-1,-1):
                    if num[k] == numtosort[j]:
                        index.append(k)
                        break
                index.sort()
                break
            elif numtosort[i] + numtosort[j] < target:
                i = i + 1
            elif numtosort[i] + numtosort[j] > target:
                j = j - 1

        return (index[0]+1,index[1]+1)
class Solution3:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        value_index=zip(num,range(1,len(num)+1))
        index = []
        value_index.sort()
        i = 0; j = len(value_index) - 1
        while i < j:
            if value_index[i][0] + value_index[j][0] == target:
               if value_index[i][1]>value_index[j][1]:
                   return (value_index[j][1],value_index[i][1])
               else:
                   return (value_index[i][1],value_index[j][1])
            else:
               if value_index[i][0] + value_index[j][0] < target:
                  i = i + 1
               else :
                  j = j - 1

instance=Solution3()
num=[1,2,3,4,5,6,7,8,9,0]
#value_index=zip(num,range(1,len(num)+1))
#value_index.sort()
#print value_index
target=8
print instance.twoSum(num,target)
#for x in {x for x in instance.twoSum(num,target) if x[0]<x[1]}:

#     print x    