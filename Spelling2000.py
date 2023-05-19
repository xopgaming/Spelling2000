"""
    Import Libraries
"""

# for TTS conversion
from gtts import gTTS

# to play the converted audio
from playsound import playsound

# to generate random numbers
from random import randint



"""
    Initiate loading sequence
"""

# Beginning of loading sequence
print("Loading...")

# List of index numbers for all the completed words
doneList = []

# List of index numbers for all the words answered incorrectly
wrongList = []

resourceDirectory = __file__.removesuffix("Spelling2000.py")+"Resources\\"

# Open vocab.txt
f = open(resourceDirectory+"vocab.txt", "r")

# Extract words from file as a list
tempList = f.readlines()

# Strip \n from each item in list
wordList = []
for i in tempList:
    wordList.append(i.strip())

# Close file
f.close()

# Get every mp3 file for each word
for i in range(len(wordList)):
    # Passing the text and language to the engine
    # slow=False tells the module that the converted audio should have a high speed
    myobj = gTTS(text=wordList[i], lang='en', slow=False)

    # Saving the converted audio in a mp3 file 
    myobj.save(resourceDirectory+"tempSounds\\"+str(i)+".mp3")

# End of loading sequence
print("Done loading\n")


"""
    End loading sequence
"""




"""
    Ask questions
"""

# Ask questions until there are same number of items in doneList and wordList
while len(doneList) != len(wordList):
    # set a random index from the list
    number = randint(0,len(wordList)-1)
    # check and change if word has been already been said
    while number in doneList:
        number = randint(0,len(wordList)-1)
    
    # Playing the converted file
    playsound(resourceDirectory+"tempSounds\\"+str(number)+".mp3")

    # Ask question
    answer = input("Word: ")
    
    # Check if user's answer is the same as correct answer
    if answer.lower() == wordList[number].lower():
        # If the answer is correct, add index number to doneList
        doneList.append(number)
        print("Correct Answer!")
    else:
        # If answer is wrong, print Wrong Answer
        if not number in wrongList:
            wrongList.append(number)
        print("Wrong Answer!")




"""
    End of quiz
"""

# Indicate end of quiz
print("\nAll words done!\n")
# Print out all words gotten incorrect
print("Words to revise: ")
for i in range(len(wrongList)):
    print(wordList[wrongList[i]])
print()
