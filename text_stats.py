import json
from collections import Counter

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
print(f"\n{"rank":<6}  {"term":<12}  {"freq.":<7}  {"perc.":<7}")
print("-" * 36)
for i, (word, count) in enumerate(wordCount.most_common(30), start=1):
    print(f"{i:<6}  {word:<12}  {count:<7}  {count / totalWords:<7.3f}")