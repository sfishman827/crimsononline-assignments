import string

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    freq = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                wordm = word.translate(string.maketrans("",""), string.punctuation)
                if wordm in freq:
                    freq[wordm] += 1
                else:
                    freq[wordm] = 1

    return sorted(freq, key=freq.get, reverse=True)    
    

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    freq = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                wordm = word.translate(string.maketrans("",""), string.punctuation)
                if len(wordm) > min_chars:
                    if wordm in freq:
                        freq[wordm] += 1
                    else:
                        freq[wordm] = 1

    return sorted(freq, key=freq.get, reverse=True)    

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    freq = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                wordm = word.translate(string.maketrans("",""), string.punctuation)
                if len(wordm) > min_chars:
                    if wordm in freq:
                        freq[wordm] += 1
                    else:
                        freq[wordm] = 1

    return sorted(freq.items(), key=lambda freq:freq[1], reverse=True)

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        freq = {}
        with open(filename, 'r') as f:
            for line in f:
                words = line.split()
                for word in words:
                    wordm = word.translate(string.maketrans("",""), string.punctuation)
                    if len(wordm) > min_chars:
                        if wordm in freq:
                            freq[wordm] += 1
                        else:
                            freq[wordm] = 1
        return sorted(freq.items(), key=lambda freq:freq[1], reverse=True)
    
    except IOError:
        return None

