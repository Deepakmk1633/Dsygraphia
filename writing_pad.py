import tkinter as tk
import time
import csv

# Prepare the log file with a unique timestamp-based filename
filename = f"writing_data_{int(time.time())}.csv"
log_file = open(filename, 'w', newline='')
writer = csv.writer(log_file)
writer.writerow(["timestamp", "x", "y", "event"])

# Create the writing window
root = tk.Tk()
root.title("🖊️ Dysgraphia Writing Pad")

# Make the window full screen
root.attributes('-fullscreen', True)

canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

drawing = False

def start_draw(event):
    global drawing
    drawing = True
    writer.writerow([time.time(), event.x, event.y, "press"])

def draw(event):
    if drawing:
        canvas.create_oval(event.x, event.y, event.x + 1, event.y + 1, fill='black', width=1)
        writer.writerow([time.time(), event.x, event.y, "move"])

def stop_draw(event):
    global drawing
    drawing = False
    writer.writerow([time.time(), event.x, event.y, "release"])

def on_close():
    log_file.close()
    root.destroy()

def exit_program(event=None):
    log_file.close()
    root.destroy()

# Bind pen/mouse events
canvas.bind("<ButtonPress-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

# Pressing Escape closes the program immediately
root.bind("<Escape>", exit_program)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
