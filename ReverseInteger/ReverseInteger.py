__author__ = 'jianying.wcj'
class Solution:
    # @return an integer
    def reverse(self, x):
        max = 0x7fffffff
        min = 0x80000000
        sign = 1
        result = 0
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            result = result * 10 + x % 10
            if(result > max | result < min):
                if(result > max):
                    result = max
                else:
                    result = min
            x = (int)(x/10)
        return sign * result

if __name__=="__main__":
    # 生命对象的时候要加上括号，否则只是声明了一个别名
    s = Solution()
    print(str(s.reverse(-83943)))