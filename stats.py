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