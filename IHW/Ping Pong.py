import tkinter as tk
import random

# Створення головного вікна
window = tk.Tk()
window.title("Ping-pong")

# Розміри вікна
WIDTH = 800
HEIGHT = 400

# Створення Canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Розміри ракеток і м'яча
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20

# Початкові координати ракеток
paddle1_x = 20
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

paddle2_x = WIDTH - 20 - PADDLE_WIDTH
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Швидкість
paddle_speed = 20
ball_speed = 10
ball_dx = ball_speed
ball_dy = ball_speed

# Рахунок
score1 = 0
score2 = 0

# Максимальний рахунок
MAX_SCORE = 1

# Стан гри
game_paused = False
game_over = False

# Ракетки
paddle1 = canvas.create_rectangle(paddle1_x, paddle1_y,
                                  paddle1_x + PADDLE_WIDTH, paddle1_y + PADDLE_HEIGHT, fill="white")
paddle2 = canvas.create_rectangle(paddle2_x, paddle2_y,
                                  paddle2_x + PADDLE_WIDTH, paddle2_y + PADDLE_HEIGHT, fill="white")

# М'яч
ball = canvas.create_oval(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2,
                          WIDTH // 2 + BALL_SIZE // 2, HEIGHT // 2 + BALL_SIZE // 2, fill="white")

# Рахунок
score_text = canvas.create_text(WIDTH // 2, 20, text="0 : 0",
                                font=("Arial", 24), fill="white")

# Функція перемикання паузи
def toggle_pause():
    global game_paused
    if game_over:
        return  # Не можна ставити на паузу, якщо гра завершена
    game_paused = not game_paused
    if game_paused:
        pause_button.config(text="Continue")
    else:
        pause_button.config(text="Pause")
        move_ball()

# Кнопка паузи
pause_button = tk.Button(window, text="Pause", command=toggle_pause)
pause_button.pack()

# Обмеження руху ракеток
def move_paddle(paddle, dy):
    if game_over:
        return
    paddle_pos = canvas.coords(paddle)
    if paddle_pos[1] + dy >= 0 and paddle_pos[3] + dy <= HEIGHT:
        canvas.move(paddle, 0, dy)

# Функції руху ракеток
def move_paddle1_up(event):
    move_paddle(paddle1, -paddle_speed)

def move_paddle1_down(event):
    move_paddle(paddle1, paddle_speed)

def move_paddle2_up(event):
    move_paddle(paddle2, -paddle_speed)

def move_paddle2_down(event):
    move_paddle(paddle2, paddle_speed)

# Прив'язка клавіш
window.bind("w", move_paddle1_up)
window.bind("s", move_paddle1_down)
window.bind("<Up>", move_paddle2_up)
window.bind("<Down>", move_paddle2_down)

# Рух м'яча та логіка гри
def move_ball():
    global ball_dx, ball_dy, score1, score2, game_over

    if game_paused or game_over:
        return

    # Рух м'яча
    canvas.move(ball, ball_dx, ball_dy)

    # Координати м'яча та ракеток
    ball_pos = canvas.coords(ball)
    paddle1_pos = canvas.coords(paddle1)
    paddle2_pos = canvas.coords(paddle2)

    # Відбивання від верхньої та нижньої меж
    if ball_pos[1] <= 0 or ball_pos[3] >= HEIGHT:
        ball_dy = -ball_dy

    # Відбивання від лівої ракетки
    if (ball_pos[0] <= paddle1_pos[2] and
        ball_pos[1] + BALL_SIZE // 2 >= paddle1_pos[1] and
        ball_pos[1] + BALL_SIZE // 2 <= paddle1_pos[3]):
        ball_dx = -ball_dx

    # Відбивання від правої ракетки
    if (ball_pos[2] >= paddle2_pos[0] and
        ball_pos[1] + BALL_SIZE // 2 >= paddle2_pos[1] and
        ball_pos[1] + BALL_SIZE // 2 <= paddle2_pos[3]):
        ball_dx = -ball_dx

    # Забитий гол ліворуч
    if ball_pos[0] <= 0:
        score2 += 1
        canvas.itemconfig(score_text, text=f"{score1} : {score2}")
        reset_ball()

    # Забитий гол праворуч
    elif ball_pos[2] >= WIDTH:
        score1 += 1
        canvas.itemconfig(score_text, text=f"{score1} : {score2}")
        reset_ball()

    # Перевірка завершення гри
    if score1 >= MAX_SCORE or score2 >= MAX_SCORE:
        game_over = True
        winner = "Лівий гравець" if score1 >= MAX_SCORE else "Правий гравець"
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"{winner} переміг!",
                           font=("Times new roman", 36), fill="white")
        return

    # Рекурсивний виклик функції
    window.after(30, move_ball)

def reset_ball():
    global ball_dx, ball_dy
    canvas.coords(ball, WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2,
                  WIDTH // 2 + BALL_SIZE // 2, HEIGHT // 2 + BALL_SIZE // 2)
    ball_dx = ball_speed * random.choice([-1, 1])
    ball_dy = ball_speed * random.choice([-1, 1])
    
# Запуск гри
move_ball()
window.mainloop()
