def lines(a, b):
    """Return lines in both a and b"""
    a_list = a.split("\n")
    b_list = b.split("\n")
    result = []
    for line in a_list:
        if line in b_list and not line in result:
            result.append(line)
    return(result)



def sentences(a, b):
    from nltk.tokenize import sent_tokenize
    """Return sentences in both a and b"""
    a_list = sent_tokenize(a)
    b_list = sent_tokenize(b)
    result = []
    for sentence in a_list:
        if sentence in b_list and not sentence in result:
            result.append(sentence)
    return(result)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    result= []

    def substring(string, n):

        substring_list = []
        counter = 0

        while counter < len(string) - n:
            sub = string[counter:counter + n]
            counter += 1
            substring_list.append(sub)
        return substring_list

    for i in substring(a, n):
        if i in substring(b, n):
            result.append(i)

    return (result)
