pos = -1

def search(list , n):
    i = 0 
    
    for i in range(i,len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False

list = [9,2,6,3,7,1,12]

n = 1

if search(list,n):
    print('Found', pos + 1)
else:
    print('Not Found')
    
    

