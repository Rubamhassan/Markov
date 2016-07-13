from random import choice

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    raw_file = open(file_path).read()
    print raw_file
    return raw_file


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    poem = text_string.rstrip()
    lst_poem = poem.split() #this makes it into a list

    for word in range(len(lst_poem) - 2):
        key = (lst_poem[word], lst_poem[word + 1])
        value = lst_poem[word + 2]

        # if key in chains:
        #     chains[key].append(value)
        # else:
        #     chains[key] = [value]

        chains[key] = chains.get(key, [])
        chains[key].append(lst_poem[word+2])

    print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    random_key = choice(chains.random_key())
    words = [random_key[0], random_key[1]]

    for key in chains:
        word = chains(chains[key])
        words.append(word)
        key = (key[1], word)
    return " ".join(words)


    # random_key = choice(chains.keys())

    # for key in random_key:
    #     random_value = chains.values(key)
    #     new_variable = " ".join(random_key, random_value)
    #     new_key chain[key].append(new_variable) #make string a new key
    #     chains.get(random_key)
    #     return 
    

# find one inital random key

# for loop
#     use picked key to find value in dictionary (which is a tuple)
#     new_variable = convert that key to a string
#     new_key = ("second word in the first key", "random word from the list of words that follow")
#     look up new_key in dictionary & pull new_random_word out of new_key
#     return extend new_key in text = ""
# print text



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
