"""
Write Number in Expanded Form.py

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""

def expanded_form(num):
    l = len(str(num))-1
    li = list(str(num))
    out = ''
    for i in ((range(len(str(num))))):
        mod = int(li[i])  * (int(10**l))
        
        out += str(mod)+ " + " if mod !=0  else ""
        l-=1
    
    return out.strip(" + ")
    
print(expanded_form(70304))