n = int(input())
prices = list(map(int,input().split())) 
prices.sort()
q = int(input())
def forwardSearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left)//2
        if (nums[mid] > target):
            right = mid - 1
        elif (nums[mid] < target):
            left = mid + 1
        else:
            return mid
    return -1

for i in range(q):
    m = int(input())
    value = forwardSearch(prices, m)
    if value != -1:
        print(len(prices[:value+1]))
    else:
        print(0)

        
        