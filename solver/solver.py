import socket, time, re
from stockfish import Stockfish

port = "8164"
host = "localhost"
try:
    stockfish = Stockfish("./stockfish.android.armv8")
except:
    print("You need stockfish : https://stockfishchess.org/download/")
    exit(1)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
except:
    print('Failed')
    exit(1)

def SendAnswer(answer):
    s.send((answer + '\n').encode())

def SolveBoard(ignoredLine):
    recv_data = s.recv(1024)
    # Format data
    board = recv_data.decode("utf-8").splitlines()[ignoredLine:-3:2]
    board = re.sub("[1-8]", "", "/".join(board).replace('   ','.').replace('|', '').replace(' ', ''))

    # Fen converter
    fen = ""
    emptyCount = 0
    count = 0
    for square in board:
        if square == ".":
            emptyCount+=1
            if count == len(board)-1:
                fen += str(emptyCount)
        else:
            if emptyCount > 0:
                fen += str(emptyCount) + square
                emptyCount = 0
            else:
                fen += square
        count+=1
    fen += " w - - 0 1"

    stockfish.set_fen_position(fen)
    best_move = stockfish.get_best_move()
    SendAnswer(best_move)


print("Waiting for slow writing to end...")
time.sleep(6.5)
SendAnswer("Vincent")
print("Name sent")
print("Waiting again for slow writing to end...")
time.sleep(7)
print("Solving board #1...")
SolveBoard(9)
print("Solving board #2...")
SolveBoard(2)
print("Solving board #3...")
SolveBoard(2)
print("All boards are now solved!")
print("Waiting for flag.....")
print("Waiting again*2 for slow writing to end...")
time.sleep(13)
print(s.recv(1024).decode("utf-8"))

