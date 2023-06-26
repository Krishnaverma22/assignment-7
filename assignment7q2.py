import tkinter as tk
import calendar

def show_calendar():
    try:
        year = int(year_entry.get())
        cal = calendar.calendar(year)
        calendar_text.delete("1.0", tk.END)
        calendar_text.insert(tk.END, cal)
    except ValueError:
        calendar_text.delete("1.0", tk.END)
        calendar_text.insert(tk.END, "Invalid input")

# Create the main window
window = tk.Tk()
window.title("Calendar Application")

# Create and place the input label and entry field
year_label = tk.Label(window, text="Enter the year:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

# Create and place the show calendar button
show_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_button.pack()

# Create and place the text widget to display the calendar
calendar_text = tk.Text(window, height=20, width=50)
calendar_text.pack()

# Start the main event loop
window.mainloop()
