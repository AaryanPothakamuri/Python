from fileinput import filename


def countWordsFromFile():
    filename = input("Enter the file name")
    numberOfWords = 0
    file = open(filename)
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of Words:",numberOfWords)
countWordsFromFile()