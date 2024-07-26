import customtkinter as ctk

class Elam(ctk.CTk):
  def __init__(self):
    super().__init__()

    my_font = ctk.CTkFont(family="Tahoma", size=46, weight="bold")
    
    self.title("Elam's Alarm!")
    
    self.geometry('1024x768+400+400')
    # self.grid_columnconfigure((0, 1), weight=1)

    self.nameLabel = ctk.CTkLabel(self, 
                                  text="Ema!!!", 
                                  text_color="white", 
                                  fg_color="#01a6f8", 
                                  width=200,
                                  height=25,
                                  corner_radius=5,
                                  font=my_font)
    self.nameLabel.pack(pady=30)

app = Elam()
app.mainloop()