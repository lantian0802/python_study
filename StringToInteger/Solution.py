__author__ = 'jianying.wcj'
class Solution:
    #@return an integer
    def atoi(self,str):
        value=str.strip()
        if not value:
            return 0
        strSeq = list(value)
        result = []
        sign = 1
        signCount=0
        vzFlag = -1

        for item in strSeq:
            if(item == '+'):
                sign = 1
                signCount += 1
                continue
            if(item == '-'):
                sign = -1
                signCount += 1
                continue
            if(item < '0' or item >'9'):
                break
            if(item == '0' and vzFlag < 0):
                continue
            result.append(item)
            if(len(result) > 0) :
                vzFlag = 1
        if(signCount > 1):
            return 0
        if(len(result) < 1):
            return 0
        max = 0x7fffffff
        min = 0x80000000
        resValue = int("".join(result))
        if(sign > 0 and (resValue >= max or resValue < 0)):
                resValue = max
        if(sign < 0 and (resValue > max or resValue < 0)):
                resValue = min
        return resValue * sign


if __name__ == "__main__":
    s = Solution()
    print(s.atoi("2147483648"))