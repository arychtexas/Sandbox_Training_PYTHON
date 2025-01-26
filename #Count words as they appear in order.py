#Word frequencies

""" Write a program that reads a list of words. 
Then, the program outputs those words and their frequencies."""

word_freq = {}

# Read input and update frequency count
while True:
    try:
        words = input().split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        # Print words and their frequencies
        for word in words:
            print(word, word_freq[word])
    except EOFError:
        break
