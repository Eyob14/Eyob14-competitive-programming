from ast import List


def minJumps(arr):
    last_element = arr[-1]
    new_arr = []
    for i in arr:
        if i not in new_arr and i != last_element:
            new_arr.append(i)
    new_arr.append(last_element)
    print(new_arr, last_element)
    if len(arr) == 1:
        return 0
    elif arr[0] == arr[len(arr)-1]:
        return 1
    else:
        index = new_arr.index(arr[-1])
        return len(new_arr[:index])
arr = [100,-23,-23,404,100,23,23,23,3,404]
print(minJumps([11,22,7,7,7,7,7,7,7,22,13]))
print(minJumps(arr)) 
arr = [7]
print(minJumps(arr)) 
arr = [7,6,9,6,9,6,9,7]
print(minJumps(arr)) 