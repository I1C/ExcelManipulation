#!/usr/bin/python3.7

import pyexcel

def get_profile_data():
	input_Name = input("\nWhat is your name ? ")
	input_LastName = input("What is your last name ? ")
        input_Occupation = input("What is your occupation ? ")
	d = {"Name": input_Name, "Last Name": input_LastName, "Occupation" : input_Occupation}
	return d

mylistdict = [] 
print("Hello! This program will make you a *.xls file")

while(True):
	mylistdict.append(get_profile_data()) 
	keep_going = input ("\nWould you like to add another person? Press 'Enter' to continue, or 'q' to quit: ")
	if(keep_going.lower()=='q'):
		break

filename = input("\nWhat is the name of the *.xls file? ")
myxlsfile = filename + ".xls"

pyexcel.save_as(records=mylistdict, dest_file_name=myxlsfile)

print("The file " + filename + ".xls should be in your local directory ^_^ ")
