#File: homework1.py
#variables and datat types

a=10
print(a)
print(type(a)) #a is an integer, a whole number with no decimals
b=1.5
print(b)
print(type(b)) #b is a float, number that has a decimal place
c=3j
print(c)
print(type(c)) #c is a complex, a number with real and imaginary parts
d="hello"
print(d)
print(type(d)) #d is a string, sequence of characters inside ""
e=[1,2,3]
print(e)
print(type(e)) #e is a list, multiple items within a single variable
f={"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dictionary, stores data in key-value pairs
g=(1,2)
print(g)
print(type(g)) #g is a tuple, ordered list of unchangable items stored in a variable
h=["apple", "banana", "strawberry" ]
print(h)
print(type(h)) #h is a list, multiple items within a single variable
i=True
print(i)
print(type(i)) #i is a boolean, which holds either true or false
j=None
print(j)
print(type(j)) #j is NoneType, represents the absence of a value
k=[True, "blue", 12]
print(k)
print(type(k)) #k is a list, multiple items within a single variable
l=str(14)
print(l)
print(type(l)) #l is a string, sequence of characters inside ""
m=1e4
print(m)
print(type(m)) #m is a float, number that has a decimal place
#9
#integer, float, complex, string, list, dictionary, tuple, boolean, NoneType
#E, H, K are all lists. M and B are floats. D and L are strings
#L was a string. The command str() turns anything inside the parentheses into a string.
n={"apple", "strawberry", "mango"}
print(n)
print(type(n)) #n is a set, unordered collection of unique elements

print(10>9) #true, 10 is greater than 9
print(10==9) #false, 10 is not equal to 9
print(10<=9) #false, 10 is not greater than 9
print(bool("abc")) #true, a string of letters
print(bool(123)) #true, a list of numbers
print(bool(["apple", "cherry", "banana"])) #true, list of items
print(bool(True)) #true, true inside the paranthesis
print(bool(False)) #false, false inside the paranthesis
print(bool(0)) #false, because 0 represents false in the binary
print(bool("")) #false, nothing inside the paranthesis
print(bool(" ")) #true, a space inside the paranthesis
print(bool(())) #false, no value inside the paranthesis
print(bool([])) #false, no value inside the bracket
print(bool({})) #false, no value inside the bracket
print(bool(True and False)) #false, and operator requires both conditions to be true
print(bool(True and True)) #true, both conditions are true
print(bool(False and False)) #false, both conditions are false
print(bool(True or False)) #true, one of the conditions is true
print(bool(True or True)) #true, one of the conditions is true
print(bool(False or False)) #false, neither of the conditions are true
print(bool(not(False))) #true, since the condition is not false
print(bool(not(True))) #false, since the condition is not true
#The true expressions are often lists or ‘True’ statements
#The parentheses with a space (“ “) surprised me because I thought it would return false.
#15>6 will return true because it is true that 15 is greater than 6
#15==10 will return false since 15 does not equal 10.

print(10+5) #15, + performs addition
print(10-5) #5, - performs subtraction
print(2*4) #8, * performs multiplication
print(6/3) #2, / performs division
print(5%2) #1, calculates the remainder of a division operation
print(3**2)#9, ** performs exponent
print(15//2)#7 // performs integer division (rounds to the nearest whole number)
print(5==2) #False, == checks if values are equal
print(10!=10) #false, != checks if values are not equal
print(2<5) #true, < checks if value is less than second value
print(12>5) #true, > checks if value is greater than second value
print(5<=6)#true, <= checks if value is less than or equal to
print(1>=10) #false, >=checks if value is greater than or equal to
x=5
x+=5
print(x)
x-=4
print(x)
x*=3
print(x)
#the operator and returns true only if both conditions are true
print(4>3 and 5<6)
#the operate or returns true if one or more of the conditions return false
print (4>3 or 5<4)
#the operator not reverses a truth value, turning true into false and vice versa
#/ performs division while // rounds any remainder to the nearest integer
#% displays the remainder while // rounds any remainder to the nearest integer
#% would be used
print(19%2)
#assigment operators assign a value to a variable
my_string="hello"
print(my_string) #prints:hello
print(my_string[0]) #prints:h
print(my_string[1]) #prints:e
print(my_string[2])#prints:l
print(my_string[3])#prints:1
print(my_string[4])#prints:o
print(my_string[-1])#prints o
print(my_string[1:3])#prints el
print(my_string[0:5:2])#prints hlo
print(len(my_string)) #prints 5
print(my_string+"goodbye")#prints hellogoodbye
print(my_string*7)#prints hellohellohellohellohellohellohello
name="Oski"
print("Hello, my name is", name)#prints: Hello, my name is Oski
print(f"Hello, my name is {name}")#prints: Hello, my name is Oski. 
#f-strings will automatically replace any variable inside {} with the variable's current value
#cd
#Changes directories. Use it to move from one folder to another
#example: cd desktop
#ls
#Lists all directories and files in the terminal
#example: ls (when inside python_decal_fa25)
#ls-a
#lists all files including hidden files
#example: ls-a (when inside python_decal_fa25)
#mkdir
#makes a new directory
#example: mkdir homework_screenshots
#cat
#displays file contents
#example: cat homework_screenshots
#pwd
#print working directory to see the path you took to the directory/file
#example: pwd (while inside a child directory)
#cd..
#moves up one level to parent directory
#example cd.. 
#cd~
#changes the current directory to the user's home directory
#example: cd~ 
#cp
#copies files and directories, duplicating the source file to a specified destination
#example: cp homework1 python_decal_fa25
#mv 
#moves or renames file or directories
#example: "homework1" homework1_part1
#rm
#removes/delets a file or directory from the system
#example: rm homework1_part1
#clear
#clears the terminal screen
#example: clear
#grep
#global regular expression print searches for specific patterns within files
#example: grep "python" homework1
#history: displays a list of previously executed commands. Example: history
#touch: creates an empty file. Example: touch homework2
#less: displays file contents page by page, allowing scrolling. Example: less homework2
#ls lists all items within a directory, ls-a lists all files as well as hidden files in a directory
#a hidden file is a file not shown by default. File names begin with a "."
#-l: lists with detailed information. Example: calling ls-l
#-i:  does a case-intensive search. Example: grep-i "python" homework1
#-r: recursive flag instructs command to operate on a directory/file's contents. Example: cp-r


