import os, re

f = open("file.txt", 'r')
t = f.read()
rawText = str(t).lower()
print('Raw Text (lowercase):\n', rawText)
allWords = re.findall('[aA-zZ\']+', rawText)
print('All Words:\n', allWords)
allWordsWithoutDuplicates = list(dict.fromkeys(allWords))
print('All WordsWithout Duplicates:\n', allWordsWithoutDuplicates)

f.close()
