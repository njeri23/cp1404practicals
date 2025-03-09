word_count = {}

text = input("Enter a string of text: ")

words = text.split()

for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = dict(sorted(word_count.items()))

print("\nWord occurrences (sorted):")
for word, count in sorted_word_count.items():
    print(f"{word:15} : {count}")
