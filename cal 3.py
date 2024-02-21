#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def  add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def  power(a,b):
    return a**b
def divide(a,b):
    if b==0:
        print("float division by zero")
        return ("None")
    else:
        return a/b
def remainder(a,b):
    if b==0:
        print("float division by zero")
        return ("None")
    else:
        return a%b
        
        
        
#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choise):
    if(choise=="#"):
        return -1
    elif(choise=="$"):
        return 0
    elif(choise in ("+,-,*,/,^,%,")):
       
        while (True):
            n1=input("Enter first number: ")
            print(n1,)
            if n1[-1]=="$":
                return 0
            a=float(n1)
            n2=input("Enter second number: ")
            print(n2,)
            if n2[-1]=="$":
                return 0
            if n2[-1]=="#":
                return -1
            b=float(n2)
            break
        
        if(choise=="+"):
            print(a,"+",b,"=",add(a,b))
        elif(choise=="-"):
            print(a,"-",b,"=",subtract(a,b))
        elif(choise=="*"):
            print(a,"*",b,"=",multiply(a,b))
        elif(choise=="^"):
            print(a,"^",b,"=", power(a,b))
        elif(choise=="/"):
            print(a,"/",b,"=",divide(a,b))
        elif(choise=="%"):
            print(a,"%",b,"=", remainder(a,b))
        else:
            return -1
    else:
        print("Unrecognized operation")
            



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
 
  if(select_op(choice)==-1):
    #program ends here
    print("Done. Terminating")
    exit()


#Succsdd
