import customtkinter
from tkinter import font




class FontSize:
    def __init__(self, font=None):
        if font is None:
            font = "TkDefaultFont"
        self.font = font

        self.sm=customtkinter.CTkFont(font, 14)
        self.xs=customtkinter.CTkFont(font, 12)
        self.md=customtkinter.CTkFont(font, 16)
        self.lg=customtkinter.CTkFont(font, 18)
        self.xl=customtkinter.CTkFont(font, 20)
        self.xl2=customtkinter.CTkFont(font, 24)
        self.xl3=customtkinter.CTkFont(font, 30)
        self.xl4=customtkinter.CTkFont(font, 36)
        self.xl5=customtkinter.CTkFont(font, 48)
        self.xl6=customtkinter.CTkFont(font, 60)
        self.xl7=customtkinter.CTkFont(font, 72)
        self.xl8=customtkinter.CTkFont(font, 96)
        self.xl9=customtkinter.CTkFont(font, 128)




    