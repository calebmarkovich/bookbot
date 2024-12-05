def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  chars_dict = get_chars_dict(text)
  chars_sorted_list = get_sorted_chars_list(chars_dict)
  
  print_report(word_count, chars_sorted_list, book_path)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  return len(text.split())

  with open("books/frankenstein.txt") as f:
      file_contents = f.read()
      words = file_contents.split()
      characters = count_characters(file_contents)
      print_report(words, characters)

def get_chars_dict(text):
  chars = {}
  for char in text:
    char = char.lower()
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  return chars

def get_sorted_chars_list(chars_dict):
  return sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)

def print_report(word_count, chars_sorted_list, book_path):
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  for char in chars_sorted_list:
    if char[0].isalpha():
      print(f"The '{char[0]}' character was found {char[1]} times")
  print("--- End report ---")

main()
