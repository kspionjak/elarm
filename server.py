import tkinter as tk
from tkinter import font as tkFont
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dorucak/')
def dorucak():
    def ok_exit():
        window.destroy()

    window = tk.Tk()
    window.title("Ema's Alarm!")
    window.attributes('-topmost', True)

    screen_width =  window.winfo_screenwidth()
    screen_height =  window.winfo_screenheight()

    window.geometry("560x400+%d+%d" % (screen_width/2-275, screen_height/2-125))
    # window.eval('tk::PlaceWindow . center')

    helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)

    btn = tk.Button(
            master=window,
            text="Ema dorucak!",
            font=helv36,
            fg="white",
            bg="#4583F4",
            width=20,
            height=10,
            command=ok_exit
        ).pack()

    window.mainloop()    
    
    return '''
        <html>
            <head>
                <title>Ema's Alarm!</title>
                <style type="text/css">
                    body {
                        font-family: Arial, Helvetica, sans-serif;
                        font-size: 18px;
                    }

                    h3 {
                        margin-top: 30px;
                        text-align: center;
                        color: #5E7686;
                    }
                </style>
            </head>
            <body>
                <h3>Ema je potvrdila da dolazi na dorucak!</h3>
            </body>
        </html>
    '''

@app.route('/rucak/')
def rucak():
    def ok_exit():
        window.destroy()

    window = tk.Tk()
    window.title("Ema's Alarm!")
    window.attributes('-topmost', True)

    screen_width =  window.winfo_screenwidth()
    screen_height =  window.winfo_screenheight()

    window.geometry("560x400+%d+%d" % (screen_width/2-275, screen_height/2-125))
    # window.eval('tk::PlaceWindow . center')

    helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)

    btn = tk.Button(
            master=window,
            text="Ema rucak!",
            font=helv36,
            fg="white",
            bg="#4583F4",
            width=20,
            height=10,
            command=ok_exit
        ).pack()

    window.mainloop()    
    return '''
        <html>
            <head>
                <title>Ema's Alarm!</title>
                <style type="text/css">
                    body {
                        font-family: Arial, Helvetica, sans-serif;
                        font-size: 18px;
                    }

                    h3 {
                        margin-top: 30px;
                        text-align: center;
                        color: #5E7686;
                    }
                </style>
            </head>
            <body>
                <h3>Ema je potvrdila da dolazi na rucak!</h3>
            </body>
        </html>
    '''

@app.route('/dodji/')
def dodji():
    def ok_exit():
        window.destroy()

    window = tk.Tk()
    window.title("Ema's Alarm!")
    window.attributes('-topmost', True)

    screen_width =  window.winfo_screenwidth()
    screen_height =  window.winfo_screenheight()

    window.geometry("560x400+%d+%d" % (screen_width/2-275, screen_height/2-125))
    # window.eval('tk::PlaceWindow . center')

    helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)

    btn = tk.Button(
            master=window,
            text="Ema dodji dolje!",
            font=helv36,
            fg="white",
            bg="#4583F4",
            width=20,
            height=10,
            command=ok_exit
        ).pack()

    window.mainloop()    
    return '''
        <html>
            <head>
                <title>Ema's Alarm!</title>
                <style type="text/css">
                    body {
                        font-family: Arial, Helvetica, sans-serif;
                        font-size: 18px;
                    }

                    h3 {
                        margin-top: 30px;
                        text-align: center;
                        color: #5E7686;
                    }
                </style>
            </head>
            <body>
                <h3>Ema je potvrdila da silazi dolje!</h3>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)