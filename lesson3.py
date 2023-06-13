import tkinter as tk
from tkinter import ttk
from gpiozero import LED



class Window(tk.Tk):
    def __init__(self,redLed):
        super().__init__()
        self.redLed=redLed
        self.title("視窗一")
        # self.geometry('380x400')
        self.resizable(False, False)
        s= ttk.Style()
        # print(s.theme_names())
        # print(s.theme_use())
        s.theme_use('clam')
        s.configure('Title.TLabel',font=("Helvetica", "16"))
        s.configure('LEDClose.TButton', foreground='blue',background='yellow',font=("Arial", 16),borderwidth=5,padding=(10,20))
        s.configure('LEDOpen.TButton', foreground='blue',background='yellow',font=("Arial", 16),borderwidth=5,padding=(10,20))
        title_label = ttk.Label(self, text="LED控制器",style='Title.TLabel')
        print(title_label.winfo_class())
        
        title_label.pack(pady=25, padx=100)
        print(s.layout('TButton'))
        self.led_btn = ttk.Button(
        self,text="LED 開",style='LEDClose.TButton',command=self.user_click)
        
        self.led_btn.pack(pady=(10,50))
        
    
    def user_click(self):
        print(self.state)
        self.state = not self.state
        if self.state:
            self.led_btn.configure(text='LED 關')
            self.led_btn.configure(style='LEDOpen.TButton')
            self.redLed.on()
        else:
            self.led_btn.configure(text='LED 開')
            self.led_btn.configure(style='LEDClose.TButton')
            self.redLed.off()
        print(self.state)


if __name__ == "__main__":
    led = LED(23)
    led.off()
    window = Window(led)
    window.mainloop()
