# Program to check if a number is prime or not

b = int(input("Enter any number :"))


if b > 1:
    for i in range(2,b):
        if (i % b)==0:
            print(b,"is not a prime number")
            break
    else:
        print(b,"is a prime number")    
else:
    print(b,"is not a prime number")       
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   