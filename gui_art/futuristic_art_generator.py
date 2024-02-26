import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Futuristic GUI Art")

# Set the window size
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=window_width, height=window_height, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)

# Create futuristic shapes and elements
# For instance, you can draw some rectangles with gradient colors
canvas.create_rectangle(50, 50, 200, 200, fill="#00bfff", outline="")
canvas.create_rectangle(300, 300, 500, 500, fill="#ff00ff", outline="")

# You can add some text
canvas.create_text(400, 100, text="FUTURISTIC", fill="white", font=("Helvetica", 30, "bold"))

# Create some lines or patterns
canvas.create_line(0, 0, window_width, window_height, fill="white", width=2)
canvas.create_line(window_width, 0, 0, window_height, fill="white", width=2)

# Create circles or ellipses
canvas.create_oval(100, 400, 300, 500, fill="#ff4500", outline="")

# Add some futuristic widgets
button = tk.Button(root, text="Press Me", bg="blue", fg="white")
button_window = canvas.create_window(600, 100, anchor="nw", window=button)

# Run the GUI event loop
root.mainloop()
