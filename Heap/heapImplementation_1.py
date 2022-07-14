# User function Template for python3

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # code here
        leftChild = self.leftChild(i)
        rightChild = self.rightChild(i)

        minimum = i

        if leftChild <= n-1 and arr[leftChild] > arr[minimum]:
            minimum = leftChild

        if rightChild <= n-1 and arr[rightChild] > arr[minimum]:
            minimum = rightChild

        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]

            self.heapify(arr, n, minimum)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # code here
        for i in range((n-1), -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.

    def HeapSort(self, arr, n):
        # code here
        self.buildHeap(arr, n)

        for i in range(n):

            arr[n-1-i], arr[0] = arr[0], arr[n-1-i]

            self.heapify(arr, n-1-i, 0)

    # Function to get parent

    def getParent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        left_index = 2 * i + 1
        return left_index

    def rightChild(self, i):
        right_index = 2 * i + 2
        return right_index

    # Function to get maximum
    def getMax(self, arr):
        return arr[0]

    # Function to get left child


s = Solution()
arr = [10,9,8,7,6,5,4,3,2,1]
s.HeapSort(arr, 10)
print(arr)
