#tuple unpacking

stock_prices = [('APPL',200),('GOOG',400), ('MSFT',100)]

for item in stock_prices:
    print(item)

#indiviudally grab items from the tuples

for ticker,price in stock_prices:
    print(ticker,price)

work_hours = [('Abby',10000),('Billy',4000),('Cassie',800)]
#we want to go thorugh the tuples and find which one has the most hours

def employeeCheck(work_hours):
    #used to keep track of which number of hours is the most
    current_max = 0
    #used to keep track of the name of the employee
    employee_of_month =''

    #for loop iterates through the tuples
    for employee,hours in work_hours:
        #if hours is more than current max, update value in variable to the newest number of hours assuming it was higher than the last
        if hours>current_max:
            current_max = hours
            employee_of_month = employee

    #return empoyee name and the current max number of hours
    return(employee_of_month,current_max)


#uses tuple unpacking to assign values to name and hours, with the variables being assinged in the same order that the function returns them
name,hours = employeeCheck(work_hours)

#to make sure you know whats being returned, so you dont try to unpack more than tuples items than are being returned
item = employeeCheck(work_hours)


#interactions between functions

from hashlib import new
import random
from typing import NamedTuple
#from typing_extensions import final #import random module to be used in this file

example = [1,2,3,4,5,6,7]#creating a list that will be used in the random shuffle

from random import shuffle #import shuffle from random 

shuffle(example)#using shuffle that was just imported, but this cannot be assinged to a variable because the function happens in place

def shuffle_list(mylist):#the built in shuffle that we called earlier cannot be assinged, so this function fills that need by returning the random list and it can be assigned
    shuffle(mylist)
    return mylist#returning the random list so it can be stored

result = shuffle_list(example)

print (result)

mylist = [' ','O',' '] #to be used in the monte function, where the user has to guess where the capital O is

def player_guess():#this functiion will get the player guess and return it as a interger to be used in another function
    guess = ''
    while guess not in ['0','1','2']: #keep asking for input if the number entered is not a number that will be accepted
        guess = input('Pick a number: 0, 1, or 2: ')
    return int(guess) #return as an integer

def check_guess(mylist,guess):#this function checks if the user guess is right or wrong 
    if mylist[guess] == 'O':#the users guess is used as an index position, and if that position has the O, then the user will be correct
        print('Correct')
    else:
        print('Wrong guess')
        print(mylist)

#initial list
#mylist = [' ','O',' ']
#shuffle list
#mixedup_list = shuffle_list(mylist)
#user guess
#guess = player_guess()
#check guess
#check_guess(mixedup_list,guess)

#learning args and kwargs

def myfunc (a,b): #this function takes two parameters and gets the sum, then finds 5 percent of that sum and returns it 
    return sum ((a,b))*0.05 #sum adds together whatever is in the tuple 

def myfunc(*args):#the *args parameter allows the function to take as many arguements as it wants in the form of a tuple, the name args is a placeholder, but used by convention
    for item in args:
        print(item)#prints whatever value is at item per iteration

def mytrunk(**kwargs):#**kwargs takes an arbitrary amount of keyword arguments in the form of a dictionary,the name kwargs is a placeholder, but used by convention
    for item in kwargs:
        if 'fruit' in kwargs:#looks for the 'fruit' key 
            print('Your fruit of choice is {}'.format(['fruit'])) #looks for the value to key fruit passed into the function 
        else:
            print('I did not find any fruit here')

def myluck(*args, **kwargs): #can accept both arguments and keyword arguements
    print ('I would like {} {}'.format(args[0],kwargs['food']))
            #takes args as tuple and kwargs as the key value pairs
print(myluck(10,20,30, fruit="orange",food="eggs",animal='dog'))

#write a function that computes the volume of a sphere given its radius
import math

def vol(rad):
    return (4/3)*math.pi*rad**3

print(vol(2))

#write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num in range (low,high+1): #finds if num is in range of low and high. Since in range is at then one below(so high-1) we add one to offset the loss
        print(f'{num} is in the range of {low} to  {high}')
    else:
        print (f'{num} is not in the range of {low} and {high}')

#same function as above but returns a boolean

def ran_bool(num,low,high):
    if num >= low and num <= high:
        return True
    return False

#write a function that  count the number of lowercase letters and uppercase letters

def up_low(str):
    count_low = 0
    count_high = 0

    for i in range(len(str)):
        if str[i].islower(): #dont need ==True because islower() is a boolean and will return true if condition is met
            count_low+=1
        elif str[i].isupper():
            count_high+=1
        else:
            pass
    print (f'The number of capital letters is {count_high} and the number of lowercase letters is {count_low}')

#write a function that takes a list and returns a new list with unique elements of the first list

def unique_list(lit):
    set_list = set(lit) #get unique values only
    new_lit = []
    for i in set_list:
        new_lit.append(i) #append unique values to new list
    return new_lit

