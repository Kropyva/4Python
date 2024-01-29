import re

def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            sentences = re.split(r'(?<=[.!?])\s+', text)
            if len(sentences) > 0:
                print("First sentence:")
                print(sentences[0])
                return sentences[0]
            else:
                print("File is empty.")
    except FileNotFoundError:
        print("File is not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

def ukrainian_sort_key(word):
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    return [alphabet.index(letter) for letter in word.lower()]

def english_sort_key(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return [alphabet.index(letter) for letter in word.lower()]

def print_sorted_words(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    words = [word for word in words if word.isalpha()]

    ukrainian_words = sorted([word for word in words if re.match(r'^[а-яїієґ]+$', word, re.I)], key=ukrainian_sort_key)
    english_words = sorted([word for word in words if re.match(r'^[a-z]+$', word, re.I)], key=english_sort_key)

    if ukrainian_words:
        print("\nUkrainian words:")
        print(", ".join(ukrainian_words))
    if english_words:
        print("\nEnglish words:")
        print(", ".join(english_words))

    print(f"\nCount of words: {len(words)}")

def main():
    filename = 'input.txt'
    sentence = read_first_sentence(filename)
    if sentence:
        if len(sentence.split()) > 100:
            print("The sentance contains more than 100 words. Stop process.")
        else:print_sorted_words(sentence)

if __name__ == "__main__":
    main()