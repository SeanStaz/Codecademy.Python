#Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

#For example: anti_vowel("Hey You!") should return "Hy Y!".

    #Don't count Y as a vowel.
    #Make sure to remove lowercase and uppercase vowels.


def anti_vowel(text):
    s = ""
    for c in text:
        if type(c) is str:
            d = c.lower()
            if d != 'a' and d != 'e' and d != 'i' and d != 'o' and d != 'u':
                s = s + c
        else:
            s = s + c
    return s
