
import tkinter as tk
import random
import math

DICE_SIZE = 120
PIP_RADIUS = 8
BASE_FRAMES = 20

PIPS = {
    1: [(0.5, 0.5)],
    2: [(0.25, 0.25), (0.75, 0.75)],
    3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
    4: [(0.25, 0.25), (0.75, 0.25),
        (0.25, 0.75), (0.75, 0.75)],
    5: [(0.25, 0.25), (0.75, 0.25),
        (0.5, 0.5),
        (0.25, 0.75), (0.75, 0.75)],
    6: [(0.25, 0.25), (0.25, 0.5), (0.25, 0.75),
        (0.75, 0.25), (0.75, 0.5), (0.75, 0.75)]
}

def ease_out(t):
    return 1 - (1 - t) ** 3

def draw_dice(value, offset_x=0, offset_y=0):
    canvas.delete("all")

    x0 = 20 + offset_x
    y0 = 20 + offset_y
    x1 = x0 + DICE_SIZE
    y1 = y0 + DICE_SIZE

    canvas.create_rectangle(
        x0, y0, x1, y1,
        fill="white",
        outline="black",
        width=3
    )

    for px, py in PIPS[value]:
        cx = x0 + px * DICE_SIZE
        cy = y0 + py * DICE_SIZE
        canvas.create_oval(
            cx - PIP_RADIUS, cy - PIP_RADIUS,
            cx + PIP_RADIUS, cy + PIP_RADIUS,
            fill="black"
        )

def roll_animation(frame=0, final_value=None):
    if frame == 0:
        roll_animation.final = random.randint(1, 6)

    t = frame / BASE_FRAMES
    speed_factor = 1 - ease_out(t)

    shake = int(15 * speed_factor)
    offset_x = random.randint(-shake, shake)
    offset_y = random.randint(-shake, shake)

    face = random.randint(1, 6)
    draw_dice(face, offset_x, offset_y)

    if frame < BASE_FRAMES:
        delay = int(25 + 120 * ease_out(t))
        root.after(delay, roll_animation, frame + 1)
    else:
        draw_dice(roll_animation.final, 0, 0)

def roll_dice():
    roll_animation(0)

root = tk.Tk()
root.title("Real Dice Roller")
root.geometry("220x290")
root.resizable(False, False)

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack(pady=15)

button = tk.Button(
    root,
    text="Roll Dice",
    font=("Arial", 14),
    command=roll_dice
)
button.pack()

draw_dice(1)

root.mainloop()