#Import json module
import json

#Loading the json file into the variable birthday unto MongoDB
birthday = json.load(open("My_Birthdays_3.json"))

##Printing the output pretext
print(">>> Welcome to the birthday dictionary. We know the birthdays of: ")
#To call the names in the variable birthday, 
#call the values out from the birthday variable and print
for name in birthday:
    print(name)
  
#Defining the input functions for the statement using variable name_on_request
#Calling both the key = name and the value = birthdate
name_on_request = input(">>> Who's birthday do you want to look up : ? ")
for name, birthdate in birthday.items():
    #Defining the condition for name print for subsequent birthdate print
    if name == name_on_request: 
        print(">>>%s's birthday is %s: " %(name, birthdate))
        