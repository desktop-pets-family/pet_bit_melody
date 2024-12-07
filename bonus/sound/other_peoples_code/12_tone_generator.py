# This code was gathered from: https://github.com/colry/Tone-Row-Generator/blob/master/12_Tone_Generator.py
################################################################################
# AUTHOR:       Chris Olry
# FILENAME:     12_Tone_Generator.py
# DATE:         Finished on 10-23-2019
# DESCRIPTION:  Generates tone rows.
# VERSION:      0.9 BETA
# TO-DO:        Input validation, error checking.
# OTHER:
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
################################################################################

###########
# Modules #
###########
import random   # Necessary for the selection of notes from the array.
# import sys

#############
# Variables #
#############
genNum = 0      # Number of notes to generate.
remainder = 0   # Remaining notes after looping thru array.
arrTimes = 0    # Number of times array needs looped.

#############
# Functions #
#############


def noteGen(genNum):
    # Note Array (List)
    noteArr = ["A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "G#"]

    # Ensure that genNum is an integer. Compiler barked about this before.
    genNum = int(genNum)

    # This logic ensures that the notes are NOT duplicated.
    # Number of times array needs looped. (Number of notes / 12)
    arrTimes = genNum / 12
    remainder = genNum % 12  # Remaining notes after above loops.
    genNum = genNum - remainder  # Calculate number of elements remaining.

    # Determine if the user input is divisible by 12.
    if remainder == 0:
        i = 0
    else:
        # If not, there needs to be 1 less loop to allow the remainder to be determined.
        i = 1

    # Go thru the number of times the array needs looped.
    while i < arrTimes:
        random.shuffle(noteArr)     # Shuffle the array
        print(*noteArr, sep="\n")  # Print the array, each entry on new line.
        i = i + 1                   # Increment.

    random.shuffle(noteArr)  # Shuffle the array

    i = 0   # Set loop to 0.
    # Loop for remainder.
    while i < remainder:
        print(noteArr[i])  # Loop thru remainder.
        i = i + 1  # Increment.
# End noteGen()

###########
# RunTime #
###########


def main():
    genNum = 1
    # Prompt for number of notes.
    # Loop until user inputs "0" (zero).
    while genNum != 0:
        print('How many notes would you like to generate? ')
        genNum = input('Enter a whole number, or "0" to quit: ')
        if genNum == "0":
            return
        noteGen(genNum)
        print()


#
main()
