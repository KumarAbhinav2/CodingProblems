class Solution:

    def closestPerson_intuitive(self, seats):
        # Iterate from left and keep on updating the closest person from left
        # Iterate from right and keep on upadting the closest person from right
        n = len(seats)
        left = [n]*n
        right = [n]*n

        for i in range(len(seats)):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1]+1

        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n - 1:
                right[i] = right[i+1]+1

        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if not seat)

    # time: O(N)
    # space: O(N)

    def closestPerson_better(self, seats):
        # two pointers to keep updating the nearest left and right closest person at each seat location

        ans = 0
        person = (i for i, seat in enumerate(seats) if seat)
        prev, upnext = None, next(person)

        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while upnext is not None and upnext < i:
                    upnext = next(person, None)
            left = float('inf') if prev is None else i - prev
            right = float('inf') if upnext is None else upnext - i

            ans = max(ans, min(left, right))

        return ans

        # time: O(N)
        # space: O(1)



obj = Solution()
print(obj.closestPerson_intuitive([1,0,0,0,1,0,0,0]))

