from screen import startup_screen
import customtkinter
from style import font

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Podify")
        self.font= font.FontSize("Montserrat")

        width= self.winfo_screenwidth()    
        height= self.winfo_screenheight()
        self.geometry(f"{width}x{height}")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        # customtkinter.set_default_color_theme("/Users/aniruddhagawali/Code/Mini Project/interface/style/theme.json")

        self.startup_screen = startup_screen.StartupScreeen(self,self.font)
        self.startup_screen.grid(row=0,column=0,padx=20,pady=20)



if __name__ == "__main__":
    app = App()
    app.mainloop()