

def main():
    text = "this is a collection of words of nice words this is a fun thing it is"
    words = text.lower().split()     # convert to lower case and put into a list
    word_to_count = convert_to_dictionary(words)
    print_sorted_word_frequency(word_to_count)

def convert_to_dictionary(words):
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count

def print_sorted_word_frequency(word_to_count):
    for key in sorted(word_to_count.keys()):
        print(f"{key} : {word_to_count[key]}")

if __name__ == '__main__':
    main()