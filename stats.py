def string_word_count(book_text_string):
    num_words = len(book_text_string.split())
    return num_words

def character_count(book_text_string):
    char_count = {}
    for char in book_text_string:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sorted_dicts(char_count_dict):
    dict_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            mini_dict = {}
            mini_dict["char"] = char
            mini_dict["num"] = count
            dict_list.append(mini_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list