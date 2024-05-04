# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/submissions/1217122235/
from queue import Queue  
from typing import List  

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        frequency_map = {element: students.count(element) for element in students}  

        stud_queue = Queue()
        for element in sandwiches:
            stud_queue.put(element)

        
        while not stud_queue.empty():  
            var = stud_queue.get()
            if frequency_map.get(var,0)!=0:
                frequency_map[var]-=1
            else:
                return stud_queue.qsize()+1
        return 0
    
solution = Solution()
print(solution.countStudents([1,1], [0,1]))
  
        