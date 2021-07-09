#Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.


def pig_it(sentence):
    text  =  sentence.split(" ")    
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
    new  = []
    for i in range(len(text)):
        #print(text[i])
        
        if  text[i] in alpha and len(text[i]) == 1:
            text[i] = text[i]+"ay"

        elif len(text[i]) >= 2:
            print(text[i])
            text[i] =  text[i][1:-1] + text[i][-1] + text[i][0]+"ay"
        else:
            text[i] = text[i]
        new.append(text[i])
    return " ".join(new)




sentence = "Pig latin is cool"
text =  sentence.split(" ")
alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
new =[]
for i in range(len(text)):
    if text[i] in alpha and len(text[i]) == 1:
        text[i] = text[i] + "ay"
    elif len(text[i]) >= 2:
        text[i] = text[i][1:-1] + text[i][-1] + text[i][0]+ "ay"
    else:text[i] = text[i]
    new.append(text[i])
print(" ".join(new))

