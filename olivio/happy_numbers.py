def HappyNumber(figure):    

    digit = sum = 0   

    while(figure > 0):    
        digit = figure % 10 
        sum = sum + (digit * digit)    
        figure = figure // 10   
    return sum    
        
number = int(input("Olivio enter a number: "))    
result = number    
     
while(result != 1 and result != 4):    
    result = HappyNumber(result)   
     
if(result == 1):    
    print(number, " is a Happy Number Bruv!!!")   
else:    
    print(number, " is an Unhappy Number Bruv!!!")


