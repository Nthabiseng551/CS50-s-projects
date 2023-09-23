from cs50 import get_string

def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = int(round((0.0588 * L) - (0.296 * S) - 15.8))
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

# Function to count letters in a text
def count_letters(text):
    n = 0
    for i in range(len(text))
        if isalpha(text[i]):
            n = n + 1
        else:
            n = n + 0
    return n

def count_words(text):
def count_sentences(text):