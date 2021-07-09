#You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. The array is either entirely comprised of odd integers or entirely
#  comprised of even integers except for a single integer N. Write a method that takes the 
# array as an argument and returns this "outlier" N.
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

def find_outlier(integers):
    temp = [ i%2 for i in integers]
    m = 1 if temp.count(1) > temp.count(0) else  0
    return (integers[(temp.index(m))])        
find_outlier([2, 4, 6, 8, 10, 3])
