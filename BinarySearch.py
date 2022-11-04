pos = -1
def search(list, n):
    
    l = -1
    u = len(list)
    for l in range(l,u):
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        elif l ==n:
            globals()['pos'] = l
            return True
        elif u == n:
            globals()['pos'] = u
            return True
    return False

list = [1,2,3,4,5,6,7,8,9]
n = 9

if search(list,n):
    print('Found', pos)
else:
    print('Not Found')
    
    
