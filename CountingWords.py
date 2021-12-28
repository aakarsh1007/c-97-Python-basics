intro = input("Enter Something About You:")
charCount = 0
wordCount = 0

for i in intro:
    charCount = charCount+1
    if(i == ' '):
        wordCount = wordCount+1

print(charCount)
print(wordCount+1)