#write a function to multiply all numbers in a list
import operator #imports the operator tools that has the multiply operator
from functools import reduce #imports the reduce method
def multiply(num):
    return reduce(operator.mul,num) #reduce applies the function to every iterable, at first step takes first two in sequence,then takes that value and the next item and apply the function, so on and so forth

    #or you can do this
    #x=num[0]
    #for i in num:
    #    x = x * i
    #return x


#write a python function that checks whether a word or phrase is a palindrome or not

def palindrome(s):
    #this is the long way

    #reverse_word = ""
    #count = -1

    #for i in range(len(s)):
    #    reverse_word = reverse_word + s[count]
    #    count -= 1

    #if reverse_word == s:
    #    return True

    #return False

    #this is the fast way

    s = s.replace(' ','') #replace all the whitespace with nothing
    return s == s[::-1] #if s is equal to the opposite of s

#write a python function to check whether a string is pangram or not (assume the string passed in does not have any punctuation)
        #note: pangrams are words or sentences containing every letter of the alphabet at least once.
import string


def pangram(str,al = string.ascii_lowercase):
    #long way
    str = str.replace(" ","")

    def ascii_return(str): #function that returns ascii numbers of string and puts it in slist
        x=[]
        w= str.lower() #making sure that the sentence only has lowercase letters
        
        for i in range (len(str)):
            y = ord(w[i]) #turn letter to ascii number
            x.append(y) #append ascii number to list
        return x

    ascii_list = set(ascii_return(str)) #create a variable to store the asciis for the string, and only take in the unique items.
    ascii_al_list = ascii_return(al) #create a variable to store the asciis for the alphabet
    
    if len(ascii_list) == 26: #if there are 26 unique items in the new list set, the str is a pangram 
        return True
    else:
        return False

#short way
# alphaset = set(al) this create a set of the alphabet letters
#str = str.replace(" ","") this replaces the whitespace in the sentence with nothing
#str = str.lower() this turn all letters to lowercase
#str = set(str) this turns the sentence into a set, only getting the unique letters
#return str = alphaset if the str set is the same as the alphaset than it will return true

## print (pangram('Fickle jinx bog dwarves spy math quiz'))

#this is code i made to remove whitespace, but i know use .replace()
#for i in range (len(str)):#removing all spaces from the list
#        try:
#            ascii_list.remove(32) #if the item is a blackspace(ascii of 32) remove it 
#        except:
#            pass #if ascii isnt a blackspace, this handles the error

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for i in map(square,my_nums): #map applies the function placed in its first paremeter (so square in this case) to every iterable in the list at its second parameter
    #so it will apply square to every list object in my_nums
    print (i)


print (list(map(square,my_nums))) # this returns the original list 

def splicer (mystring): #simple program that returns whether word has even number of letters
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

print (list(map(lambda str: str[::-1],names)))


print (list(map(splicer,names))) #map applies splicer to every iterable of names and prints them all in  a list

def check_even(num):
    return num %2 == 0

mynums = [1,2,3,4,5,6]

print (list(filter(lambda num:num%2==0,mynums))) #similar to below, but a lambda expression instead

print (list(filter(check_even,mynums))) #filter takes each iterable and returns only the ones that pass the condition, filter only works on functions that return a boolean
#either use a for loop similar to map to return values, or transform to a list, otherwise python will just point to memory of the filter function
 
#def square(num): return ** 2
#the above function does the same as the lambda function
lambda num:num ** 2 #dont need a return num ** 2 because lambda excepts a return after colon
#lambda, aka anoymous function because its a function you only used a small number of times
#lambda generally used with map and filter or similar functions

print (list(map(lambda num: num**2,  mynums))) #using lambda to do map, lambda acts as the functino, so in this case, it squares the item at each iterable of mynums

x = 25

def printer ():
    x = 50
    return x

print (x)

print (printer())

#function practice that was supposed to get done before the methods practice

#lesser of two evens: write a function that returns the lesser of two given numbers if both number are even, but returns the greater if one or both numbers are odd

def lesser_of_two(a,b):
    if a>b:
        return b
    else:
        return a 

#write a functin that takes a two word string and returns true if both words begin with same letter

def animal_crackers(text):
    compare = text.split()
    return compare[0][0] == compare [1][0]

print (animal_crackers("Krazy Kangaroo"))

