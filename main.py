import sys

"""
Sorting function.
"""
def sort_on(d: dict):
    return d["num"]

"""
Create a list of dictionaries from dictionary entries in d.
"""
def dict_to_list(d: dict):
    d_list = []
    for (key, value) in d.items():
        d_list.append({"name": key, "num": value})
    return d_list

def main():

    # file path passed as an argument
    # file_path = sys.argv[1]
    file_path = "books/frankenstein.txt"    # hardcoded for testing purposes
    # initialize an empty dictionary for characters
    char_dict = {}

    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            for char in word:
                if char.isalpha():
                    char = char.lower()
                    if char not in char_dict:
                        char_dict[char] = 1
                    else:
                        char_dict[char] = char_dict.get(char) + 1
        char_list = dict_to_list(char_dict)
        char_list.sort(reverse=True, key=sort_on)
        create_report(file_path, len(words), char_list)

""" 
Prints out a detailed report of the given book
"""
def create_report(file_path: str, c_words: int, char_list: list):
    print(f"--- Begin report of {file_path} ---")
    print(f"{c_words} words found in the document")
    print("\n")
    for d in char_list:
        print(f"The {d.get('name')} character was found {d.get('num')} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()