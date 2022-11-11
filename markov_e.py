"""Generate Markov text from text files."""

from random import choice

#DEFUNCT n long
# python3 markov.py

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path)
    return text_string.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    
    # needs to create Tuple==>print text[i], text[i + 1]
    #This tuple will be the key to our dictionary for the Markov Chain
    #
    #erikkas thoughts:
    #empty dictionary
    #LOOP thrugh string and couple up adjacent indices into tuples:
    make empty tuple<---not efficient, we dont know how many tuples...may just need method
        #LOOP through tuple (for i in tuple) ....assign these as dictionaty key(s)

    
    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {} #TUPLES are KEYS, LISTS are VALUES
    
    split_string = text_string.split() #<----now a LIST of words

    for i in range(len(split_string) - 2):   #i+1, i+2, 
        key=(split_string[i], split_string[i + 1]) #<-----implicitly a TUPLES now, ordered pair
        next_word = split_string[i+2] #list ofwords...split_string [i]=0 index word, THIS is us recording that the first misc. word came after first two (tuple)

        #if key is already there or not <-behavioral
        if key in chains:
            value = chains[key] #all those other tiny filler words that follow our key tuples
        else:
            value = [] #now we have a value regardless

        value.append(next_word) #the value is 
        chains[key]=value #<----dictionary assignment 
    
    return chains
    

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    key = choice(list(chains)) #taking keys from chain and making a list...bc choice needs an argument thats iterable
    words.extend(key)
    while key in chains:
        value = chains[key]
        next_word = choice(value)
        words.append(next_word)
        key = (key[1], next_word) #<----if this is false itll stop
    
    
    return ' '.join(words)


#will need a .rsplit (" ") or a delimiter


#when dicts are treated as enumerables, theyre only using keys....our keys are lists
#----------------------------------------------------------------------------------------------------
input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
#print (make_chains(input_text))

# Produce random text
random_text = make_text(chains)

print(random_text)
