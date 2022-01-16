class Solution:
    def scheduleCourse(self, courses) -> int:
        courses = sorted(courses, key=lambda x: (x[1], x[0]))
        max_courses = 0
        total_duration = 0
        stack = []
        for course in courses:
            total_duration += course[0]
            if total_duration <= course[1]:
                max_courses +=1
        return max_courses


obj = Solution()
print(obj.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]))
print(obj.scheduleCourse([[1,2]]))
print(obj.scheduleCourse([[3,2],[4,3]]))
print(obj.scheduleCourse([[5,5],[4,6],[2,6]]))