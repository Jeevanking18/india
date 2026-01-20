## map will store the operated values 

##map(functions,iterables)

##print functions print(), 
##print(i, end=" ") : this will print the individual print state next to it
##print(i, sep=",") : this is called saperater will seperates with what we provide 

input=list(map(int,input().split())) ## this will store the input in the list formate 

simpleList=[1,2,3,4,5]

def square(i):
    if i%2==0:
        return i**2
    else:
        return i**3
mapfun=list(map(square,simpleList))

print(mapfun)



