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
        self.total_importance = 0
        def dfs(employee,employee_subordinates, visited, employee_importance):
            if len(employee_subordinates[employee]) == 0:
                visited.append(employee)
                self.total_importance += employee_importance[employee]
                print(self.total_importance)
            else:
                self.total_importance += employee_importance[employee]
                print(self.total_importance)
                visited.append(employee)
                for employee_id in employee_subordinates[employee]:
                    if employee_id in visited:
                        continue
                    dfs(employee_id, employee_subordinates, visited, employee_importance)
        
        employee_importance = {}
        employee_subordinates = {} 
        
        for employee in employees:
            employee_importance[employee.id] = employee.importance
            employee_subordinates[employee.id] = employee.subordinates
        
        
        visited = []
        dfs(id, employee_subordinates, visited, employee_importance)
        return self.total_importance
        
        
        
        
        
        
        
            