from tkinter import *
import cv2
import numpy as np
from PIL import ImageGrab
import threading

window = Tk()
window.geometry("500x200+460+170")
window.resizable(0, 0)
window.configure(bg='#030818')

screen_size = (3000, 2000) #Scrren size needs to be adapted to fit your dispay
recording = threading.Event()

def recorder():
    print("recording started")
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 10.0 #FPS count needs to be modified to fit source 
    output = cv2.VideoWriter("Screen record.avi", fourcc, fps, screen_size)
    recording.set()
    while recording.is_set():
        img = ImageGrab.grab().resize(screen_size)
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        output.write(frame)
    output.release()
    cv2.destroyAllWindows()
    print("recording stopped")

def start_recording():
    if not recording.is_set():
        threading.Thread(target=recorder).start()

def stop_recording():
    recording.clear()

Label(window, text="OBS CLONE", fg="white",bg="#030818",font=("Helvetica", 23, "bold")).pack()
Button(window, text="Start Recording", command=start_recording, bd=0, bg="gray",fg="white",font=("Helvetica", 15, "bold")).place(x=170,y=60)
Button(window, text="Stop Recording", command=stop_recording, bd=0, bg="gray",fg="white",font=("Helvetica", 15, "bold")).place(x=170,y=110)

window.mainloop()