#write a function that returns true if either of the numbers is 20 or if the sum of the numbers is twenty
def makes_twenty(n1,n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    return False

print(makes_twenty(1,20)) 

def mcdonald(name):
    newname = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return newname 

print (mcdonald("macdonald"))

#return a sentence but in reverse order

def yoda(text):
    splitsen = text.split()
    newlist = []
    count = -1
    for i in range (len(splitsen)):
        newlist.append(splitsen[count])
        count -=1
    return " ".join(newlist)

print (yoda("I am Home"))

#given an integer n reutrn true if n is within 10 of either 100 or 200

def almost(n):
    if n >=90 and n <= 110 or n >=190 and n <=210:
        return True
    return False

#given a list of ints reutrn true of the array contains a 3 next to a 3 somewhere

def has_33(nums):
    for i in range (len(nums)-1):
        if nums[i] == 3:
            if nums[i+1] == 3:
                return True
    return False

#given a string, retuyrn as tring where for every character in the orgnal there are three characters

def paper_doll(text):
    new_word =""
    for i in range (len(text)):
        new_word = new_word + text[i] + text[i] + text[i]
    return new_word

print (paper_doll("Hello"))

#given three ints between 1 and 11, if there sum is less than or equal to 21, return their sum. If their sum exceeds 21 and theres an eleven, reduce the total sum by 10
# Finally, if the sum exceeds 21,return bust

def blackjack(a,b,c):
    if a + b + c <= 21:
        return a+b+c
    elif a+b+c > 21 and a == 11 or b == 11 or c == 11:
        if (a+b+c)-10>21:
            return "Bust"
        else:
            return (a+b+c) - 10
    elif a+b+c>21:
        return "Bust"
    

print (blackjack(9,9,9))

#return the sum of the numbers in the array,except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# RETURN 0 FOR NO NUMBERS

def summer_69(arr):

    remove_list = []
    sum_list=[]
    new_count = arr

    if (len(arr)) > 0:
        for i in range (len(arr)):
            if arr[i] == 6:
                remove_list.append(arr[i])
                new_count = arr[i+1:]
                for x in range (len(new_count)):
                    if new_count[x] == 9:
                        remove_list.append(new_count[x])
                        break
                    else:
                        remove_list.append(new_count[x])

    for i in arr:
        if i not in remove_list:
            sum_list.append(i)
        elif i in remove_list:
            remove_list.remove(i)
    
    return sum(sum_list)


print (summer_69([5,4,5,6,7,9,8,9,6,7,9,8,4,8,6,7,7,9]))

#write a function that takes in a list of integers and returns True if it cointains 007 in order

def spy_game(nums):
    for i in range (len(nums)-2):
        if nums[i] == 0:
            if nums[i+1] == 0:
                if nums [i+2] == 7:
                    return True
    return False

print (spy_game([1,0,2,4,0,5,7,0,0,7]))


#write a function that returns the number of prime numbers that exist up to and including a given number

#how imma do it :
#have loop that goes through the input number
#then have to iterate through each iteration of number, eg. if im at 50 of 100, ill have to iterate from 2 to 49
#then i have to divide the orignal iteration by the newer iteration using float(old iteration/new iteration) == int(old iteration/new iteration). If that is true
#add 1 to count. Since prime numbers are only divisible by 1 and themselves, and the new iteration should always skip 1(ill have to use if statement here) and whatever number the old
#iteration is, the count for prime numbers should be 0. if, at the end of the second for loop, count is greater than 0, it means that the number that was the old iteration, 50 in this case,
#was divisible by something other than itself and is therefor not a prime number. If a number is a prime number, the count should be 0 at the end of the second loop
#and so i'll add one to the variable prime_count. this script should iterate through each number in num, then each iteration so i should have the amount of prime numbers in num
#if i find a number to be a prime number i can append it to a list to display at the end

def count_primes(num):
    
    count =0
    prime_count =0
    prime_list = []

    for x in range (num): #iterate thorugh user input number 
        for y in range (x): #for loop to iterate through each iteration to divide it by each number (thats not 1 and itself) to see if the numbers prime
            if y>1: #as to not divide a number by 1
                if float(x/y) == int(x/y): #if number at oringal iteration divided by number at new iteration results in whole number 
                    count +=1 #add 1 to count
                    break #end loop
                else:
                    count = count #otherwise do nothing
        if x == 0 or x ==1: #0 and 1 are not prime numbers 
            prime_count = prime_count
        elif count == 0: #if count is zero by end of loop
            prime_count +=1 #then number must be prime so add one to prime count 
            prime_list.append(x) #append that number to list
        count = 0 #return count to zero 
    return prime_count, prime_list

print (count_primes(1000))

#displaying user information

print ([1,2,3]) 

def display(row1,row2,row3): #this displays the three input in three rows 
    print (row1)
    print (row2)
    print (row3)

row1 = [" "," "," "] #creating variables to be used as rows for the display function
row2 = [" "," "," "]
row3 = [" "," "," "]

print (display(row1,row2,row3))

#row2[1] = "x" #change row 2 index 1 (so the middle space) into an x 

print (display(row1,row2,row3))

# result = input ("Please enter a value: ") #this is how you get an input from a user, defautls to string

#result_int = int(result) #converts result into integer

print (result)

print (type(result)) #how to check type of variable

print (display(row1,row2,row3))
#to make this tic tac program work you would need to loop until someone gets tic tac toe or all the spaces are full 

#position_index = int(input("Choose an index position: "))
#row_position = int(input("Choose a row to change") )

#if row_position == 1:
#    row1[position_index] = "x"
#elif row_position == 2:
#    row2[position_index] = "x"
#elif row_position == 3:
#    row3[position_index] = "x"

#print (display(row1,row2,row3))

def user_choice(): #useing this function to check user input
    choice = 'Wrong'
    while choice.isdigit() == False or int(choice) <0 or int(choice) >10: #checks if variable is digit or can be turned into a digit

        choice = input("Please enter a number (0-10), not a string: ") #will ask this input as long as option is not digit

        if choice.isdigit() == True and (int(choice) < 0 or int(choice) > 10): #isidigit doesnt register negative numbers as digits, so a negative number will get the digit false print below
            print ("Please enter a number greater than zero and less than ten")
        if choice.isdigit() == False: #returns this string if input is not digit
            print ("Please enter a number not a string")
        
    return int(choice)

some_value = '100'

some_value.isdigit() #will check if some_value can be turned into int, and if so return true

int(some_value)

#creating mulitple functions to create a program that involves simple user interaction
game_list = [0,1,2]

#this function will be used to dispay the user interface
def display_game(game_list):
    print ('Here is the current list: ')
    print (game_list)

#this function asks the user to pick a position to change within the list
def position_choice():
    choice = 'wrong' #choice starts off wrong to start the while loop
    while choice not in ['0','1','2']: #while choice is not 0,1,2 (which are the index positoins of the game list), 
        choice = input("Pick a position(0,1,2): ") #ask user to pick a postion between 0,1,2
        if choice not in ["0",'1','2']: #if that choice is not 0,1,2
            print ("Sorry, invalid choice!") #print this statement
    return int(choice) #return the user choice as an int 

def replacement_choice(game_list, position):
    #asking for string to place at index position requested in the position_choice function 
    user_placement = input("Type a string to place at position: ")
    #updating the game_list so the chosen string is placed at the index position chosen 
    game_list[position] = user_placement
    #return updated game list
    return game_list

def gameon_choice():
    choice = 'wrong' #choice starts off wrong to start the while loop
    while choice not in ['Y','N']: #while choice is not 0,1,2 (which are the index positoins of the game list), 
        choice = input("Keep playing? (Y or N): ") #ask user to pick a postion between 0,1,2
        if choice not in ['Y','N']: #if that choice is not 0,1,2
            print ("Sorry, I don't understand, please choose Y or N") #print this statement
    if choice == "Y":
        return True
    else:
        return False

game_on = False #to be used in the while loop, while game_on is true run loop
game_list = [0,1,2] #game list to be used 

while game_on: #loop that runs the game
    display_game(game_list) #display game using the gamelist
    position = position_choice() #create variable position that takes in user chosen position from position choice function
    game_list = replacement_choice(game_list,position) #change game list to update game list using replacement choice function
    display_game(game_list) #display updated list
    game_on= gameon_choice() #ask user if they want to keep playing 

mylist = [1,2,3]

myset = set()

print (type(myset))

class Dog():
    #class object attribute
    #same for any instance of a class
    species = 'mammal'
    def __init__ (self, breed,name,):
            #below is an attribute, which is a characteristic of an object, not an actual method
        self.breed = breed
        #we take in the parameter, in the case below it would be name, and assign it to the attribute, which is self.name, self being the instance of the class and name being the attritbute
        self.name = name
    #Operations/Actions ----> Methods
    def bark(self,number):                                      #need a self.name because its referencing the instance of the class #dont need self.number because its not referencing an instance, just a user parameter
        print ('WOOF! My name is {} and the number is {}'.format(self.name,number))


my_dog = Dog('Lab','Frankie') #this is an instance of the class dog, aka an object of the class dog

print(my_dog.breed) #can call specific attributes to see what they are
print(my_dog.name)
print(my_dog.bark(10))

class Circle():
    #Class object attribute
    pi = 3.14 

    def __init__(self,radius=1):
        self.radius = radius #creating a radius object that can be changed through parameters
        self.area = radius * radius *self.pi #self.pi uses self because its calling a particular instance of the class, but you can use Circle.pi because its a class attribute

    #Method
    def get_circumference(self): #takes in the object as the parameter since object already has radius 
        return self.radius * Circle.pi * 2

my_circle = Circle(30) #Circle(30) is giving the radius a value of 30 for the mycircle object

print(my_circle.pi)
print(my_circle.area)
print(my_circle.get_circumference())

class Animal(): #creating Animal class

    def __init__ (self): #define the attribute for creating the object
        print ("Animal Created") #this will be printed everytime an object created

    def who_am_i(self): #a method that prints I am an animal everytime a function is called
        print("I am an animal")
    def eat(self):
        print ("I am eating")

class Dog(Animal): #creating a dog class that inherits from the Animal class
    def __init__(self): #initializing the object
        Animal.__init__(self) #creating an instance of the animal class when creating an instance of the dog class
        print ('Dog Created')
    def bark(self):
        print ("Woof!")
    def eat(self):#rewriting the who_am_i method from the Animal class 
        print ("I am a dog and eating")


myanimal = Animal()#creating an Animal object

myanimal.who_am_i()
myanimal.eat()

mydog = Dog() #creating a mydog object thats an instance of the dog class, but because of inheritance, it gains the methods and init of the Animal class

print(mydog.who_am_i()) #A method from the dog class
print(mydog.eat())#a method from the orignal Animal class

class Dog(): #create dog class
    def __init__(self,name): #init object, but need name parameter
        self.name = name #name attribute = name
    def speak(self): #speak method that returns the object name and says woof
        return self.name + ' says woof!'

class Cat(): #create cat class
    def __init__(self,name):#init object, parameter is name
        self.name = name #name attribute
    def speak(self):
        return self.name + ' says meow!' #speak method that prints name and says meow

niko = Dog('niko') #create a niko dog object with the name niko
felix = Cat('felix') #create a felix cat object with the name felix

print (niko.speak()) #can call the speak method from the dog class and because niko is an instance of the dog class, uses the method from the dog class
print (felix.speak())#can call the speak method from the cat class and because niko is an instance of the cat class, uses the method from the cat class

for pet in [niko,felix]: #for loop that iterates thorugh the two objects

    print (type(pet)) #shows the type of object
    print (pet.speak()) #print speak function, output depends on the what class instance is being used 

def pet_speak(pet): #calls an object
    print(pet.speak()) #calls a method, output depends on the objects inheritance

print (pet_speak(niko))   

class Animal (): #this class is a shell class, not meant to be used to create objects 
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method") #skeleton method, raises an error when tried to be used

class Dog(Animal):#dog class inherits from the animal class , creates an object using the parameters from the animal class

    def speak(self):  #speak method that returns the name of the object and says woof
        return self.name + ' says woof!'
                #need self.name because your need to refer to the attribute of the current instance
class Cat(Animal): #same thing as the above class
    def speak(self):
        return self.name + ' says meow!'

fido = Dog('fido')
isis = Cat('isis')

print (fido.speak())

mylist = [1,2,3]

class Sample():
    pass

mysample = Sample()

print (mysample)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages

b = Book('Python Rocks', 'Jose', 200)

print (b)

#distance formula : d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#slope formula : (y2 -y1) / (x2 -x1)

import math

class Line():

    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2

    def distance(self):
        return math.sqrt((self.c2[0] - self.c1[0])**2 + (self.c2[1] - self.c1[1])**2)

    def slope(self):
        return ((self.c2[1] - self.c1[1])/(self.c2[0] - self.c1[0]))

c1 = (3,2)
c2 = (8,10)

li = Line(c1,c2)

print (li.distance())

print (li.slope())

class Cylinder():

    def __init__ (self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

cyl1 = Cylinder(2,3)

print (cyl1.volume())
print (cyl1.surface_area())

class Account ():

    def __init__ (self, owner,balance = 0):
        self.owner = owner
        self.balance = balance
        print (f'Owner Account: {self.owner}')
        print (f'Account Balance: ${self.balance}')

    def __str__ (self):
        return f'Owner: {self.owner} \nBalance: ${self.balance}'

    def deposit (self, deposit):
        self.balance = self.balance + deposit
        print (f'Deposit accepted. Account has ${self.balance}')

    def withdraw (self, withdraw):
        if withdraw > self.balance: 
            print (f'Funds unavailable. Account has ${self.balance}')
        else:
            self.balance = self.balance - withdraw
            print (f'Withdrawal accepted. Account has ${self.balance}')

acct1 = Account ('Jose', 100)

print (acct1)
print (acct1.owner)
print (acct1.balance)
print (acct1.deposit(50))
print (acct1.withdraw(75))
print (acct1.withdraw(500))

def add (n1,n2):
    print (n1+n2)

print (add(10,20))

number1 = 10
#number2 = int(input('Please provide a number: '))

#add(number1,number2)
print ("Something happened!")

try:
    #Want to attempt this code
    #May have an error
    result = 10+'10'
except: #if the try statement doesnt work, excute code in the except block
    print ("Hey, it looks like your aren't adding correctly")
else: #if the try doesnt find an error, exectue the code in the else block
    print ("Add went well!")
    print (result)

try: #try to attempt
    f=open('testfile','r')
    f.write('Write a test line')
except TypeError: #occur when an error, in this case a Type Error which has to do with variable and object types
    print ('There was a type error')
except OSError: #OS error has to do with reading and writing files and other things im not sure of
    print('Hey you have an OS error')
finally: #finally block will always run 
    print ('I always run')

def ask_for_int ():
    while True: #while true
        try: #execute the try block
            result = int(input("Please provide number: "))
        except: #if theres an error
            print ('Whoops! That is not a number') #print statement
            continue 
        else: #if theres no error, print statement and then have break (only way to exit a while true loop)
            print ('Yes, thank you')
            break #only way to exit a while true statement
        finally: #the finally code will always execute
            print ("I'm going to ask you again") #sometimes you dont want a finally statement because its always executes

try:
    for i in ['a','b','c']:
        print (i ** 2)
except TypeError:
    print ("Error. Expecting a number")

x = 5
y=0


try:
    z = x/y
except ZeroDivisionError:
    print ('Answer is 0')
finally:
    print ('All done')


def ask():
    while True:
        try:
            x = int(input('Please enter an integer: ')) 
        except TypeError:
            print ('Please enter a number!')
        else:
            print (f'Thank you. {x} squared is {x ** 2}')
            break
        

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card(): #card class creates card objects. Creates a card with a suit and rank(string number), and finds the value corrosponding with that rank from the value dictionary

    def __init__ (self,suit,rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank] #self.value attribute gets its value from the values dictionary, which is a global variable, using rank as the key

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck(): #deck class creates 52 card objects, holds all cards as a list, shuffle deck and hand out cards from deck
    
    def __init__ (self):

        self.all_cards = [] #create a list that will be used to append card objects

        for suit in suits: #iterate through every suit, but for every suit
            for rank in ranks: #iterate thorugh every rank for every suit
                #create a card object for each rank in each suit
                created_card = Card(suit,rank)
                #then append that card object so the all cards list so that we get every rank at every suit in the list, creating a 52 card deck
                self.all_cards.append(created_card)

    def shuffle(self): #this method will suffle the deck object

        random.shuffle(self.all_cards) #random.shuffle is the same as doing from random import shuffle then doing shuffle(self.all_cards)

    def deal(self): #this deals one card at a time
        return self.all_cards.pop() #this will pop the card, printing its value and remove it from the deck object



new_deck = Deck() #create a deck

new_deck.shuffle() #shuffle a deck

my_Card = new_deck.deal() #the cards become the popped card from the deck

print (my_Card) #the card will be a random card from the deck
print (len(new_deck.all_cards)) #the length of the deck will be 51 because a card got popped 
print (new_deck.all_cards[-1]) #since the deck is randomized, the last card will be different than the last rank of the last suit defined as the global variables

class Player(): #class that encompasses all player actions and player environment

    def __init__(self, name): #create a player with a name and give them a list that will hold their cards
        self.name = name
        self.all_cards = []
    
    def remove_one(self): #remove one removes a card from the player deck
        return self.all_cards.pop(0) #pop at index 0 removes card from what would be the top of the deck

    def add_cards(self,new_cards): #add cards adds cards to the player deck (in this case the list)
        
        if type(new_cards) == type([]): #if the players are at war and there are multiple card objects ( if new_cards is a list )
            self.all_cards.extend(new_cards) #use extend to add that list to the all_cards list that holds the players cards. Extend is like zip, lets you add lists without having a nested list in the main list
        else:
            self.all_cards.append(new_cards) #otherwise, if there is just one card, append it to the bottom of deck, in this case the end of the list since it wont add a nested list

    def __str__(self): #defines the string repersentation of the object
        return f'Player {self.name} has {len(self.all_cards)} cards. '

new_player = Player('Jose') #create player object

print (new_player)

new_player.add_cards(my_Card) #adding a card object to player deck

print(new_player) #should print Jose has one card because i added a card object to the deck

print (new_player.all_cards[0])#showing what card is in the deck object at index 0, which, in this use case, would be the top of the deck

print(my_Card)

new_player.add_cards([my_Card,my_Card,my_Card])#add three card objects to player deck

print (new_player) #should show the player as having 4 card objects in the deck object

new_player.remove_one() #this pops a card from the players deck at the index position zero(this is specfied in the method)

print (new_player)#should show the player as having 3 cards 


def hello():
    return 'hello'

print (hello()) # brackets execute a functino. When you dont put brackets it points to where the function is but doesnt execute it

greet = hello #greet becomes assigned the hello function. Dont put hello () because brackets are used to exectue a function

print (greet()) #now when you call the greet function with the brackets it will execute the hello function because we set hello to greet. Remeber to exectue a function you need the brackets

def hello (name = 'Jose'):
    print ('The hello() function has been excuted!')
    def greet():
        return '\t this is the greet () function inside hello'
    def welcome ():
        return '\t this is welcome () inside hello'
    
    print ('I am going to return a function')

    if name == 'Jose':
        return greet
    else:
        return welcome


my_new_func = hello()
print (my_new_func())


def cool ():

    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func = cool()

print (some_func())


def hello():
    return 'Hi Jose!'

def other(some_def_function):
    print ('Other code runs here!')
    print (some_def_function())

print (other(hello)) #when im passing in the function, i dont use brackets because i dont want to execute the function in the call. It will execute in the other function

def new_decorator(original_func): #this will take a function and return the wrap func function which warps the parameter function in text

    def wrap_func():

        print ('Some extra code, before the original function')

        original_func()

        print ('Some extra code after the orginal function')

    return wrap_func

def func_needs_decorator():
    print ('I want to be decorated')

decorated_func=new_decorator(func_needs_decorator)

print (decorated_func())

@new_decorator #@new_decorater just calls the new_decorator function and passes in the func_needs_decorator into it so when you call func needs decorator u get the wrap func output
def func_needs_decorator():
    print ('I want to be decorated')

print (func_needs_decorator())


def create_cubes(n):
    for x in range(n):
        yield x**3
    
for x in create_cubes(10):
    print (x)

def gen_fibon(n):

    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b, a+b

for number in gen_fibon(10):
    print (number)


def simple_gen():
    for x in range(3):
        yield x

for x in simple_gen():
    print (x)

g = simple_gen()

print (next(g))
print (next(g))

s = 'hello'

for letter in s:
    print (letter)

s_inter = iter(s)

print (next(s_inter))
print (next(s_inter))
print (next(s_inter))

#create a generator that generates the squares of number up to some number N

def gensquares(n):
    for x in range(n):
        yield x**2

for x in gensquares(10):
    print (x)

#create a generator that yields n random numbers between a low and high number

import random

def rand_num(low,high,n):
    for x in range(n):
        yield (random.randint(low,high))

for x in rand_num(1,10,12):
    print (x)

#the the iter() function to convert the string below to an iterator

h = 'hello'
h_iter = iter(s)
print (next(h_iter))
print (next(h_iter))
print (next(h_iter))

#explain a user case for a generator using a yield statement where you would not want to use a normal function with a return statement

#i guess if you dont need to store the value and only need to generate at a certain instance, then you wouldnt need a return statement
#**actual answer** return sends a specfied value back to its caller whereas yield can produce a sequence of values. We should use yield when we want to iterate over a sequence
#but dont want to store the entire squence in memory

from collections import Counter #counter method

mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3]

print (Counter(mylist))#counter displays how often each unique character appears

mylist =['a','a','10','10']

print(Counter(mylist))

print(Counter('aadadwadwdadawd'))

sentence = 'how many times does each word show up in this sentence'

print (f' this is sentence lower().split {Counter(sentence.lower().split())}') #counts how many times each word shows up split at the white space

letters = 'aaabbbccccccccdddddddd'
c = Counter(letters)

print(c)

print(c.most_common()) #prints the most commons characters first, and also give key value pairing(common character:times it appears)

print(list(c))

from collections import defaultdict #gives an unassigned dictionary key a deafault value so you dont get an error if you call a wrong key
from collections import namedtuple #allows you to find create tuples in a similar way to objects so you can sort by the tuple name and whatever key you want to find the value for

d = {'a':10}

print(d['a'])

d = defaultdict(lambda:0)

d['correct']=100

print(d)

d['WRONG KEY!']

print(d)

mytuple = (10,20,30) #create tuple

print(mytuple[0]) #call tuple at index 0

Dog = namedtuple('Dog',['age','breed','name']) #create a named tuple object that allows you to find keys and their values

sammy = Dog(5,'Husky','Samm') #sammy is tuple object dog with the three values needed to create a tuple list

print (sammy)

print(sammy.breed) #you can call the parameters of named tuple the same way you would call attributes of objects

import os

print(os.getcwd())
f = open('practice.txt', 'w')
f.write('This is a test string')
f.close()
#os.system('practice.txt') #this actually opens the file in its native extension
os.system('D:\Code\python')
print(os.listdir())

import shutil #lets you move files

import webbrowser #opens deafult web browser pointed to the file, which will dispaly images

import subprocess
def openshit():
    subprocess.Popen(r'explorer / select, "D:\Code\python"') # this opens the path in the file explorer
#webbrowser.open('practice.txt') #will disply the text file as an image in the web browser


#shutil.move('practice.txt', 'D:\Code\python\extrashit',os.getcwd()) #moves file to designated path

#import send2trash this module is supposed to send files to recycling bin

#send2trash.send2trash('practice.txt')
print('\n')
print('\n')
print('\n')
for folder,sub_folders,files in os.walk("D:\Code\Example_Top_Level"):
    print (f'currently looking at folder {folder}')
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print (f'Subfolder: {sub_fold}')
    
    print ('\n')
    print ("the files are: ")
    for f in files:
        print (f'File: {f}')
    print ('\n')

import re #can look for regular expression patterns

text = "The agents phone number is 408-555-1234.Call soon!"

pattern = 'phone'

re.search(pattern,text) #will search for pattern in text and give you if the pattern was found and what that patterns spans to(the index position where it starts and stops)

pattern = 'NOT IN TEXT'

re.search(pattern,text) #this should return nothing as there is no pattern 'not in text' in this text

pattern = 'phone'

match = re.search(pattern,text) #same as before, will give you span of phone but saves to variable match

print(match.span()) #method gives you index location of the span

print(match.start()) #where the span starts, so whatever index position is of the first appearance of the pattern youre looking for

print(match.end()) #where the span ends

text = 'my phone once, my phone twice'

match = re.search('phone',text) #only returns the first match, not all of them so phone will match here will only return the first match

print(match)

matches = re.findall('phone',text) #findall finds all matches of the pattern in the list

print(matches)

print(len(matches)) #prints the legth of matches, so how many match objects have been found and placed into the matches variable

for match in re.finditer('phone',text): #iterate through the text and returns each match object thats found
    print(match)

text='My phone number is 408-555-1234'

phone = re.search(r'\d{3}-\d{3}-\d{4}',text) #this uses quantifiers to find the pattern, so \d is looking for a digit and {} is looking for the number of times that character appears

print(phone)

phone.group() #returns the number object as the actual number

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern,text)

