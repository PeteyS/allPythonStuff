import shutil

import os
import re

#shutil.unpack_archive('unzip_me_for_instructions.zip','unpackedpuzzlezip','zip') i cant test if i leave this code because it resets that zip file each time, but it just unpacks zip
numbers = {} #creating dictionary to display phone number and what text file they were found in
listit=[] #creating list for string formating of the regex tuple (phone numbers)

for folder,sub_folders,files in os.walk(r'D:\Code\python\unpackedpuzzlezip'): #this will iterate through the directory going through folder, subfolder, and files
    print (f'currently looking at folder {folder}')
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders: #iterate through the subfolder of each folder
        print (f'Subfolder: {sub_fold}')
    
    print ('\n')
    print ("the files are: ")
    for f in files: #iterate through the files of each folder (not each subfolder)
        print (f'File: {f}')
        path = fr'{folder}\{f}' #path will give the full path to the textfile (only way i could bypass file not found error)
        opened_file = open(path,'r') #open file using path
        phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') #use regex compile to search for phone number pattern
        results = re.findall(phone_pattern,opened_file.read()) #find all all phone numbers in text file
        if len(results)>0: #if a phone number was found, regex list will not be empty
            for a,b,c in results: #tuple unpacking for string format
                listit = [] #make list empty, so multiple lists wont have build up for dictionary enteries later down the line
                listit.append(a) #append tuple objects
                listit.append(b)
                listit.append(c)
            joined = "-".join(listit) #join together numbers as strings
            numbers.update({(f):(joined)}) #create dictionary with file being key and number being value
            joined = "" #empty joined for next phone number
    print ('\n')

instruct = open(r'D:\Code\python\unpackedpuzzlezip\extracted_content\Instructions.txt','r') #open instructions
print(instruct.read()) #print instructions
print(numbers)#print numbers dictionary


