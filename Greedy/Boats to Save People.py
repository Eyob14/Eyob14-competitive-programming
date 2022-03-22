class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        counter = 0
        start = 0
        end = len(people) - 1
        # mid = start + (end - start)//2
        while start <= end:
            if people[end] + people[start] <= limit:
                counter += 1
                end -= 1
                start += 1
            elif not(people[end] + people[start] <= limit) and people[end] <= limit:
                counter += 1
                end -= 1
        return counter
            
