class Solution:
    # @param A : string
    # @return an integer
    def intuitive(self, A):
        n = len(A)
        end = n-1
        if not A:
            return 0
        if n == 1:
            return 1
        res = 0
        while A[end] == ' ':
            end -=1
        for i in range(end, -1, -1):
            if i != ' ':
                res +=1
            break
        return len(res)
