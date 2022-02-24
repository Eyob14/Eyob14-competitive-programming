import math
class Solution:
    def __init__(self, arr=[]):
        self.arr = arr
    def leftChild(self, index):
        if len(self.arr) > 1 and 2*index + 1 <= len(self.arr):
            return 2*index + 1
    def rightchild(self, index):
        if len(self.arr) > 2 and 2*index + 1 <= len(self.arr):
            return 2*index + 2
    def parent(self, index):
        if len(self.arr) > 1 and math.floor((index-1)/2) >= 0:
            return math.floor((index-1)/2)
    def insert(self, value):
        self.arr.append(value)
        for i in range(len(self.arr)):
            curr = self.arr.index(value)
            if self.parent(curr) != None:
                parent = self.parent(curr)
                if self.arr[parent] > self.arr[curr] and (curr > 0):
                    self.arr[parent], self.arr[curr] = self.arr[curr], self.arr[parent] 
        return self.arr
    def remove(self, index):
        if index != len(self.arr) -1: 
            lastValue = self.arr[-1]
            self.arr[-1], self.arr[index] = self.arr[index], self.arr[-1]
            self.arr.pop()
            if (self.rightchild(index) != None) and (self.leftChild(index) != None) and (self.parent(index) != None):
                left = self.leftChild(index)
                right = self.rightchild(index)
                changed = left if self.arr[left] < self.arr[right] else right
                parent = self.parent(index)
            if self.arr[parent] > self.arr[index]:
                for i in range(len(self.arr)):
                    parent = self.parent(index)
                    if self.arr[parent] > self.arr[index] and (index > 0):
                        self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            else:
                for i in range(len(self.arr)):
                    if (self.rightchild(index) != None) and self.leftChild(index) != None:
                        left = self.leftChild(index)
                        right = self.rightchild(index)
                        changed = left if self.arr[left] < self.arr[right] else right
                        if self.arr[index] > self.arr[changed] and (index < len(self.arr)-1):
                            self.arr[index], self.arr[changed] = self.arr[changed], self.arr[index]
                    elif self.leftChild(index) != None:
                        left = self.leftChild(index)
                        if self.arr[index] > self.arr[left] and (index < len(self.arr)-1):
                            self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
        else:
            self.arr.pop()  
        return self.arr
    def getMin(self):
        if self.arr:
            return self.arr[0]
    def update(self, index, value):
        self.arr[index] = value
        if (self.rightchild(index) != None) and (self.leftChild(index) != None) and (self.parent(index) != None):
            left = self.leftChild(index)
            right = self.rightchild(index)
            changed = left if self.arr[left] < self.arr[right] else right
            parent = self.parent(index)
            if self.arr[parent] > self.arr[index]:
                for i in range(len(self.arr)):
                    parent = self.parent(index)
                    if self.arr[parent] > self.arr[index] and (index > 0):
                        self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            else:
                for i in range(len(self.arr)):
                    if (self.rightchild(index) != None) and self.leftChild(index) != None:
                        left = self.leftChild(index)
                        right = self.rightchild(index)
                        changed = left if self.arr[left] < self.arr[right] else right
                        if self.arr[index] > self.arr[changed] and (index < len(self.arr)-1):
                            self.arr[index], self.arr[changed] = self.arr[changed], self.arr[index]
                    elif self.leftChild(index) != None:
                        left = self.leftChild(index)
                        if self.arr[index] > self.arr[left] and (index < len(self.arr)-1):
                            self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
        return self.arr
    
s = Solution([0,4,1,8,107,5,2,100,20,177,144,70,80,3])
print(s.remove(3))


        