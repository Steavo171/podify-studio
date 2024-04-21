import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter")
        self.geometry("300x300")
        self.grid_columnconfigure((0,1),weight=1)

        self.checkboxframe = customtkinter.CTkFrame(self)
        self.checkboxframe.grid(row=1,column=0,padx=20,pady=20)
        self.button =  customtkinter.CTkButton(self,text="This is button",command=self.buttonFunc)
        self.button.grid(row=3,column=0,padx=20,pady=20,sticky="ew",columnspan=2)

        self.checkbox1 = customtkinter.CTkCheckBox(self.checkboxframe,text="check 1")
        self.checkbox1.grid(row=1,column=0,padx=20,pady=20)
        self.checkbox2 = customtkinter.CTkCheckBox(self.checkboxframe,text="check 2")
        self.checkbox2.grid(row=2,column=0,padx=20,pady=20)

        self.progress= customtkinter.CTkProgressBar(self, orientation="horizontal")
        self.progress.set(0)
        self.progress.grid(row=4,column=0,padx=20,pady=20,sticky="ew",columnspan=2)

    def buttonFunc(self):
        print("Hello")
        

 

app = App()
app.mainloop()