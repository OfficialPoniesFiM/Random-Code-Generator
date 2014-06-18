#! /usr/bin/env python

#Random Code Generator: Makes random codes.
#Copyright (C) 2014 PoniesFiM/Nathan Guerrero
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#Contact me on Twitter at @PoniesFiM, or email at poniesfim@hushmail.com.

#We need to import one thing to the program can generate random numbers.
import random

#Because of copyright stuff, I have to print some things.
print("Random Code Generator Copyright (C) 2014 PoniesFiM/Nathan Guerrero")
print("This programs comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it under certain conditions.")

print("How many digits do you want? (A minimum of 4) (No decimals)")
permanentDigits = int(input()) #The program asks for input, turns it into an integer/floating point, and stores it into a variable called "permanentDigits".
while permanentDigits <= 3: #If permanentDigits is 3 or less, do something below, and go back if the variable is still 3 or less.
    print("Try again.")
    print("How many digits do you want? (A minimum of 4) (No decimals)")
    permanentDigits = int(input()) #The program asks for input, turns it into an integer/floating point, and stores it into a variable called "permanentDigits".
    
print("You have " + str(permanentDigits) + " digits.")
print("Generating code...")

#Before the program generates the code, some variables are made.
changingDigits = permanentDigits #changingDigits will be the same as permanentDigits, but permanentDigits will stay the same, and changingDigits won't.
randomCode = [] #All the code that is generated will be appended here.
randomNumber = 0 #This is the random number.
randomStuff = "" #This is the random character.
isCapital = 0 #This variable represents the state of if a character is a capital.

#The program runs the loop.
while changingDigits != 0: #While changingDigits isn't 0,
    randomNumber = random.randint(0, 36) #Generate a random number.
    
    if randomNumber == 0: #If the random number is 0,
        randomStuff = str(0) #The random character is 0 as a string.
    elif randomNumber == 1: #If the random number is 1,
        randomStuff = str(1) #The random character is 1 as a string.
    elif randomNumber == 2: #If the random number is 2,
        randomStuff = str(2) #The random character is 2 as a string.
    elif randomNumber == 3: #If the random number is 3,
        randomStuff = str(3) #The random character is 3 as a string.
    elif randomNumber == 4: #If the random number is 4,
        randomStuff = str(4) #The random character is 4 as a string.
    elif randomNumber == 5: #If the random number is 5,
        randomStuff = str(5) #The random character is 5 as a string.
    elif randomNumber == 6: #If the random number is 6,
        randomStuff = str(6) #The random character is 6 as a string.
    elif randomNumber == 7: #If the random number is 7,
        randomStuff = str(7) #The random character is 7 as a string.
    elif randomNumber == 8: #If the random number is 8,
        randomStuff = str(8) #The random character is 8 as a string.
    elif randomNumber == 9: #If the random number is 9,
        randomStuff = str(9) #The random character is 9 as a string.
    elif randomNumber == 10: #If the random number is 10,
        randomStuff = "a" #The random character is "a".
    elif randomNumber == 11: #If the random number is 11,
        randomStuff = "b" #The random character is "b".
    elif randomNumber == 12: #If the random number is 12,
        randomStuff = "c" #The random character is "c".
    elif randomNumber == 13: #If the random number is 13,
        randomStuff = "d" #The random character is "d".
    elif randomNumber == 14: #If the random number is 14,
        randomStuff = "e" #The random character is "e".
    elif randomNumber == 15: #If the random number is 15,
        randomStuff = "f" #The random character is "f".
    elif randomNumber == 16: #If the random number is 16,
        randomStuff = "g" #The random character is "g".
    elif randomNumber == 17: #If the random number is 17,
        randomStuff = "h" #The random character is "h".
    elif randomNumber == 18: #If the random number is 18,
        randomStuff = "i" #The random character is "i".
    elif randomNumber == 19: #If the random number is 19,
        randomStuff = "j" #The random character is "j".
    elif randomNumber == 20: #If the random number is 20,
        randomStuff = "k" #The random character is "k".
    elif randomNumber == 21: #If the random number is 21,
        randomStuff = "l" #The random character is "l".
    elif randomNumber == 22: #If the random number is 22,
        randomStuff = "m" #The random character is "m".
    elif randomNumber == 23: #If the random number is 23,
        randomStuff = "n" #The random character is "n".
    elif randomNumber == 24: #If the random number is 24,
        randomStuff = "o" #The random character is "o".
    elif randomNumber == 25: #If the random number is 25,
        randomStuff = "p" #The random character is "p".
    elif randomNumber == 26: #If the random number is 26,
        randomStuff = "q" #The random character is "q".
    elif randomNumber == 27: #If the random number is 27,
        randomStuff = "r" #The random character is "r".
    elif randomNumber == 28: #If the random number is 28,
        randomStuff = "s" #The random character is "s".
    elif randomNumber == 29: #If the random number is 29,
        randomStuff = "t" #The random character is "t".
    elif randomNumber == 30: #If the random number is 30,
        randomStuff = "u" #The random character is "u".
    elif randomNumber == 31: #If the random number is 31,
        randomStuff = "v" #The random character is "v".
    elif randomNumber == 32: #If the random number is 32,
        randomStuff = "w" #The random character is "w".
    elif randomNumber == 33: #If the random number is 33,
        randomStuff = "x" #The random character is "z".
    elif randomNumber == 34: #If the random number is 34,
        randomStuff = "y" #The random character is "y".
    elif randomNumber == 35: #If the random number is 35,
        randomStuff = "z" #The random character is "z".
    elif randomNumber == 36: #If the random number is 36,
        randomStuff = "_" #The random character is an underscore.
    
    isCapital = random.randint(0,1) #The program creates a random number that represents the state of if a letter is a capital and stores it in a variable called "isCapital".
    
    if str(randomNumber) in "10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35".split() and isCapital == 1: #If the random number is 10-35(which means the character is a letter, and not another type of character), and the random number that represents the state of when a letter is capital is 1,
        randomStuff = randomStuff.upper() #Make the current random character uppercase.
    randomCode.append(randomStuff) #Append the character to a list
    
    changingDigits -= 1 #Remove 1 from changingDigits.

newCode = "" #Another variable.
newCode = newCode.join(randomCode) #Add everything in the list of characters to this variable, newCode.
fileToPrintTo = open("randomCodes.txt", "a") #Open a file, and set the mode to append.
fileToPrintTo.write(str(newCode) + "\n") #Write the random code string to the file plus a \n to make a new line for the future.
fileToPrintTo.close() #Close and save the file.
print(newCode) #Print the code.
#Finished!
