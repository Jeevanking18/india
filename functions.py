def function_one(a,b):
    return a+b

store=function_one(10,20)

print(store)

def even_odd(num):
    if num%2==0:
        print(f"This is even number {num}")
    else:
        print("This is not even number")
        
even_odd(2)    

## natural numbers

def natural_numbers(num):
    for i in range(1,num):
        print(i)
natural_numbers(11)        

def with_while(num):
    i=1
    while (i<num):
        print(i)
        i=i+1
with_while(8)        
                