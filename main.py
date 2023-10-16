def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dictionary = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dictionary)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if item['char'].isalpha():
            print(f"The {item['char']} was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read().lower()
        
        
def sort_on(d):
    return d["num"]


def get_num_words(text):
        words = text.split()
        return len(words)         

def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




main()
    
