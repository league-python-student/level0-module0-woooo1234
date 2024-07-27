from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
var = random.randint(0, 3)
print(var)
    # 2. Print your variable to the console

    # 3. Get the user to enter something that they think is awesome
answer1 = simpledialog.askstring(title='question1',prompt="Enter something you think is awesome")
    # 4. If your variable is  0
if var == 0:
    simpledialog.messagebox.showinfo('question','That is awesome')
        # -- tell the user whatever they entered is awesome!
if var == 1:
    simpledialog.messagebox.showinfo('question', 'That is ok')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
if var == 2:
    simpledialog.messagebox.showinfo('question', 'That is boring')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
if var == 3
    simpledialog.messagebox.showinfo('question', 'Sensational')
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    window.mainloop()
    # Run the window's .mainloop() method
