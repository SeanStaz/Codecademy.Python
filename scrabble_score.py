#Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.

    #Assume your input is only one word containing no spaces or punctuation.
    #As mentioned, no need to worry about score multipliers!
    #Your function should work even if the letters you get are uppercase, lowercase, or a mix.
    #Assume that you're only given non-empty strings.

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    total = 0
    for c in word:
        d = c.lower()
        total += score[d]
    return total
