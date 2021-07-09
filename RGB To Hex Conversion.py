"""
RGB To Hex Conversion
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result 
in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255.
 Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""
def getVal(r):
    out = ''
    if r <= 0 :
        out = "00"
    elif r >=255:
        out = "FF" 
    else:
        out = hex(r)[-2:]
    return out.upper().replace('x', "0")

def rgb(r, g, b):
    return "{}{}{}".format(getVal(r),getVal(g),getVal(b))
def getVal(r):
    return 0 if r <=0  else r if r >=255 255

def rgb2(r,g,b):
    return "{}{}{}".format(format(r,'02x'),format(g,'02x'),format(b,'02x'))

def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


# def rgb(r, g, b):
#     return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))

print(rgb(148, 0, 211))
print(rgb(255, 255, 255))
#print(rgb(255, 255, 300))
print(rgb(1,2,3))