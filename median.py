#Instructions

#Write a function called median that takes a list as an input and returns the median value of the list.

#For example: median([1,1,2]) should return 1.

    #The list can be of any size and the numbers are not guaranteed to be in any particular order.
    #If the list contains an even number of elements, your function should return the average of the middle two.


def median(l):
    l.sort()
    lth = len(l)
    if lth % 2 == 1:
        return (l[int((lth/2) + .5)])
    else:
        return ((l[int(lth/2)] + l[int(lth/2 - 1)]) / 2.0)
