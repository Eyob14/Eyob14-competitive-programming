#User function Template for python3

class Solution: 
    def select(self, arr, i):
        position = None
        for i in range(i, len(arr)):
            if (position is None) or (arr[i] < arr[position]):
                position = i
        return position
    
    def selectionSort(self, arr,n):
        for i in range(n):
            position = self.select(arr, i)
            temp = arr.pop(position)
            arr.insert(i, temp)
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends