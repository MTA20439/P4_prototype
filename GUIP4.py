import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image

myColor1 = '#59D8CD'
myColor2 = '#2FEAC3' 

myColor3 = '#101C59'
myColor4 = '#16246A'

myColor5 = '#FF397F'
myColor6 = '#FFA85C'

myColor7 = '#E7BC3D'


class PrototypeGUI(tk.Tk):
    def __init__(self, *args, **kwargs):        #Function that creates window for prototype GUI
        tk.Tk.__init__(self, *args, **kwargs)
        self._frame = None
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):        #Function for switching frames
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()               #Destroys current window and creates a new one
        self._frame = new_frame
        self._frame.grid()
        #self._frame.pack()
        #self._frame.update()


    def quit(self):
        self.destroy()


class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, background=myColor3)

        self.chooseASong = tk.Label(self, text="CHOOSE A SONG!", fg="white", background=myColor1, padx="250", pady="10",font=("BELLABOO", 56))\
            .grid(row=0, column=0)

        vs = 5
        hs = 250
        fs = 25

        #tk.Label(self, text=" ", bg=myColor6).grid(row =1, column=0, pady="25")



        MainMenu.var = IntVar()
        MainMenu.var.set(0)



        def show1():
            MainMenu.var.set(1)
            MainMenu.var.get()
            print(MainMenu.var.get())

        def show2():
            MainMenu.var.set(2)
            MainMenu.var.get()
            print(MainMenu.var.get())

        def show3():
            MainMenu.var.set(3)
            MainMenu.var.get()
            print(MainMenu.var.get())

        def show4():
            MainMenu.var.set(4)
            MainMenu.var.get()
            print(MainMenu.var.get())



        MainMenu.CB1 = tk.Checkbutton(self, text="Song 1", font=("Tofino Pro Personal Con Md", fs))
        MainMenu.CB1.grid_propagate(False)
        MainMenu.CB1.configure(background=myColor3, fg="White", activebackground=myColor3, activeforeground="White",
                           selectcolor=myColor5, variable=MainMenu.var, onvalue = 1, command=show1)
        MainMenu.CB1.grid(row=1, column= 0, sticky="W", pady=vs, padx=hs)

        MainMenu.CB2 = tk.Checkbutton(self, text="Song 2", font=("Tofino Pro Personal Con Md", fs))
        MainMenu.CB2.configure(bg=myColor3, fg="White", activebackground=myColor3, activeforeground="White",
                           selectcolor=myColor5, variable=MainMenu.var, onvalue = 2, command=show2)
        MainMenu.CB2.grid(row=2, column= 0, sticky="W", pady=vs, padx=hs)

        MainMenu.CB3 = tk.Checkbutton(self, text="Twinkle, Twinkle, Little Star", font=("Tofino Pro Personal Con Md", fs))
        MainMenu.CB3.configure(bg=myColor3, fg="White", activebackground=myColor3, activeforeground="White",
                           selectcolor=myColor5, variable=MainMenu.var, onvalue = 3, command=show3)
        MainMenu.CB3.grid(row=3, column= 0, sticky="W", pady=vs, padx=hs)

        MainMenu.CB4 = tk.Checkbutton(self, text="Song 4", font=("Tofino Pro Personal Con Md", fs))
        MainMenu.CB4.configure(bg=myColor3, fg="White", activebackground=myColor3, activeforeground="White",
                           selectcolor=myColor5, variable=MainMenu.var, onvalue = 4, command=show4)
        MainMenu.CB4.grid(row=4, column= 0, sticky="W", pady=vs, padx=hs)

        self.starButtonCanvas = Canvas(self, highlightthickness=0, bg=myColor7, width=100, height=10)
        self.startButton = tk.Button(self, text="START", fg="white", bg=myColor5, borderwidth=2, relief=FLAT, padx=0)
        self.startButton.config(activebackground=myColor5, activeforeground="white", bd=0,
                                font=("Tofino Pro Personal Con Md", 26))
        # self.startButton.config(command=lambda: master.switch_frame(PlayFrame))
        # self.startButton.place(bordermode=INSIDE, relx=0.75, rely=0.5, anchor=CENTER)
        self.startButton.grid(row=4, column=0, sticky=E, ipadx=20, ipady=0, padx=120)
        # self.starButtonCanvas.grid(row=4, column=0, sticky=E)

        if (MainMenu.var.get() == 0):
            self.startButton.config(state=ACTIVE, command=lambda: master.switch_frame(PlayFrame))
        else:
            self.startButton.config(state=DISABLED)


        navInfoCanvas = Canvas(self, highlightthickness=0, bg=myColor3, width=960, height=720)
        navInfoCanvas.grid(row=6, column=0)
        navInfoImage = ImageTk.PhotoImage(file="NavigationInfo.png")
        navInfoCanvas.create_image(480, -42, image=navInfoImage)
        self.grid(row=6, column=0)
        navInfoCanvas.navInfoImage = navInfoImage


