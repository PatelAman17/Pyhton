#Pattern Example

a = int(input("Enter any number :"))

for i in range(0,a):
    for j in range(0,i+1):
        print("@", end="")
        
    print()               