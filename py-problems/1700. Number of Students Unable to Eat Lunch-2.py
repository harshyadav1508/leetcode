# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches:
            if sandwiches[0] in students:
                students.remove(sandwiches[0])
                sandwiches.pop(0)
            else:
                return len(students)

        return 0
        