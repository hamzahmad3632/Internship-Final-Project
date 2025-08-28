import tkinter as tk
import time
import math
import random

# Create window
root = tk.Tk()
root.title("Analog Clock")
root.geometry("400x400")
root.resizable(False, False)

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# Colors list
colors = ["white", "cyan", "yellow", "orange", "red", "lightgreen", "pink", "lightblue"]

# Function to update clock
def update_clock():
    canvas.delete("hands")
    canvas.delete("ring")  # Delete old ring so we can redraw with new color

    now = time.localtime()

    # Random color each second
    ring_color = random.choice(colors)
    date_color = random.choice(colors)
    day_color = random.choice(colors)

    # Draw outer ring
    canvas.create_oval(50, 50, 350, 350, outline=ring_color, width=4, tags="ring")

    # Hour marks
    for i in range(12):
        angle = math.radians(i * 30)
        x_outer = 200 + 130 * math.sin(angle)
        y_outer = 200 - 130 * math.cos(angle)
        x_inner = 200 + 120 * math.sin(angle)
        y_inner = 200 - 120 * math.cos(angle)
        canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill="white", width=3)

    # Get angles
    sec_angle = math.radians(now.tm_sec * 6)
    min_angle = math.radians(now.tm_min * 6 + now.tm_sec * 0.1)
    hr_angle = math.radians((now.tm_hour % 12) * 30 + now.tm_min * 0.5)

    # Second hand
    sec_x = 200 + 100 * math.sin(sec_angle)
    sec_y = 200 - 100 * math.cos(sec_angle)
    canvas.create_line(200, 200, sec_x, sec_y, fill="red", width=1, tags="hands")

    # Minute hand
    min_x = 200 + 90 * math.sin(min_angle)
    min_y = 200 - 90 * math.cos(min_angle)
    canvas.create_line(200, 200, min_x, min_y, fill="white", width=3, tags="hands")

    # Hour hand
    hr_x = 200 + 60 * math.sin(hr_angle)
    hr_y = 200 - 60 * math.cos(hr_angle)
    canvas.create_line(200, 200, hr_x, hr_y, fill="cyan", width=4, tags="hands")

    # Date (near 3 o’clock)
    date_text = time.strftime("%d", now)
    canvas.create_text(300, 200, text=date_text, fill=date_color, font=("Arial", 14, "bold"), tags="hands")

    # Day (beside 9 o’clock)
    day_text = time.strftime("%A", now)
    canvas.create_text(120, 200, text=day_text, fill=day_color, font=("Arial", 10, "bold"), tags="hands")

    root.after(1000, update_clock)

update_clock()
root.mainloop()
