"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    return (x%2==1)


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    reverse="".join(list(reversed(word)))
    return reverse==word


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    for e in numlist:
        if not is_odd(e):
            numlist.remove(e)
    return numlist


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    words=text.split(" ")
    my_dict={}
    for word in words:
        if word in my_dict.keys():
            #word has already appeared in the text as in in the dict
            my_dict[word]+=1
        else:
            #word has not appeared in the text before, it is not in the dict
            my_dict[word]=1
    return my_dict