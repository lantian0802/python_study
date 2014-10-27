__author__ = 'jianying.wcj'
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        unmatch = []
        max = 0
        min = 0
        for str in list(s):
            if(str not in list("".join(dict))):
                return False
        for item in dict:
            if(max < len(item)):
                max = len(item)
            if(min > len(item)):
                min = len(item)
        return self.doWordBreak(s,dict,unmatch,max,min)

    # 具体处理业务的函数
    def doWordBreak(self,s,dict,unmatch,max,min):
        if(s in dict):
            return True
        if(s in unmatch):
            return False
        for i in range(0,len(s)-1):
            first = s[0:i+1]
            second = s[i+1:len(s)]
            if(self.doWordBreak(first,dict,unmatch,max,min)):
                if(len(first) > max or len(first) < min):
                    return False
                if(self.doWordBreak(second,dict,unmatch,max,min)):
                    return True
                else:
                    unmatch.append(second)
            else:
                unmatch.append(first)
            #if(first in dict and second in dict):
             #   return True
        return False




##  "a", []
if __name__=="__main__":
    sol = Solution()
    s = "a"
    dict = []
    print(sol.wordBreak(s,dict))