class PlayFrame(MainMenu):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, background=myColor3)

        if(self.var.get() == 1):

            self.nowPlayingLabel = tk.Label(self, text="NOW PLAYING", fg="white", background=myColor1, padx="300",pady="10",font=("BELLABOO", 56)).grid(row=0, column=0)

            self.nowPlayingLabel = tk.Label(self, text="Song 1", fg="white", background=myColor3, padx="0", pady="10", font=("BELLABOO", 45)).grid(row=1, column=0)

            self.nextButton = tk.Button(self, text="NEXT", fg="white", bg=myColor5, borderwidth=2, relief=FLAT, padx=25)
            self.nextButton.config(activebackground=myColor5, activeforeground="white", bd=0,
                                   font=("Tofino Pro Personal Con Md", 26))
            self.nextButton.place(relx=0.85, rely=0.92, anchor=CENTER)
            self.nextButton.config(command=lambda: master.switch_frame(EndFrame))

        elif(self.var.get() == 2):

            self.nowPlayingLabel = tk.Label(self, text="NOW PLAYING", fg="white", background=myColor1, padx="300",
                                            pady="10", font=("BELLABOO", 56)).grid(row=0, column=0)

            self.nowPlayingLabel = tk.Label(self, text="Song 2", fg="white", background=myColor3, padx="0", pady="10", font=("BELLABOO", 45)).grid(row=1, column=0)

            self.nextButton = tk.Button(self, text="NEXT", fg="white", bg=myColor5, borderwidth=2, relief=FLAT, padx=25)
            self.nextButton.config(activebackground=myColor5, activeforeground="white", bd=0,
                                   font=("Tofino Pro Personal Con Md", 26))
            self.nextButton.place(relx=0.85, rely=0.92, anchor=CENTER)
            self.nextButton.config(command=lambda: master.switch_frame(EndFrame))

        elif (self.var.get() == 3):

            self.nowPlayingLabel = tk.Label(self, text="NOW PLAYING", fg="white", background=myColor1, padx="300",
                                            pady="10", font=("BELLABOO", 56)).grid(row=0, column=0)

            self.nowPlayingLabel = tk.Label(self, text="Twinkle, Twinkle, Little Star", fg="white", background=myColor3, padx="0", pady="10", font=("BELLABOO", 45)).grid(row=1, column=0)

            self.nextButton = tk.Button(self, text="NEXT", fg="white", bg=myColor5, borderwidth=2, relief=FLAT, padx=25)
            self.nextButton.config(activebackground=myColor5, activeforeground="white", bd=0,
                                   font=("Tofino Pro Personal Con Md", 26))
            self.nextButton.place(relx=0.85, rely=0.92, anchor=CENTER)
            self.nextButton.config(command=lambda: master.switch_frame(EndFrame))

            twinkleCanvas = Canvas(self, highlightthickness=0, bg=myColor3, width=500, height=500)
            twinkleCanvas.grid(row=2, column=0)
            twinkleImage = ImageTk.PhotoImage(file="twinkle.png")
            twinkleCanvas.create_image(250, 220, image=twinkleImage)
            twinkleCanvas.navInfoImage = twinkleImage

        elif (self.var.get() == 4):

            self.nowPlayingLabel = tk.Label(self, text="NOW PLAYING", fg="white", background=myColor1, padx="300",
                                            pady="10", font=("BELLABOO", 56)).grid(row=0, column=0)

            self.nowPlayingLabel = tk.Label(self, text="Song 4", fg="white", background=myColor3, padx="0", pady="10", font=("BELLABOO", 45)).grid(row=1, column=0)

            self.nextButton = tk.Button(self, text="NEXT", fg="white", bg=myColor5, borderwidth=2, relief=FLAT, padx=25)
            self.nextButton.config(activebackground=myColor5, activeforeground="white", bd=0,
                                   font=("Tofino Pro Personal Con Md", 26))
            self.nextButton.place(relx=0.85, rely=0.92, anchor=CENTER)
            self.nextButton.config(command=lambda: master.switch_frame(EndFrame))

        else:
            self.nowPlayingLabel = tk.Label(self, text="NO SONG SELECTED", fg="white", background=myColor1, padx="300",pady="10",font=("BELLABOO", 56)).grid(row=0)

            self.backButton = tk.Button(self, text="BACK", fg="white", bg=myColor7, borderwidth=2, relief=FLAT, padx=25)
            self.backButton.config(activebackground=myColor5, activeforeground="white", bd=0, font=("Tofino Pro Personal Con Md", 26))
            self.backButton.grid(row=1, padx=0, pady=80)
            self.backButton.config(command=lambda: master.switch_frame(MainMenu))




class EndFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, background=myColor7)

        self.songEndedLabel = tk.Label(self, text="SONG ENDED", fg="white", background=myColor1, padx="315", pady="10", font=("BELLABOO", 56)).grid(row=0, column=0)
        self.nowPlayingLabel = tk.Label(self, text="Good Job!", fg="black", background=myColor7, padx="0", pady="30", font=("BELLABOO", 45)).grid(row=1, column=0)

        smileCanvas = Canvas(self, highlightthickness=0, bg=myColor7, width=500, height=500)
        smileCanvas.grid(row=2, column=0)
        smileImage = ImageTk.PhotoImage(file="smileb.png")
        smileCanvas.create_image(250, 220, image=smileImage)
        smileCanvas.navInfoImage = smileImage

        self.againButton = tk.Button(self, text="TRY AGAIN", fg="white", bg=myColor5, borderwidth=2, relief=FLAT, padx=25)
        self.againButton.config(activebackground=myColor5, activeforeground="white", bd=0, font=("Tofino Pro Personal Con Md", 26))
        self.againButton.place(relx=0.85, rely=0.88, anchor=CENTER)
        self.againButton.config(command=lambda: master.switch_frame(PlayFrame))

        self.newButton = tk.Button(self, text="NEW SONG", fg="white", bg=myColor5, borderwidth=2, relief=FLAT, padx=25)
        self.newButton.config(activebackground=myColor5, activeforeground="white", bd=0, font=("Tofino Pro Personal Con Md", 26))
        self.newButton.place(relx=0.15, rely=0.88, anchor=CENTER)
        self.newButton.config(command=lambda: master.switch_frame(MainMenu))


if __name__ == "__main__":

    GUI = PrototypeGUI()
    GUI.resvar = '960x720'
    GUI.config(bg=myColor3)
    GUI.geometry(GUI.resvar)
    GUI.resizable(0, 0)
    GUI.mainloop()