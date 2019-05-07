# Anuj Kashyap
# BIOF309 - Code Writing Project

print("")
print ("Anuj Kashyap")
print ("May 7 2019")
print("")
print("\t\t\tBIOF309 - Code Writing Project - Anuj Kashyap")
print("")

#The goal of this project is to learn code writing for biological applications
print("-------------------------------------------------------------------------")
#Goal 1 - How to convert DNA to RNA for Biologists
print("")
print("Goal 1")
print("I am going to write a program transcribes DNA to RNA. I will create a string that stores a DNA sequence in my code, and then replaces all the T's with U's. The program will display to the screen the DNA and RNA sequences.")
print("")
#Enter DNA sequence below
DNA = "GATATATAGGCGCTACCCA"
#Setup DNA to RNA conversion (T-->U)
RNA = DNA.replace('T', 'U')
print ("My DNA sequence is the following  " + DNA)
print ("Today, I would like to transcribe DNA into RNA as follows: " + RNA)
print("")
print("-------------------------------------------------------------------------")
#Goal 2 - Learn how to store the following DNA sequence into an array (not string) - for Biologists
print("Goal 2")
#Question#3
print("Store a sequence as a array and not a string")
#I will write a program to store the following DNA sequence into an array (not string):
#CCGTAACGC (where every letter is an element of the array).
Sequence = "CCGTAACGC"
SequenceArray = list(Sequence)
print(SequenceArray)
#Then the following:
print("Add a T to the end of the array as such:  ")
#a) Add a T to the end of the array, then print the array.
SequenceArray.append('T')
print(SequenceArray)
print("Then remove the 1st element of the array by using pop(0)")
#b) Remove the 1st element of the array by using pop(0) to remove 1st element in index and print it.
print("Dear User, we will remove the 1st element as follows:  " + SequenceArray.pop(0))
print(SequenceArray)
print("Then add a T to the beginning of the array")
#c) Add T to the beginning of the array and print the array.
print("Dear User, we will add T to the beginning of the array as follows: " )
SequenceArray.insert(0, 'T')
print(SequenceArray)
print("Neat and clean code is readable code")
#d) My output is neat and readable.    
print("Cheers!")
print("-------------------------------------------------------------------------")
#import the os find the file
import os
#import the regular module
import re
#Goal 3 - Learn how to setup a function that accepts a file containing sequence as an argument
#My program will ask if the file exists or not
#If the file does not exist - then it will state it
#Setup a function that will accept a motif search in a sequence
print("Goal 3")
#define the function below
def isFileExist(BIOF309file):

    while not os.path.isfile(BIOF309file):
        print ("Dear User, your file was not found. Pick again. Our motto is 5 strikes and you are out. ")
        BIOF309file = input("Dear User, please enter the file name that you are looking for:   ")
    return BIOF309file 

#Now setup a function that will accept a motif search in a sequence
def checkmotifinseq(sequence, motif):

    if (re.search(motif, sequence)):
        print("Dear User, we have found your motif within our sequence")
    else:
        print("Dear User, we could not find your motif within our sequence")

def main():
        BIOF309file = input ("Dear User, please enter your file name:  ")
        BIOF309file = isFileExist(BIOF309file)

        doc = ""
        file = open(BIOF309file)
        for line in file:
            if line.startswith(">"):
                print(line.rstrip())
            else:
                doc += line.rstrip()
        print(doc) 
        
        motif = input("Dear User, please enter the motif that you would like to search for:   ")

        checkmotifinseq(doc, motif)
main()
print("-------------------------------------------------------------------------")

