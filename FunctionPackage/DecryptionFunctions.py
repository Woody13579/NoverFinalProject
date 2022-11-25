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


# Code from https://www.geeksforgeeks.org/read-json-file-using-python/
import json
def TeamResults(TeamName):
    # json.load(_io)
    io = open("C:/Users/Matthew Cox/git/NoverFinalProject/NoverFinalProject/MainPackage/EncryptedGroupHints.json")
    dictionary = json.load(io)
    
    # or one-liner
    # dictionary = json.load(open("in.json","r"))
    
    return(dictionary[str(TeamName)])


# Code to Import List of English words
def EnglishList(filename):
    #define text file to open
    my_file = open('english.txt', 'r')
    
    #read text file into list
    data = my_file.read()
    
    #create an empty list and delimit the string into its elements
    newList = []
    newList = data.split('\n')
    return newList
