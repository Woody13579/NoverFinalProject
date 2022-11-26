'''
Name: Tyra Crandell, Matt Cox, Aaron Wood, Mark Johnson
email: crandete@mail.uc.edu, coxm6@mail.uc.edu, wood2ao@mail.uc.edu, johns8mk@mail.uc.edu
Assignment: Assignment 13
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: We can collaborate with a team to develop an Eclipse app and go on a scavenger hunt.
Citations:
Anything else that's relevant:
'''
# DecryptionFunctions.py
import json

# Code from https://www.geeksforgeeks.org/read-json-file-using-python/
def TeamResults(TeamName, Filename):
    # json.load(_io)
    io = open(Filename)
    dictionary = json.load(io)
    
    # or one-liner
    # dictionary = json.load(open("in.json","r"))
    
    return(dictionary[str(TeamName)])


# Code to Import List of English words
def EnglishList(filename):
    my_file = open(filename, 'r')
    data = my_file.read()
    
    #create an empty list and delimit the string into its elements
    newList = []
    newList = data.split('\n')
    return newList


# Function to slice the English list by the numbers gathered from the JSON file using indexing
def LocationLookup(NameOfList, NameOfDictionary):
    for index in NameOfDictionary:
        IndexingVariable = index - 1
        Word = NameOfList[IndexingVariable]
        print(Word)

    
    
    
    
    
    