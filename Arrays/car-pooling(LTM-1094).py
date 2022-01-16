class Solution:

    def carPooling(self, trips, capacity):
        # have a list of what happened at each drop and pisck up event
        events = []
        for trip in trips:
            events.append([trip[1], trip[0]])
            events.append([trip[2], -trip[0]])

        used_seats  = 0
        for event, passengers in events:
            used_seats+=passengers
            if used_seats > capacity:
                return False
        return True


