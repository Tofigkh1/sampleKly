import ctypes
import tkinter as tk

def is_caps_lock_on():

    return ctypes.windll.user32.GetKeyState(0x14) & 0xffff != 0

def toggle_caps_lock():

    ctypes.windll.user32.keybd_event(0x14, 0x45, 0x1, 0)
    ctypes.windll.user32.keybd_event(0x14, 0x45, 0x3, 0)
    update_caps_lock_label()

def update_caps_lock_label():
    caps_lock_label.config(text=f"Caps Lock: {'On' if is_caps_lock_on() else 'Off'}")


root = tk.Tk()
root.title("Caps Lock Control")


caps_lock_label = tk.Label(root, text=f"Caps Lock: {'On' if is_caps_lock_on() else 'Off'}", font=("Helvetica", 16))
caps_lock_label.pack(pady=20)


toggle_button = tk.Button(root, text="Toggle Caps Lock", command=toggle_caps_lock)
toggle_button.pack()


root.mainloop()
