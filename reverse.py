#Define a function called reverse that takes a string textand returns that string in reverse.

#For example: reverse("abcd") should return "dcba".

    #You may not use reversed or [::-1] to help you with this.
    #You may get a string containing special characters (for example, !, @, or #).

def reverse(text):
    string = ""
    l = len(text)
    while l > 0:
        string += text[l-1]
        l -= 1
    return string

print (reverse("car"))
