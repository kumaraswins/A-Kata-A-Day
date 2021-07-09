"""
Catching Car Mileage Numbers
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting
 number coming up, he notices and then promptly forgets. Who doesn't like catching those
  one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked into his car's 
computer, and we have a box hooked up that reads mileage numbers. We've got a box glued
 to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that
 parses the mileage number input, and returns a 2 if the number is "interesting
 " (see below), a 1 if an interesting number occurs within the next two miles,
  or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

So, you should expect these inputs and outputs:

# "boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0

# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2

# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2
"""
from functools import reduce

def checkAscendingDescending(num):
    ascending = "1234567890"
    return True if num in ascending  else False

def checkDescending(num):
    dscending = "9876543210"
    return True if  str(num) in dscending else False

def checkPalindrome(number):
    return str(number) == str(number)[::-1]

def checkSameDigit(number):
    numberList = list(str(number))
    return numberList.count(numberList[0]) == len(str(number))

def checZeros(number):
    numberList = list(str(number))
    for n in numberList[1:]:
        if n != str(0): return False
    return True

def awesome(number,awesome):
    for k in awesome:
        if number == str(k):
            return True
    return False

def is_interesting(number, awesome_phrases):
        print("--------------- number", number)
        print("checkPalindrome",checkPalindrome(str(number)))
        print("checkAscendingDescending",checkAscendingDescending(str(number)))
        print("checkDescending",checkDescending(str(number)))
        print("awesome",awesome(str(number), awesome_phrases))
        print("checkSameDigit",checkSameDigit(str(number)))
        print("checZeros",checZeros(str(number)))
        
    

if __name__ == "__main__":
    tests = [
        {'n': 3, 'interesting': [1337, 256], 'expected': 0},
        {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
        {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
        {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
        {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
        {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
    ]
    for t in tests:
        is_interesting(t['n'], t['interesting'])
