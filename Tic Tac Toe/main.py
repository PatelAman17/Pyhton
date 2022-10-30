from multiprocessing.sharedctypes import Value
from re import X

def sum(a, b, c):
    return a+b+c

def win(x, y):
    wins = [[0,1,2],[0,4,8],[0,3,6],[1,4,8],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
    for win in wins:
        if(sum(x[win[0]], x[win[1]], x[win[2]]) == 3):
            print("X won the match")
            return 1
        if(sum(y[win[0]], y[win[1]], y[win[2]]) == 3):
            print("O won the match")
            return 0
    return -1


def printboard(x, y):
    zero = 'X' if x[0] else ('o' if y[0] else 0)
    one = 'X' if x[1] else ('o' if y[1] else 1)
    two = 'X' if x[2] else ('o' if y[2] else 2)
    three = 'X' if x[3] else ('o' if y[3] else 3)
    four = 'X' if x[4] else ('o' if y[4] else 4)
    five = 'X' if x[5] else ('o' if y[5] else 5)
    six = 'X' if x[6] else ('o' if y[6] else 6)
    seven = 'X' if x[7] else ('o' if y[7] else 7)
    eight = 'X' if x[8] else ('o' if y[8] else 8)
    
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")
    
if __name__ == "__main__":
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while(True):
        printboard(x, y)
        if(turn == 1):
            print("First X")
            Value = int(input("Please select the X box : "))
            x[Value] = 1
        else:
            print("First Y")
            Value = int(input("Please select the Y box : "))
            y[Value] = 1
            
        check = win(x, y)
        if(check != -1):
            print("Match Over")
            break
        turn = 1 - turn