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

from FunctionPackage.DecryptionFunctions import *

NoverList = TeamResults('Nover', 'EncryptedGroupHints.json')
NoverListInt = []
# Need to convert the string results from the json file to integers to be usable for indexing later
# reference website for the for-loop : https://www.pythonforbeginners.com/basics/convert-a-list-of-strings-to-ints-in-python
for string in NoverList:
    is_digit = string.isdigit()
    if is_digit:
        integer = int(string)
        NoverListInt.append(integer)
    else:
        print('String Conversion Issue')
        
NewNover = EnglishList('english.txt')
# print(NewNover)

NoverLocs = LocationLookup(NewNover, NoverListInt)
print(NoverLocs)