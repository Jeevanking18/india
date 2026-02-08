import  string

one=string.ascii_lowercase
two=string.ascii_uppercase
loweranduppercase=string.ascii_letters
digitsconstant=string.digits ##only numbers
hexdigits=string.hexdigits ##numbers and alphabets combinatiion
octdigits=string.octdigits ##'012334567'
whitespace=string.whitespace ## prints the white spaces 
punctuation=string.punctuation ##special charecters 
printable=string.printable ##combination of the

####string module methods:
capwords=string.capwords(string) ##this will work as it skips  at a space and next letter will become capital and join the sentence, by defualtly sep= none
##if we give any letter in spe=e, so it will split hear and rejoin the sentence.
 

name=input("enter the name:")

for char in name:
    if char==loweranduppercase:
        print(char)
    else:
        print("billa")  
print(one)          