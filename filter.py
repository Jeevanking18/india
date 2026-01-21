##filter it is a built in function, it works on the functions andd iterables to filter the iterables in the fnctions and take the true value and return the result

##syntax: filter(function,iterable): iterable may be list, tuple ,string,set, dictionary,range,etc.

##it only filter the true returned values 

a=[2,3,4,5,6,7]

def fun(i):
    if i%2==0:
        return True

result=filter(fun,a)
print(list(result))    

##modules: modules are the sub programms which is divided the progrme in to the smaller parts and helps to understand the code easily without disturbing the remaining code
## example : i have normal calculater, i need to create a scientific calculater so i use the normal calculater and i will design the scientificc calculater