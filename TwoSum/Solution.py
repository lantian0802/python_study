__author__ = 'jianying.wcj'
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index1 = 0
        index2 = 0
        numMap = {}
        length = len(num)
        for i in range(0,length):
            numMap[num[i]] = i
        for j in range(0,length):
            #dict[key]的方式，也可以是dict.get(key)
            res = numMap.get(target-num[j])
            if(res is not None and res != j):
                index1 = res
                index2 = j
                break
        if(index1 > index2):
            return (index2+1,index1+1)
        else:
            return (index1+1,index2+1)

if __name__=="__main__":
    s = Solution()
    numbers=[5,75,25]
    target=100
    print(s.twoSum(numbers,target))