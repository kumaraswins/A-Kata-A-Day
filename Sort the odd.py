"""
#Sort the odd
---

You will be given an array of numbers. You have to sort the odd numbers in ascending order while
leaving the even numbers at their original positions.

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""
def sort_array(source_array):
    odd  = sorted([i for i in source_array if i%2 !=0])
    res =[]
    c=0
    for i in range(len(source_array)):
        if source_array[i] %2 !=0:
            res.append(odd[c])
            c+=1
        else:
            res.append(source_array[i])
    return res

print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0] ))