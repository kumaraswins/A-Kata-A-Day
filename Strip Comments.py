"""
Complete the solution so that it strips all text that follows any of a 
set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
"""

def solution1(string,markers):
    stringlist = list(string)
    out = []
    add = True
    for i in stringlist:
        if i in markers:
            add=False
        if add == True:
            out.append(i)
        if i =="\n" and add==False: 
            out.append("\n")
            add= True
            
    return "".join(out).replace(" \n", "\n").rstrip(" ")

def solution(string, markers):
    lines = string.split("\n")
    for i, line in enumerate(lines):
        for marker in markers:
            index =  line.find(marker)
            if index != -1:
                line = line[:index]
                print(line)
        lines[i] = line.strip(" ")
    return "\n".join(lines)


result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
#print(result)
print("out",  "apples, pears\\ngrapes\\nbananas")
