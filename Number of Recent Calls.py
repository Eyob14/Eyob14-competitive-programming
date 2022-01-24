class RecentCounter:

    def __init__(self):
        self.requests = deque()
 
    def ping(self, t: int) -> int:
        self.requests.append(t)
        count = 0
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
r = RecentCounter()
print(r.ping(100))
