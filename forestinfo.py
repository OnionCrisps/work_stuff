# Names: Gavin Harban, Philip Palacio, Raymond Singh, Jahmor Lopez
# Class: 3B
# Submission Date: 12.6.2023

# IDP INSTRUCTIONS: Create a tkinter program that requests five pieces of info from the user about a plant in the forest.
# Have a button titled Submit and also include the info displayed in a report.

import tkinter as tk

# Initialize Tkinter and set to root widget: ; configures and titles window

window = tk.Tk()
window.configure(bg='#f0bc97')
window.title('Plant Portfolio')

# Frames for question formatting. Allows the text to be set next to the entry widget
name_frame = tk.Frame(window)
name_frame.configure(bg='#f0bc97')

height_frame = tk.Frame(window)
height_frame.configure(bg='#f0bc97')

width_frame = tk.Frame(window)
width_frame.configure(bg='#f0bc97')

fertility_frame = tk.Frame(window)
fertility_frame.configure(bg='#f0bc97')

age_frame = tk.Frame(window)
age_frame.configure(bg='#f0bc97')

button_frame = tk.Frame(window)
button_frame.configure(bg='#f0bc97')

# Erases content on the frames/screen


def clear_frames():
    name_frame.pack_forget()
    height_frame.pack_forget()
    width_frame.pack_forget()
    fertility_frame.pack_forget()
    age_frame.pack_forget()
    button_frame.pack_forget()

# Displays the text from the input fields


    def display_text():
        name = name_entry.get()
        height = height_entry.get()
        width = width_entry.get()
        fertility = fertility_entry.get()
        age = age_entry.get()

        name_label.config(text=f"The name of the plant is: {name}", fg = 'black', bg ='#f0bc97', pady=10, font='bold')
        height_label.config(text=f"The height of the plant in meters is: {height}", fg = 'black', bg ='#f0bc97', font='bold')
        width_label.config(text=f"The width of the plant in meters is: {width}", fg = 'black', bg ='#f0bc97', pady=10, font='bold')
        fertility_label.config(text=f"Plant's reproduction: {fertility}", fg = 'black', bg ='#f0bc97', font='bold')
        age_label.config(text=f"The plant has been alive for: {age}", fg = 'black', bg ='#f0bc97', pady=10, font='bold')

    # Creates fresh labels to insert text into
    report_heading = tk.Label(window, text="REPORT", borderwidth=2, relief='solid', fg = 'black', bg='#baf097', font='bold', padx=2, pady=2)
    report_heading.pack()
    name_label = tk.Label(window)
    name_label.pack()
    height_label = tk.Label(window)
    height_label.pack()
    width_label = tk.Label(window)
    width_label.pack()
    fertility_label = tk.Label(window)
    fertility_label.pack()
    age_label = tk.Label(window)
    age_label.pack()

    # Calls the function to display text
    display_text()


# Question Labels and Entry Widgets with styling
name_question = tk.Label(name_frame, text="What is the name of the tree?: ", fg = 'white', bg ='#f0bc97', font='bold')
name_entry = tk.Entry(name_frame, bg = '#baf097', fg = 'black', font='bold')

name_question.pack(side="left")
name_entry.pack(side="left")

height_question = tk.Label(height_frame, text="What is the height of the tree in meters?: ", fg = 'white', bg ='#f0bc97', pady=10, font='bold')
height_entry = tk.Entry(height_frame, bg = '#baf097', fg = 'black', font='bold')

height_question.pack(side="left")
height_entry.pack(side="left")

width_question = tk.Label(width_frame, text="What is the width of the tree in meters?: ", fg = 'white', bg ='#f0bc97', font='bold')
width_entry = tk.Entry(width_frame, bg = '#baf097', fg = 'black', font='bold')

width_question.pack(side="left")
width_entry.pack(side="left")

fertility_question = tk.Label(fertility_frame, text="How is the plant fertilized? \nDoes it reproduce sexually, asexually, or some other form of reproduction like autogamy: ", fg = 'white', bg ='#f0bc97', pady=10, font='bold')
fertility_entry = tk.Entry(fertility_frame, bg = '#baf097', fg = 'black', font='bold')

fertility_question.pack(side="top")
fertility_entry.pack(side="bottom")

age_question = tk.Label(age_frame, text="How long has the tree been alive?: ", fg = 'white', bg ='#f0bc97', pady=10, font='bold')
age_entry = tk.Entry(age_frame, bg = '#baf097', fg = 'black', font='bold')

age_question.pack(side="left")
age_entry.pack(side="left")

# Submit button. The button clears the frame then displays the text under a REPORT header.
space = tk.Label(button_frame, text=' ',pady=20)
submit_button = tk.Button(button_frame, text="Submit", bg='GREEN', fg='white', font='bold',command=clear_frames)
submit_button.pack()

# Packs all the frames

name_frame.pack()
height_frame.pack()
width_frame.pack()
fertility_frame.pack()
age_frame.pack()
button_frame.pack()

# Calls the mainloop
window.mainloop()
