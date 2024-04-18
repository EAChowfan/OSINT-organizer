import tkinter as tk

root = tk.Tk()

root.geometry("1920x1080")
root.title("OSINT")

label = tk.Label(root, text = "OSINT Organizer", font =('Roboto', 18))
label.pack(pady = 12, padx = 10)
#textbox = tk.Text(root, font =('Roboto', 18))
#textbox.pack()

myentry = tk.Entry(root)
myentry.pack()

root.mainloop()