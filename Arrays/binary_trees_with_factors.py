class Solution:
    def numFactoredBinaryTrees(self, arr) -> int:
        arr.sort(reverse=True)
        res_set = len(arr)

        def get_binary(target, arr):
            if not arr:return 0
            if len(arr) == 1:
                return 1 if arr[0]**2 == target else 0
            mymap = set()
            for val in arr:
                if target / val in mymap:
                    return len(set([target/val, val]))
                mymap.add(val)
            return 0

        for i in range(len(arr)):
            res_set += get_binary(arr[i], arr[i+1:])
        return res_set


obj = Solution()
print(obj.numFactoredBinaryTrees([2, 4]))
#print(obj.numFactoredBinaryTrees([2, 4, 5, 10]))
#print(obj.numFactoredBinaryTrees([5, 19, 15, 10]))