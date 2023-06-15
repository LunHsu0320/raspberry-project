import tkinter as tk
from tkinter import ttk
from gpiozero import LED
import datasource

class LEDButton(ttk.Button):
    def __init__(self,master,led,**kwargs):
        super().__init__(master,**kwargs)
        self.led = led
        self.state= False
        self.configure(command=self.user_click)
        
        s= ttk.Style()
        s.theme_use('clam')        
        s.configure('LEDClose.TButton', foreground='blue',background='yellow',font=("Arial", 16),borderwidth=5,padding=(10,20))
        s.configure('LEDOpen.TButton', foreground='blue',background='yellow',font=("Arial", 16),borderwidth=5,padding=(10,20))
        
    def user_click(self):
        # print(self.state)
        self.state = not self.state
        if self.state:
            self.configure(text='LED 關')
            self.configure(style='LEDOpen.TButton')
            self.led.on()
        else:
            self.configure(text='LED 開')
            self.configure(style='LEDClose.TButton')
            self.led.off()
        print(self.state)    

class Window(tk.Tk):
    def __init__(self,redLed,**kwargs):
        '''
        @parmater redLed,是gpiozero.LED的實體
        '''
        super().__init__(**kwargs)
        # self.redLed=redLed           
        self.title("視窗一")
        # self.geometry('380x400')
        self.resizable(False, False)
        s= ttk.Style()
        # print(s.theme_names())
        # print(s.theme_use())
        s.theme_use('clam')
        s.configure('Title.TLabel',font=("Helvetica", "16"))
        
        title_label = ttk.Label(self, text="LED控制器",style='Title.TLabel')
        # print(title_label.winfo_class())
        
        title_label.pack(pady=25, padx=100)
        # print(s.layout('TButton'))
        
        self.led_btn = LEDButton(
        self,led=redLed,text="LED 開",style='LEDClose.TButton')
        
        self.led_btn.pack(pady=(10,50))
        
    
   


if __name__ == "__main__":
    conn = datasource.create_connection('iot.db')
    led = LED(23)
    led.off()
    window = Window(led)
    window.mainloop()
