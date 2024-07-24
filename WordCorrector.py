from tkinter import *
from textblob import TextBlob

# Function to clear all the data from the entry boxes
def clrAll():
    word1_place.delete(0, END)
    word2_place.delete(0, END)
    mistake_count_label.config(text="Number of Mistakes: 0")

# Function to get the corrected word in the box and count mistakes
def crction():
    input_wrd = word1_place.get().strip()
    
    if not input_wrd:
        word2_place.delete(0, END)
        word2_place.insert(0, "No input provided")
        mistake_count_label.config(text="Number of Mistakes: 0")
        return
    
    blob_objct = TextBlob(input_wrd)
    crctd_word = str(blob_objct.correct())
    
    word2_place.delete(0, END)
    word2_place.insert(0, crctd_word)

    # Count the number of mistakes
    mistakes = 0
    for word in input_wrd.split():
        corrected_word = str(TextBlob(word).correct())
        if word != corrected_word:
            mistakes += 1
    
    mistake_count_label.config(text=f"Number of Mistakes: {mistakes}")

# Main code
if __name__ == "__main__":
    base = Tk()
    base.configure(background='light grey')
    base.title("Word Corrector")

    # Get screen width and height
    screen_width = base.winfo_screenwidth()
    screen_height = base.winfo_screenheight()

    # Set window width and height
    window_width = 500
    window_height = 250

    # Calculate position x and y coordinates
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    base.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create GUI components
    headlbl = Label(base, text='Welcome to Word Corrector', fg='white', bg="dark blue", font=('Helvetica', 16, 'bold'))
    lbl1 = Label(base, text="Input Word", fg='white', bg='dark blue', font=('Helvetica', 12, 'bold'))
    lbl2 = Label(base, text="Corrected Word", fg='white', bg='dark blue', font=('Helvetica', 12, 'bold'))
    mistake_count_label = Label(base, text="Number of Mistakes: 0", fg='white', bg='red', font=('Helvetica', 12))

    # Layout GUI components
    headlbl.grid(row=0, column=1, pady=10)
    lbl1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
    lbl2.grid(row=3, column=0, padx=10, pady=5, sticky=W)
    mistake_count_label.grid(row=5, column=1, pady=10)

    word1_place = Entry(base, width=25, font=('Helvetica', 12), borderwidth=2, relief=SUNKEN)
    word2_place = Entry(base, width=25, font=('Helvetica', 12), borderwidth=2, relief=SUNKEN)

    word1_place.grid(row=1, column=1, padx=10, pady=5, sticky=W)
    word2_place.grid(row=3, column=1, padx=10, pady=5, sticky=W)

    btn1 = Button(base, text="Correct The Word", bg="green", fg="white", font=('Helvetica', 12), command=crction)
    btn1.grid(row=1, column=2, padx=10, pady=5, sticky=W)

    btn2 = Button(base, text="Clear", bg="black", fg="white", font=('Helvetica', 12), command=clrAll)
    btn2.grid(row=3, column=2, padx=10, pady=5, sticky=W)

    base.mainloop()
