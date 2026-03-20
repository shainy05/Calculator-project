while True:
    print("Menu\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Power\n5.Division\n6.Remainder\n7.Exit")
    num=int(input("Enter the operation number:"))
    if num==7 :
        break
    elif 1<=num<7:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        if num==1:
            result=num1+num2
            print("Result",result,"\n")
            
        elif num==2:
            result=num1-num2
            print("Result",result,"\n")
            
        
        elif num==3:
            result=num1*num2
            print("Result",result,"\n")
            
        
        elif num==4:
            result=num1**num2
            print("Result",result,"\n")
        
        
        elif num==5:
            if num2!=0:
                result=num1/num2
                print("Result",result,"\n")
            
            else:
                print("Cannot divide by zero")
                
        
        elif num==6:
            result=num1%num2
            print("Result",result,"\n")

            
    else:
            print("Invalid choice\n")
