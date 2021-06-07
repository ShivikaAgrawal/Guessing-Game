#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Create a new window and set the dimensions
window = tk.Tk()
window.geometry("600x400")
 
# Set the background color of the window
window.config(bg="#065569")
 
window.resizable(width=False,height=False)
 
# Window's Title
window.title('Number Guessing Game')


# In[6]:


#Create random variable
TARGET = random.randint(0, 1000)
RETRIES = 0


# In[7]:


def update_result(text):
    result.configure(text=text)
 
# Creating a game
def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 1000)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 1000")


# In[8]:


def play_game():
    global RETRIES
 
    choice = int(number_form.get())
     
    if choice != TARGET:
        RETRIES += 1
     
        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "The required number lies between 0 and {}".format(result)
        else:
            hint = "The required number lies between {} and 1000".format(choice)
        result += "\n\nHINT :\n" + hint
     
    else:
        result = "You guessed the correct number after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"
     
    update_result(result)


# In[9]:


# Heading of our game
title = tk.Label(window,text="Guessing Game",font=("Arial",24),fg="#fffcbd",bg="#065569")
 
# Result and hints of our game
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
 
# Play Button
play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=new_game)
 
# Guess Button
guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=play_game)
 
# Exit Button
exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)
 


# In[10]:


# Entry Fields
guessed_number = tk.StringVar()
number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)


# In[11]:


# Place the labels
 
title.place(x=170, y=50)
result.place(x=180, y=210)
 
# Place the buttons
exit_button.place(x=300,y=320)
guess_button.place(x=350, y=147) 
play_button.place(x=170, y=320)
 
# Place the entry field
number_form.place(x=180, y=150)


# In[12]:


# Start the window
window.mainloop()


# In[ ]:




