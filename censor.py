#Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks. 

def censor(text, word):
    index = text.index(word)
    l = len(word)
    text = str.replace(text, word, '*' * l)
    return text
