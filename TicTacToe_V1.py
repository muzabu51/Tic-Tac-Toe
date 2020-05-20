#tictactoe grid
pos=[0,1,2,3,4,5,6,7,8]
def print_table(li=pos):
    print()
    print(' {} | {} | {} '.format(li[0], li[1], li[2]))
    print('------------')
    print(' {} | {} | {} '.format(li[3], li[4], li[5]))
    print('------------')
    print(' {} | {} | {} '.format(li[6], li[7], li[8]))
    print()
    return li

#gameplay
## All possible combinations for winning
li=[]
def solution_pos(li):
    pt_p1=0
    pt_p2=0
    
    if li[0]==li[3]==li[6]=='O':
        print("Congratulations... 'O' won")
        return 0
    elif li[0]==li[3]==li[6]=='X':
        print("Congratulations... 'X' won")
        return 0
    elif li[0]==li[1]==li[2]=='X':
        print("Congratulations... 'X' won")
        return 0
    elif li[0]==li[1]==li[2]=='O':
        print("Congratulations... 'O' won")
        return 0
    elif li[0]==li[4]==li[8]=='O':
        print("Congratulations... 'O' won")
        return 0
    elif li[0]==li[4]==li[8]=='X':
        print("Congratulations... 'X' won")
        return 0
    elif li[1]==li[4]==li[7]=='O':
        print("Congratulations... 'O' won")
        return 0
    elif li[1]==li[4]==li[7]=='X':
        print("Congratulations... 'X' won")     
        return 0
    elif li[3]==li[4]==li[5]=='O':
        print("Congratulations... 'O' won")
        return 0
    elif li[3]==li[4]==li[5]=='X':
        print("Congratulations... 'X' won")
        return 0
    elif li[6]==li[4]==li[2]=='O':
        print("Congratulations... 'O' won")
        return 0
    elif li[6]==li[4]==li[2]=='X':
        print("Congratulations... 'X' won")             
        return 0
    elif li[2]==li[5]==li[8]=='O':
        print("Congratulations... 'O' won")
        return 0
    elif li[2]==li[5]==li[8]=='X':
        print("Congratulations... 'X' won")
        return 0
    elif li[6]==li[7]==li[8]=='O':
        print("Congratulations... 'O' won")
        return 0
    elif li[6]==li[7]==li[8]=='X':
        print("Congratulations... 'X' won")    
        return 0
    else:
        return 1

#input
def assign(flag=1):
    XO=('X','O')
    p1=1 
    p2=0
    pl=['0','1','2','3','4','5','6','7','8']
    p_in=0
    
    while flag and (p1 or p2):
        if p1==1:
            p_in=int(input("Player 1 choose position in 0-8 "))
            pl[p_in]=XO[0].upper()
            li=print_table(pl)
            p1=0
            p2=1
            flag=solution_pos(li)
        elif p2==1:
            p_in=int(input("Player 2 choose position in 0-8 "))
            pl[p_in]=XO[1].upper()
            li=print_table(pl)
            p2=0
            p1=1
            flag=solution_pos(li)
        else:
            p1=0
            p2=0
            break

print_table()

print("player 1 is X and Player 2 is O")

assign()

