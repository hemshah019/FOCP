# Task 2

# You will write a program that will process the data stream from one of these devices to produce some useful statistics. The device is half way round the course, and is is known
# that every runner will pass it at most once.The data stream from the timing apparatus consists of the runner's number (as read from their singlet), and a time in seconds. A time 
# in seconds is used because runners tend to start at different actual times as they pass a designated point. The two elements on the line are separated by two colons (::), and each 
# data item appears on its own line.
import math

print("\nPark Run Timer")
print("~~~~~~~~~~~~~~")
print("\n\nLet's goo!")
Runner_Number = []
Runner_Time = []
Total = 0

while True:
    try:
        #This will show two inputs in one because we use the Split function.
        Run_No,Run_Tim = input("< ").split("::")
        #If Run_No and Run_Tim are both empty, this statement will run.
        if ('' == Run_No or '' == Run_Tim):
            print("Error in data stream. Ignorning. Carry on.")
        else:
            #If Run_No and Run_Tim are not empty, Runner_Number and Runner_Time are added.
            Runner_Number.append(Run_No)
            Runner_Time.append(int(Run_Tim))
            continue
    #If we enter anything except an integer, it will break and show output(eg if we enter END during input).    
    except ValueError:
        break
#If Runner_Number is greater than 1, it will add Runner_Time.       
for i in Runner_Time:
    Total += i

#To change the total number of Average_Time in minutes and seconds.   
Time_Length = len(Runner_Time)
Average_Time = Total/Time_Length
a_sec = Average_Time
a_sec = a_sec % (24 * 3600)
a_sec %= 3600
a_min = a_sec // 60
a_sec %= 60

#To change the total number of Fastest_Time in minutes and seconds.    
Fastest_Time = min(Runner_Time)
f_sec = Fastest_Time
f_sec = f_sec % (24 * 3600)
f_sec %= 3600
f_min = f_sec // 60
f_sec %= 60

#To change the total number of Slowest_Time in minutes and seconds.   
Slowest_Time = max(Runner_Time)
s_sec = Slowest_Time
s_sec = s_sec % (24 * 3600)
s_sec %= 3600
s_min = s_sec // 60
s_sec %= 60

#It will print the slowest_time from Runner_Time.
Runner_BestTime = Runner_Time.index(min(Runner_Time))

#We are printing the total number of runners who have entered.
print("\nTotal Runners: ",Time_Length)
#Round() means it will remove all values ​​after the dot (.)
print("Average Time: ",round(a_min,),"Minutes, ",round(a_sec,),"Seconds")
print("Fastest Time: ",round(f_min,),"Minutes, ",round(f_sec,),"Seconds")
print("Slowest Time: ",round(s_min,),"Minutes, ",round(s_sec,),"Seconds")
#Printing the best runner time.
print("\nBest Time Here: Runner #",Runner_Number[Runner_BestTime])