from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
# Make a new window variable, window = Tk()
window = Tk()
# Hide the window using the window's .withdraw() method
window.withdraw()
# 1. Create a variable to hold the user's score. Set it equal to zero.
Score = 20
# ASK A QUESTION AND CHECK THE ANSWER
answer = simpledialog.askstring(title='question', prompt="What is the full name of the individual who invented Calculas")
    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct
if answer == 'Issac Newton':
    Score += 21
    #      // 4.  if the user's answer was correct, add one to their score 

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    answer1 = simpledialog.askstring(title='question1',prompt="How many continents exist?")

if answer1 == '7' :
    Score += 22
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    window.mainloop()
    # Run the window's .mainloop() method