print(results.group())

print(results.group(3)) #returns back group corrosponding to the compile groups, so this will return \d{4} pattern of text. If i wanted the whole number i would use .group()

re.search(r'cat|dog','The cat is here') #| is or operator so it looks for cat or dog

re.findall(r'.at','The cat in the hat sat there') #the period infront of at acts as a wildcard, so this finall wll return cat hat and sat since the period is just a placeholder for any character that has at for the last two letters and one character infornt of it

re.findall(r'^\d',"1 is a number")# ^, in this context, looks to see if the entire string starts with a \d (digit)

re.findall(r'\d$',"1 is a number")# $ looks to see if the string ends with a \d (digit)

phrase = 'There are 3 numbers 34 inside 5 this sentence'

pattern = r'[^\d]' #this means to exclude any digits

re.findall(pattern,phrase) #this will return phrase without any numbers

pattern = r'[^\d]+' # the plus sign will return the words back together in groups,excludign the digits

test_phrase = 'This is a string! But it has puncutation. How can we remove it?'

clean = ' '.join(re.findall(r'[^!.? ]+',test_phrase)) #gets rid of the characters within the square brackets (including the space) in the test phrase and uses ' '.join to join the different groups together agian as a sentence

print(clean)

text = 'Only find the hyphen-words in this sentence. But you do not know how long-ish they are'

