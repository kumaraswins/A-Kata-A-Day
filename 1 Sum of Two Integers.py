# add two numbers
# without using arithmetic operator
def Add(x, y):
    while (y != 0):
        carry = x & y
        x = x ^ y         
        y = carry << 1
    return x
print(Add(15, 30))
 