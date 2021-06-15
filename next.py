# import tkinter modules
from tkinter import *
from tkinter import messagebox

# configuration of the window
window = Tk()
window.title("Account Balance")
window.geometry("400x300")
window.config(bg="Yellow")
# label and entry for the amount needed
top_label = Label(window, text="Please enter your amount below: ", bg="Grey", fg="light green")
top_label.place(x=84, y=10)
input_label = Entry(window)
input_label.place(x=110, y=70)


# functions for the tkinter window to work
def qualify():
    funds = input_label.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror(" Declined ", "Insufficient funds.")
        else:
            messagebox.showinfo("Congratulations", "You qualify for the trip to Malaysia")
    except ValueError:
        messagebox.showerror("Error", "Please insert a valid number.")


def exit_program():
    messagebox.showinfo("GOING SO SOON ?", "Are you sure you want to exit?")
    window.destroy()


# buttons to call the function and exit
qualify_btn = Button(window, text="Check Qualification", command=qualify)
qualify_btn.place(x=115, y=170)
exit_btn = Button(window, text="Exit", bg="red", fg="white", command=exit_program)
exit_btn.place(x=165, y=260)
window.mainloop()