pattern = r'[\w]+-[\w]+' # r indicates regular expression starting, \w is an alphanumeric character, + means character appears one or more times, - is the hypen we're looking to find, [\w]+ repeats agian, and this should give us back the words with hyphens in the middle of them

re.findall(pattern,text)

text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

pattern = r'cat.+[^.?! ]' #this pattern will find a word that starts with cat and looks for however many characters are after and also removes any punctuation

re.search(r'cat(fish|nap|erpillar)',text) #this looks for cat then either fish or nap or erpillar using the |

print(re.findall(pattern,texttwo))

import timeit
import time

def func1(n):
    return[str(num) for num in range(n)]

def func2(n):
    return list(map(str,range(n)))

print(func2(10))

#current time
start_time = time.time()
#run code
result = func1(1000000)
#current time after running code
end_time = time.time()
#elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)

start_time = time.time()
#run code
result = func2(1000000)
#current time after running code
end_time = time.time()
#elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)
#**********************************************************************************************************triple quotes creates a multiline string important to rememeber this
import timeit
def timed(): #moved this into a function so i dont have to comment it out since it takes to long to run
    #timeit function only takes arguements as strings to have to create multiline strings with the function and function calls
    statement = ''' 
    func_one(100)
    '''
    #the setup is where you put the logic that timeit will be using for testing
    setup = '''
    def func_one(n):
        return [str(num) for num in range(n)]
    '''
    print(timeit.timeit(statement,setup,number = 100000)) #timeit.timeit takes in the statement(function call), setup(function logic), and the numbner of times it will test the time(number = ?)

