class Solution:
    def isValid(self, s: str) -> bool:
        order = {"(":")", "{":"}", "[":"]"}
        values = []
        result = False
        for i in s:
            if i in order.keys():
                values.append(i)
            else:
                if len(values) == 0:
                    return False
                else:
                    if order[values[-1]] == i:
                        values.pop()
                    else: 
                        return False
        if len(values) != 0:
            return False
        return True
                