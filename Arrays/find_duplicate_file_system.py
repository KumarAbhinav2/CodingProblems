import collections
class Solution:
    def findDuplicate(self, paths):
        mmp = collections.defaultdict(list)
        for path in paths:
            d, *f = path.split(' ')
            s = [d+'/'+i for i in f]
            for p in s:
                v, k  = p.split('(')
                mmp[k].append(v)
        return [v for k,v in mmp.items() if len(v)>1]

        # Time: O(n*x) n string of length x
        # Space: O(n*x) n string of length x


obj = Solution()
print(obj.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
print(obj.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))