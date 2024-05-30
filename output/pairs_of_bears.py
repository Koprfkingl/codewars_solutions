"""Kata - Pairs of Bears

completed at: 2020-07-15 13:00:25
by: 

In order to prove it's success and gain funding, the wilderness zoo needs to prove to environmentalists that it has x number of mating pairs of bears. 

### Task:
You must check within a string (s) to find all of the mating pairs, returning a list/array of the string containing valid mating pairs and a boolean indicating whether the ***total*** number of bears is greater than or equal to x.

### Rules for a 'valid' mating pair:
1. Bears are either 'B' (male) or '8' (female),
2. Bears must be together in male/female pairs 'B8' or '8B',
3. Mating pairs must involve two distinct bears each ('B8B' may look fun, but does not count as two pairs).

Return an array containing a string of the valid mating pairs available (empty string if there are no pairs), and a boolean indicating whether the ***total*** number of bears is greater than or equal to x. , e.g:

(6, 'EvHB8KN8ik8BiyxfeyKBmiCMj') ---> ['B88B', false]; *in this example, the number of bears(=4) is lesser than the given value of x(=6)*


"""

def bears(x,s):
    # your code here
    slicedList = []
    maleFemale = 'B8'
    femaleMale = '8B'
    listOfPairs = []
    index = 0
    for i in s:

        # slice string s
        string = s[index:index + 2]
        # add it to list
        slicedList.append(string)
        index = index + 1

    lstIndex = 0
    # loop through strings in 'sliced list'
    for i in slicedList:
        # if i value in 'sliced list' equals to maleFemale string
        if i == maleFemale:
            # add the i value to 'list of pairs'
            listOfPairs.append(i)
            # delete found pair from 'sliced list'
            slicedList.pop(lstIndex)

        # if i value in 'sliced list' equals to femaleMale string
        if i == femaleMale:
            # add i to list of pairs
            listOfPairs.append(i)
            # delete found pair from 'sliced list'
            slicedList.pop(lstIndex)
        lstIndex = lstIndex + 1



    numberOfPairs = len(listOfPairs)

    truefalse = 0
    if numberOfPairs >= int(x):
        truefalse = True
    else:
        truefalse = False

    # convert 'list of pairs' to string
    outputString = ''.join(listOfPairs)

    # prepare correct output format
    solution = [outputString, truefalse]
    return(solution)
