from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    name = simpledialog.askstring(title='Greeter', prompt="Do you know how to write code?")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if name == 'yes':

    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
