"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # goal: return the total importance value of THIS employee and all of its direct and 
        # indirect subordinates 

        # make a hashmap of employee id's --> (importance, subordinates)
        # do a dfs search to go through all employees starting with id 
        tracker = {} # id --> tuple(imp, subordinates)
        for employee in employees:
            tracker[employee.id] = (employee.importance, employee.subordinates)
        
        # made a graph 
        stack = deque([id]) # appendleft and pop left 
        
        importance  = 0
        while stack: 
            employee_id = stack.popleft() 
            imp, subordinates = tracker[employee_id]
            importance += imp
            # add all subordiantes to stack
            for sub in subordinates: 
                stack.appendleft(sub)
        return importance





        