__author__ = 'jianying.wcj'
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if(m == 0):
            return B
        if(n == 0):
            return A
        C = []
        i1 = 0
        i2 = 0
        while(True):
           if(i1 < m and i2 < n):
               if(A[i1] <= B[i2]):
                   C.append(A[i1])
                   i1 += 1
               else:
                   C.append(B[i2])
                   i2 += 1
           if(i1 >= m and i2 <= n):
               C.extend(B[i2:n])
               break
           if(i2 >= n and i1 < m):
               C.append(A[i1:m])
               break
        return C

if __name__=="__main__":
    s = Solution()
    A=[]
    B=[1]
    print(s.merge(A,len(A),B,len(B)))