def timed2():
    statement2 = '''
    func2(100)
    '''

    setup2 = '''
    def func2(n):
        return list(map(str,range(n)))
    '''

    print(timeit.timeit(statement2,setup2,number = 100000))

f = open('fileone.txt','w+') #creates file, w+ is for reading and writing
f.write("one file") #named file
f.close() #close file

f = open('filetwo.txt','w+')
f.write("two file")
f.close()

import zipfile

comp_file = zipfile.ZipFile("comp_file.zip",'w') #creates a zip folder that is able to written to

comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED) #put a compressed version of file one to the zipfile
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)#wput a compressed version of file two to the zipfile
comp_file.close() #close file
#we now have a zip file that has two compressed files in it
zip_obj = zipfile.ZipFile('comp_file.zip','r') #create a zip variable, point it to the zip file that will be extracted from, since we're extracting we can open in read
zip_obj.extractall('extracted_content') #extract everything from the zipfile, to whatever folder we want to extract it too(extracted content)
#we now have a folder that has two file in it that were extracted from the zip file 

import shutil
pwd = os.getcwd()

print(pwd)

dir_to_zip = 'D:\Code\python\extracted_content' #pointing to a directory that we want to turn into a zipfile

output_filename = 'example' #creating an output filename example

shutil.make_archive(output_filename,'zip',dir_to_zip) #this creates an acrhived version(zip) of directory named output_filename('example')
shutil.unpack_archive('example.zip','final_unzip','zip') #this unpacks an archive, takes filename you wish to unpack, then the extract directory that your extracting to, and third parameter is format



