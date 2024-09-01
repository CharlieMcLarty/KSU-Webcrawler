import json
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from string import punctuation

with open('output.json', encoding='utf8') as f:
    data = json.load(f)

# Creates a collection for each word and email and their number of occurrences
wordCount = Counter()
emailCount = Counter()
totalWords = 0
emailSites = 0
for row in data:
    words = row['body']
    totalWords += len(words)
    for word in words:
        wordCount[word] += 1
    if len(row['email']) != 0:
        emailSites += 1
    for address in row['email']:
        emailCount[address] += 1

# Prints website statistics
averageLength = totalWords / len(data)
print("doc_len:", averageLength)
print("emails:")
for email, count in emailCount.most_common(10):
    print(f"\t({email}, {count})")
averageEmailSite = emailSites / len(data)
print("perc:", averageEmailSite)


# Prints word statistics
def print_words(counter):
    print(f"\n{"rank":<6}  {"term":<12}  {"freq.":<7}  {"perc.":<7}")
    print("-" * 36)
    for i, (word, count) in enumerate(counter.most_common(30), start=1):
        print(f"{i:<6}  {word:<12}  {count:<7}  {count / totalWords:<7.3f}")


print_words(wordCount)
stops = set(stopwords.words('english'))
# Remove stopwords and punctuation
for word in stops:
    if word in wordCount:
        del wordCount[word]
for punc in punctuation:
    if punc in wordCount:
        del wordCount[punc]
print_words(wordCount)

words, counts = zip(*wordCount.items())
sorted_words = sorted(counts, reverse=True)
ranks = range(1, len(sorted_words) + 1)

plt.figure(figsize=(10, 6))
plt.plot(ranks, sorted_words, marker='o', linestyle='-', color='b')
plt.title("Word Frequency Plot")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("images/word_frequency.png")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(ranks, sorted_words, marker='o', linestyle='-', color='r')
plt.title("Word Frequency Plot (log-log)")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale("log")
plt.yscale("log")
plt.tight_layout()
plt.savefig("images/word_frequency_log_log.png")
plt.show()

