import matplotlib.pyplot as plt

N = 8

moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def count_onward_moves(x, y, board):
    count = 0
    for i in range(8):
        nx = x + moves_x[i]
        ny = y + moves_y[i]
        if is_valid(nx, ny, board):
            count += 1
    return count

def knight_tour(start_x, start_y):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    x, y = start_x, start_y
    board[x][y] = 0

    for step in range(1, N * N):
        best_deg = 9
        next_x, next_y = -1, -1

        for i in range(8):
            nx = x + moves_x[i]
            ny = y + moves_y[i]
            if is_valid(nx, ny, board):
                degree = count_onward_moves(nx, ny, board)
                if degree < best_deg:
                    best_deg = degree
                    next_x, next_y = nx, ny

        if next_x == -1:
            return False, board, x, y

        board[next_x][next_y] = step
        x, y = next_x, next_y

    return True, board, x, y


def is_closed_tour(start_x, start_y, end_x, end_y):
    for i in range(8):
        if end_x + moves_x[i] == start_x and end_y + moves_y[i] == start_y:
            return True
    return False

def visualize(board, start_x, start_y, end_x, end_y):
    x = []
    y = []
    for step in range(N * N):
        for i in range(N):
            for j in range(N):
                if board[i][j] == step:
                    x.append(j + 0.5)
                    y.append(i + 0.5)

    closed = is_closed_tour(start_x, start_y, end_x, end_y)
    tour_type = "CLOSED TOUR" if closed else "OPEN TOUR"

    plt.figure(figsize=(7, 7))

    for i in range(N):
        for j in range(N):
            color = "#eed39b" if (i + j) % 2 == 0 else "#b77a3a"
            plt.fill_between([j, j + 1], i, i + 1, color=color)

    plt.plot(x, y, marker="o", linestyle="-", color="black", markersize=6)

    for idx, (px, py) in enumerate(zip(x, y)):
        plt.text(px, py, str(idx), ha='center', va='center', fontsize=7, color="red")

    plt.text(x[0], y[0], "START", ha='center', va='bottom', fontsize=10, color="green", fontweight="bold")
    plt.text(x[-1], y[-1], "END", ha='center', va='top', fontsize=10, color="blue", fontweight="bold")

    if closed:
        plt.plot([x[-1], x[0]], [y[-1], y[0]], linestyle="--", color="green", linewidth=2)

    plt.xticks([])
    plt.yticks([])
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal')
    plt.title(f"Knight's Tour Path ({tour_type})")
    plt.show()


sx = int(input("Mulai dari baris (0-7): "))
sy = int(input("Mulai dari kolom (0-7): "))

success, board, ex, ey = knight_tour(sx, sy)

if success:
    closed = is_closed_tour(sx, sy, ex, ey)

    print("\nTour berhasil diselesaikan!")
    print("Tipe:", "CLOSED TOUR" if closed else "OPEN TOUR")
    print("\nBoard:")
    for row in board:
        print(row)

    visualize(board, sx, sy, ex, ey)
else:
    print("Tour gagal ditemukan dari posisi ini. Coba posisi start lain.")
