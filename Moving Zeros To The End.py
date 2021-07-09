"""
Write an algorithm that takes an array and moves 
all of the zeros to the end, preserving the order of the other elements
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""
def move_zeros(array):
    n = array.count(0)
    res = []
    new =[]
    zero =[]

    for i in range(len(array)):
        if array[i] != 0:
            new.append(array[i])
            res.append(array[i])
        else:
            zero.append(0)

    for k in range(n):
        res.append(0)
    new.extend(zero)
    
    return res



print(move_zeros([1, 0, 1, 2, 0, 1, 3]))