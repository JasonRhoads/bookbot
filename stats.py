def get_num_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    
    for c in text:
        if c.lower() in characters:
            characters[c.lower()] += 1
        else:
            characters[c.lower()] = 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_dictionaries(dictionary):
    sorted_dictionary = []
    
    for entry in dictionary:
        sorted_dictionary.append({"char": entry, "num": dictionary[entry]})
        
    sorted_dictionary.sort(reverse=True, key=sort_on)
    return sorted_dictionary