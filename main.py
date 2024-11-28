from collections import Counter


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    words_count = len(words)
    print(words_count)
    file_contents_no_whitespace = file_contents.lower().replace(" ", "")
    counter = char_count(file_contents_no_whitespace)
    print(counter)
    words_list = dict_list(counter)
    words_list.sort(reverse=True, key=sort_on)
    print(list)
    return 0


def char_count(text):
    counter = Counter(text)
    return counter


def dict_list(words_dict):
    words_list = []
    for key in words_dict:
        if key.isalpha():
            words_list.append({"name": key, "num": words_dict[key]})
    return words_list


def sort_on(words_dict):
    return words_dict["num"]


main()
