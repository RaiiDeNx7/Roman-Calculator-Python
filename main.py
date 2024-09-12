from mathfunctions import *
from romantoint import *
from inttoroman import *
from NoOperator import *
from ErrorHandling import *
from stringManipulation import *

#Initialize Numeral String
numeral = "1"

#Check user input for invalid characters. Keep asking for input until a correct input has been made.
while not (InputCheck(numeral) and checkIfRoman(numeral) and duplicateOperator(numeral)):

    #Get input from user
     numeral = input("\nEnter your equation: ")

     #Strip white space at beginning and ends of string
     numeral = numeral.strip()  

     #Strip white space in between words
     numeral = numeral.replace(" ","") 

     #turn string into upper case for easier computing
     numeral = numeral.upper() 


     #If incorrect input, print error
     if not (InputCheck(numeral) and checkIfRoman(numeral) and duplicateOperator(numeral)):
          print("Error: Incorrect input detected. Please try again!")


#print test
print("The stripped equation is: " + numeral)


#Calls findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
if findOperator(numeral) == False:
        #If no operator found, the string is stripped of unneeded parenthesis and brackets for easy conversion.
        numeral = numeral.strip("()[]")  

        #print test
        print("The integer conversion of your roman numeral is: " + str(roman2int(numeral)))

        #successful termination
        exit()


#seperation of operators from numerals
seperatedString = split_operators(numeral)

#print test
print("The comp is: " + str(seperatedString))

#runs the roman numeral string through function to turn all roman numerals into integers.
integerString = [roman2int(i) if i not in ['+', '-', '*', '/',"(",")","[","]"] else i for i in seperatedString]

#print test
print("List to evalutate: " + str(integerString))

#combining the list back into a string
combinedString = join_tokens(integerString)
print(combinedString)  # Output: "20 + 10"

# Example usage
expr = combinedString
result = eval_expr(expr)

#check if number is float or a valid input
if (IsWhole(result) == False):
     print("Error: Can't Calculate Decimals")
     exit()

result = int(result)
print("the evaluated integer is: " + str(result))


#Call num2roman function to turn evaluated integer back into a roman numeral
roman = num2roman(result)

#print out answer to user
print(roman)

