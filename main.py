import tkinter as tk
import threading
import time
from pynput.mouse import Button, Controller

class SimpleAutoClicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auto Clicker")
        self.root.geometry("400x300")
        self.root.configure(bg='white')
        
        # Suppress the deprecation warning
        import os
        os.environ['TK_SILENCE_DEPRECATION'] = '1'
        
        self.clicking = False
        self.mouse = Controller()
        
        self.setup_gui()
        
    def setup_gui(self):
        # Title
        title = tk.Label(self.root, text="AUTO CLICKER", 
                        font=("Helvetica", 18, "bold"), 
                        bg='white', fg='black')
        title.pack(pady=20)
        
        # Interval input section
        interval_frame = tk.Frame(self.root, bg='white')
        interval_frame.pack(pady=15)
        
        tk.Label(interval_frame, text="Click every", 
                font=("Helvetica", 12), bg='white', fg='black').pack(side="left")
        
        self.interval_var = tk.StringVar(value="1.0")
        self.interval_entry = tk.Entry(interval_frame, textvariable=self.interval_var, 
                                      width=6, font=("Helvetica", 12), 
                                      justify="center", relief="solid", bd=1)
        self.interval_entry.pack(side="left", padx=10)
        
        tk.Label(interval_frame, text="minutes", 
                font=("Helvetica", 12), bg='white', fg='black').pack(side="left")
        
        # Quick set buttons
        quick_frame = tk.Frame(self.root, bg='white')
        quick_frame.pack(pady=10)
        
        tk.Label(quick_frame, text="Quick set:", 
                font=("Helvetica", 10), bg='white', fg='gray').pack()
        
        button_row = tk.Frame(quick_frame, bg='white')
        button_row.pack(pady=5)
        
        quick_buttons = [
            ("30s", "0.5"),
            ("1m", "1.0"),
            ("2m", "2.0"),
            ("5m", "5.0")
        ]
        
        for text, value in quick_buttons:
            btn = tk.Button(button_row, text=text, 
                          command=lambda v=value: self.interval_var.set(v),
                          font=("Helvetica", 10), width=6, height=1,
                          relief="solid", bd=1, bg='lightgray')
            btn.pack(side="left", padx=5)
        
        # Control buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.start_btn = tk.Button(button_frame, text="START", 
                                  command=self.start_clicking,
                                  bg="green", fg="white", 
                                  font=("Arial", 12, "bold"),
                                  width=12, height=2)
        self.start_btn.pack(side="left", padx=10)
        
        self.stop_btn = tk.Button(button_frame, text="STOP", 
                                 command=self.stop_clicking,
                                 bg="red", fg="white", 
                                 font=("Arial", 12, "bold"),
                                 width=12, height=2,
                                 state="disabled")
        self.stop_btn.pack(side="left", padx=10)
        
        # Status
        self.status_label = tk.Label(self.root, text="Ready! Set interval and click START", 
                                    font=("Arial", 10), 
                                    wraplength=300)
        self.status_label.pack(pady=15)
        
    def start_clicking(self):
        try:
            interval_minutes = float(self.interval_var.get())
            if interval_minutes <= 0:
                self.status_label.config(text="Please enter a positive number!")
                return
        except ValueError:
            self.status_label.config(text="Please enter a valid number!")
            return
        
        # Convert minutes to seconds
        interval_seconds = interval_minutes * 60
        
        self.clicking = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.interval_entry.config(state="disabled")  # Disable editing while running
        
        self.status_label.config(text=f"Clicking every {interval_minutes} minutes at mouse location")
        
        # Start clicking in a separate thread
        self.click_thread = threading.Thread(target=self.click_worker, args=(interval_seconds,), daemon=True)
        self.click_thread.start()
        
        print(f"Started clicking every {interval_minutes} minutes ({interval_seconds} seconds)")
        
    def stop_clicking(self):
        self.clicking = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.interval_entry.config(state="normal")  # Re-enable editing
        self.status_label.config(text="Stopped clicking.")
        print("Stopped clicking")
        
    def click_worker(self, interval_seconds):
        """Worker thread that performs the actual clicking"""
        click_count = 0
        while self.clicking:
            # Click at current mouse position (don't move mouse)
            self.mouse.click(Button.left, 1)
            
            click_count += 1
            current_pos = self.mouse.position
            print(f"Click #{click_count} at current position {current_pos}")
            
            # Update status on main thread
            interval_minutes = interval_seconds / 60
            self.root.after(0, lambda: self.status_label.config(
                text=f"Clicked {click_count} times. Next in {interval_minutes:.1f} min..."))
            
            time.sleep(interval_seconds)
    
    def run(self):
        print("Auto Clicker started!")
        print("Instructions:")
        print("1. Position your mouse where you want clicks")
        print("2. Set interval in minutes (or use quick set buttons)")
        print("3. Click START (don't move mouse after starting)")
        print("4. Click STOP when done")
        
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleAutoClicker()
    app.run()