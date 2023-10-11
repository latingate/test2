import platform
print('Python version ' + platform.python_version() + '\n')

import os, re

f = open("file.txt", 'r',encoding="utf8")
t = f.read()
rawText = str(t).lower()
print('Raw Text (lowercase):\n', rawText)
allWords = re.findall('[aA-zZ\']+', rawText)
hebrewWords = re.findall('[א-ת\']+', rawText)
print('All Words:\n', allWords)
print('Hebrew Words:\n', hebrewWords)
#dictonary
# allWordsWithoutDuplicates = dict.fromkeys(allWords)
# convert to list
allWordsWithoutDuplicates = list(dict.fromkeys(allWords))
print('All WordsWithout (English) Duplicates:\n', allWordsWithoutDuplicates)
# sortedWords = sorted(allWordsWithoutDuplicates, key=allWordsWithoutDuplicates.get)
sortedWords = allWordsWithoutDuplicates.copy()
sortedWords.sort()
print('Sorted Words (English):\n', sortedWords)
f.close()
