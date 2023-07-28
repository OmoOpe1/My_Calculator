import tkinter as tk


class Calculator:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        