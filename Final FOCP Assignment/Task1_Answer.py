# Task 1

# Write a program that generates a password consisting of three random words joined together. The words can be drawn from a list (or lists) declared as CONSTANTS in the program. 
# The number of possible passwords that can be generated should be at least 500 (which is obviously not enough, but will do for now).Your program could be used to generate random
# passwords for, say, a new group of students. So it should start by prompting the user to enter the number of passwords needed, and should then display a list of that many passwords.
# The number should be between 1 and 24 inclusive.

import random
#Storing three different lists of constants (Constants_Name, Last_Name, and Address) will generate a random password.
Constants_Names = ["hem","sushan","saiman","suyog","manav","poshan","prabin","mridu"]
Last_Names = ["shah","bhandari","strestha","limbu","koirala","regmi","chaudhary","mainali"]
Address = ["saptari","kathmandu","birgung","dharan","balbari","biratnagar","rajbiraj","jhapa"]

#It will add three list's to the list.
a = [(i+j+k)for i in Constants_Names for j in Last_Names for k in Address]
#To check the total number of random passwords.
print("Total possible passwords",len(a))

print("\nPassword Generator\n==================\n")
try:
    #How many passwords do you need to input?
    input_number = int(input("How many passwords are needed?:"))
    for i in range(input_number):
        #It will check if input_number is greater_then or equal to 1 and less_then is equal to 24.
        if input_number >= 1 and input_number <= 24:
            #If the input_number is greater than 1 and less than 24, it will print the passwords in the given range.
            print(i+1,"-->",random.choice(a))
        else:
            #This statement will only show if input_number is less than 1 and greater than 24.
            print("Please enter a value between 1 and 24.")
            break
except ValueError:
    #if then enter a string, floating point number, decimal number, etc in input_number.
    print("Please enter a number.")