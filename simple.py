import tkinter as tk

def ok_exit():
  window.destroy()

window = tk.Tk()
window.title("Ema's Alarm!")
window.geometry('520x300')
window.eval('tk::PlaceWindow . center')

btn = tk.Button(
        master=window,
        text="Dorucak!",
        fg="white",
        bg="blue",
        width=20,
        height=10,
        command=ok_exit
      ).pack()

window.mainloop()