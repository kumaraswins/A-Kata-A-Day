# Duplicate Encoder
#The goal of this exercise is to convert a string to a new string where
#  each character in the new string is "(" if that character appears 
# only once in the original string, or ")" if that character appears more than once in the 
# original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(text):
    textArray = text.lower()
    return "".join("(" if textArray.count(x) == 1 else ")" for x in textArray  )
    # for char in range(len(textArray)):
    #     out += "(" if textArray.count(textArray[char].lower()) == 1  else ")"
    # return out

print(duplicate_encode("recede"))