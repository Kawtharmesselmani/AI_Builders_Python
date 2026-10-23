# a=b 
# a!=b
# a>b
# a<b
# a>=b
# a<=b
# if condition is true 
# block of code will be executed
# a=10
# b=20
# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("a is less than b")
# else:
#     print("a is equal to b")


x=41
if(x>10):
    print("x is greater than 10")
    if(x>20):
        print("x is greater than 20")
        if(x>30):
            print("x is greater than 30")
            if(x>40):
                print("x is greater than 40")
                if(x>50):
                    print("x is greater than 50")
                else:
                    print("x is less than or equal to 50")
            else:
                print("x is less than or equal to 40")
        else:
            print("x is less than or equal to 30")
    else:
        print("x is less than or equal to 20")
        
        
age=20
has_lisence=True
if age>=18 and has_lisence:
    print("You can drive")
    
else:
    print("You cannot drive")
    

