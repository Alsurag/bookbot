def word_count(book):
    word_list = book.split()
    words = len(word_list)
    return words

def char_count(book):
    text = book.lower()
    c_count = {}    
    char_count = []
    for c in text:
        if c in c_count:
            c_count[c] += 1
        else:
            c_count[c] = 1
    for char, num in c_count.items():
        char_dict = {char: num}
        char_count.append(char_dict)
    char_count.sort(reverse=True, key=sort_on)
    return char_count

def sort_on(dict):    
    return list(dict.values())[0]