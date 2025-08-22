


def get_word_count(text): #counts the number of words in a file
            num_words = len(text.split())
            return num_words


def get_char_count(text): #counts the number of times each unique character appears in a file
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_by(item): #defines a function to retrieve a custom sorting value.
    return item["freq"]


def get_sorted_char_count(text): #sorts unique_char_count from most to least frequent, discarding non-alphabet characters
    char_list = []
    char_dict = get_char_count(text) #calls unique_char_count to get a dictionary of characters and their counts
    for char, count in char_dict.items():
        if char.isalpha(): 
            char_list.append({"char": char, "freq": count})          
            char_list.sort(key=sort_by, reverse=True)
    return char_list #returns a list of dictionaries with characters and their counts, sorted by frequency
