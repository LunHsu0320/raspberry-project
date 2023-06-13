import tkinter as tk
from tkinter import ttk



class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("視窗一")
        # self.geometry('380x400')
        self.resizable(False, False)
        s= ttk.Style()
        print(s.theme_names())
        print(s.theme_use())
        s.theme_use('clam')
        s.configure('Title.TLabel', foreground='blue',background='yellow',font=("Helvetica", "16"))
        s.configure('Led.TButton', foreground='blue',background='yellow',font=("Arial", 16),borderwidth=0,padding=(10,20))
        title_label = ttk.Label(self, text="LED控制器",style='Title.TLabel')
        print(title_label.winfo_class())
        
        title_label.pack(pady=25, padx=100)
        print(s.layout('TButton'))
        led_btn = ttk.Button(
            self, text="LED 開",style='Led.TButton',command=self.user_click)
        
        led_btn.pack(pady=(10,50))
    
    def user_click(self):
        print("user click")


if __name__ == "__main__":
    window = Window()
    window.mainloop()
