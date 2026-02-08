#inheritance: this is the oops princple to work with that 

##there are five types of inheritance :
#single
#multiple 
#maltilevel
#hirarecal
#hybrid

##single inheeritance:

class parent:
    def method1(self):
        print("i am parent")

class child(parent):
    def method2(self):
        print("i am child")
        
##multiple: one child two parents 

class father:
    def method1(self):
        print("i am father")

class mother:
    def method2(self):
        print("i am mother")

class child(father,mother):
    def method3(self):
        print("i have my parents")
        
##multi level inheritance : will have all the grandfather and father methods and properties 

class grandfather:
    def method1(self):
        print("i am father")

class father(father):
    def method2(self):
        print("i am mother")

class child(mother):
    def method3(self):
        print("i have my parents")        
        
##hireharical : one parent one or more child

class parent:
    def method3(self):
        print("i have my parents")   
        
class child1(parent):
    def method3(self):
        print("i have my parents")   
        
                        
class child2(parent):
    def method3(self):
        print("i have my parents")       

## hybrid inheritence: this is the combination of one or more inheritence

class grandparent(mother):
    def method3(self):
        print("i have my parents") 
        
class parent1(grandparent):
    def method4(self):
        print("parent one")
 
class parent2:
    def method3(self):
        print("i have my parents")    
        
class child(parent1,parent2):
    def method1(self):
        print("i am child")
        
        
##mro: method resolution order : based on this rule the method in the inheritence will execute if we have same method in the different classes                                         
                            
                
                        