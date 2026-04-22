board = [' '] * 9


def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")
    print()


def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] == p for a,b,c in w)


def draw():
    return ' ' not in board


def move(pos, p):
    if 0 <= pos < 9 and board[pos] == ' ':
        board[pos] = p
        return True
    return False


def best():
    for p in ['O', 'X']:
        for i in range(9):
            if board[i] == ' ':
                board[i] = p
                if win(p):
                    board[i] = ' '
                    return i
                board[i] = ' '

    if board[4] == ' ':
        return 4

    for i in range(9):
        if board[i] == ' ':
            return i


while True:
    show()

    if win('X'):
        print("Player wins!")
        break
    if win('O'):
        print("Computer wins!")
        break
    if draw():
        print("Game Draw!")
        break

    pos = int(input("Enter position (1-9): ")) - 1
    if not move(pos, 'X'):
        print("Invalid move! Try again.\n")
        continue

    if win('X') or draw():
        continue

    c = best()
    board[c] = 'O'
    print("Computer chooses position:", c + 1)