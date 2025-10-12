# Count words in book
def count_words(book_text):
    return len(book_text.split())

# Count unique characters in the book;
def count_chars(book_text):
    book_text = book_text.lower()
    words = book_text.split()
    char_count = {}
    for word in words:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

# Sort dictionary of characters.
def sort_on(items):
    return items["count"]
def sort_chars(dict_of_chars):
    cartrige = []
    sorted_chars = {}
    for char in dict_of_chars: 
        cartrige.append({"char":char, "count":dict_of_chars[char]})
    cartrige.sort(reverse=True, key=sort_on)
    for item in cartrige:
        sorted_chars[item["char"]] = item["count"]
    return sorted_chars
        
