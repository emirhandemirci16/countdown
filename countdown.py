import tkinter as tk
import time
import math

def update_timer():
    global countdown, circle, first_iteration
    if countdown >= 0:
        if first_iteration:
            first_iteration = False
            window.after(50, update_timer)  # Adjust the initial delay to 200 milliseconds
        else:
            angle = 360 - (360 * countdown / total_time)
            canvas.delete(circle)
            circle = canvas.create_arc(50, 50, 150, 150, start=90, extent=angle, outline="blue", width=5)
            countdown_label.config(text=str(countdown))
            countdown -= 1
            window.after(1000, update_timer)
    elif countdown == -1:
        canvas.delete(circle)
        countdown_label.config(text="Time's up")

def start_countdown():
    global total_time, countdown, circle, first_iteration
    total_time = int(entry.get())
    countdown = total_time
    countdown_label.config(text=str(countdown))
    first_iteration = True
    window.after(50, update_timer)  # Start the first iteration with a 200-millisecond delay

window = tk.Tk()
window.title("Countdown Timer")

entry_label = tk.Label(window, text="Enter Countdown Time:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

start_button = tk.Button(window, text="Start Countdown", command=start_countdown)
start_button.pack()

canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

# Draw the initial circle
circle = canvas.create_arc(50, 50, 150, 150, start=90, extent=0, outline="blue", width=5)

# Create a label for the countdown
countdown_label = tk.Label(window, text="0", font=("Helvetica", 24))
countdown_label.pack()

first_iteration = True

window.mainloop()
