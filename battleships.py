board1=[]
board1a=[]
board2=[]
board2a=[]
finish=0
def print_board(board):
    print("-"*20)
    for i in range (5):
        for j in range (5):
            print("| "+board[i][j],end=' ')
        print("|"+"\n"+"-"*20)
    
def make_board():
    board=[]
    for i in range (10):
        board.append([])
        for j in range (10):
            board[i].append(' ')
    return board



def placing_ships(board):
    while(1):
        try:
            for i in range(4):
                loc = [int(item) for item in input("Enter the location of ship : ").split()]
                if board[loc[0]][loc[1]]!='O':
                    board[loc[0]][loc[1]]='O'
                    print_board(board)
                else:
                    print("Ship already placed!")
            break
        except:
            print('invalid input')

def attack(board,count,board_seen):
    while(1 or count!=3):
        try:
            loc_atk = [int(item) for item in input("Enter the location for attack : ").split()]
            atk=board[loc_atk[0]][loc_atk[1]]
            if (atk!='O'):
                print("missed!")
                board[loc_atk[0]][loc_atk[1]]='M' 
                board_seen[loc_atk[0]][loc_atk[1]]='M'
                break    
            else:
                board[loc_atk[0]][loc_atk[1]]='X'
                board_seen[loc_atk[0]][loc_atk[1]]='X'
                board_seen[loc_atk[0]][loc_atk[1]]='X'
                print_board(board)
                print_board(board_seen)
                count+=1

        except:
            print('invalid input')
    return count

def game_over(count):
        finish=0
        if (count==4):
            print('Game over')
            finish=False
        return finish

user1=input('username-')
count1=0
user2=input('username-')
count2=0
finish=True
board1=make_board()
board2=make_board()
board1a=board1.copy()
board2a=board2.copy()
print('board1\n')
print_board(board1)
print_board(board1a)
print('board2\n')
print_board(board1)
print('user 1 is placing ships...')
placing_ships(board1)
print('user 2 is placing ships...')
placing_ships(board2)
while(finish):
    print('user 1 is attacking...')
    c2=attack(board2,count2,board2a)
    print_board(board2)
    finish=game_over(c2)
    if (finish):
        break
    print('user 2 is attacking...')
    c1=attack(board1,count1,board1a)
    print_board(board1)
    finish=game_over(c1)
    if (finish):
        break


        