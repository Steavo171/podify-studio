import customtkinter
from style import font

class StartupScreeen(customtkinter.CTkFrame):

    def __init__(self,master:customtkinter.CTk,font:font.FontSize):
        super().__init__(master)
        self.grid_columnconfigure((0),weight=1)
        self.grid_rowconfigure((0,1),weight=1)
        self.configure(fg_color="transparent")

        self.header = customtkinter.CTkLabel(self,text="Welcome to Podify",font=font.xl5)
        self.header.grid(row=0,column=0,padx=20,pady=20)

        self.button = customtkinter.CTkButton(self,text="Get Started",font=font.md,height=50)
        self.button.grid(row=1,column=0,padx=50,pady=50,sticky="nsew")