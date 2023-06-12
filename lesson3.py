import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GUI')
        # self.geometry('380x400')
        self.resizable(False,False)
        title_label = tk.Label(self,text="LED控制器",font=('Helvetica','16'))
        title_label.pack(pady=25,padx=100)
        
        led_btn = tk.Button(self,text="LED 開",font=('Helvetica','16'),padx=20,pady=20)
        led_btn.pack()

if __name__ == "__main__":
    window = Window()
    window.mainloop()