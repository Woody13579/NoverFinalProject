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