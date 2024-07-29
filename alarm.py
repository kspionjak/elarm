import tkinter as tk
from tkinter import font as tkFont

def ok_exit():
  window.destroy()


window = tk.Tk()
window.title("Ema's Alarm!")

screen_width =  window.winfo_screenwidth()
screen_height =  window.winfo_screenheight()

window.geometry("560x400+%d+%d" % (screen_width/2-275, screen_height/2-125))
# window.eval('tk::PlaceWindow . center')

helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)

btn = tk.Button(
        master=window,
        text="Dorucak!",
        font=helv36,
        fg="white",
        bg="blue",
        width=20,
        height=10,
        command=ok_exit
      ).pack()

window.mainloop()
