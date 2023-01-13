# Task 3

# You should create a program that processes a file containing a list of student IDs and names, and produces a second file containing the student IDs and the email address that should 
# be created.The first part is the student ID (at Poppleton that is always the same length). The rest of the line is the student's name, with family name separated from forenames by a 
# comma. As shown, and as in real life, students have different numbers of forenames. The first part of a student's email consists of their initials, separated by dots, their surname, 
# and four random digits (this last is to ensure that all students get unique emails). If a surname contains any non-alphabetic character (as in "Fink-Nottle", "De Gea", or "O'Mahoney")
# those characters are removed. The second part is the University's domain, which is the same for all students. The result is rendered all in lower case.

import string
#We import "random" because to generate a random number.
from random import choice
chars = string.digits
#Open the Students.txt file and use the Student Id and Email.txt files to rewrite the output.
with open('students.txt','r') as file_name, open("Student Id and Email.txt", "w") as Email_id:
    for i in file_name:
        #Separating Student Information with first list Student_Id and First_Name and the second list with Last_Name.
        Student_Info = i.strip().split(' ')
        forename,surname = i.split(', ')
        #To take the only first character from the surname. 
        last_name = '.'.join([surname[0] for surname in surname.split(' ')]).lower()
        #For the first name, we use the indexing function from 9, because from 0 to 8, index is for student IDs.
        first_name = ''.join(a for a in forename[9:]).lower()
        #It will show the student_id.
        student_id = Student_Info[0]
        #To generate an email for all student IDs, add the forename and surname variables.
        email = student_id +" " + last_name + "." + first_name + ''.join(choice(chars) for _ in range(4))+"@poppleton.ac.uk"
        #Write all output in the Student ID and Email.txt file.
        Email_id.write(f"{email}\n")