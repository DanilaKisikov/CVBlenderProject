import tkinter as tk
import tkinter.font as tkFont
import src.main as main

def btn_command():
    image = image_text.get()
    video = video_text.get()
    angle = angle_text.get()
    size = size_text.get()
    name = name_text.get()
    figure = figure_text.get()
    color = color_text.get()
    main.main_function(image,video,size,color,figure,name,angle)
    

root = tk.Tk()

#setting title
root.title("CVBlender")
#setting window size
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

btn=tk.Button(root)
btn["anchor"] = "center"
btn["bg"] = "#ef1515"
ft = tkFont.Font(family='Times',size=14)
btn["font"] = ft
btn["fg"] = "#ffffff"
btn["justify"] = "center"
btn["text"] = "Start"
btn["relief"] = "groove"
btn.place(x=170,y=410,width=235,height=48)
btn["command"] = btn_command

image_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
image_label["font"] = ft
image_label["fg"] = "#333333"
image_label["justify"] = "center"
image_label["text"] = "Image"
image_label.place(x=90,y=20,width=70,height=25)

image_text=tk.Entry(root)
image_text["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
image_text["font"] = ft
image_text["fg"] = "#333333"
image_text["justify"] = "center"
image_text["text"] = ""
image_text.place(x=200,y=20,width=285,height=30)

video_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
video_label["font"] = ft
video_label["fg"] = "#333333"
video_label["justify"] = "center"
video_label["text"] = "Video"
video_label.place(x=90,y=70,width=70,height=25)

size_text=tk.Entry(root)
size_text["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
size_text["font"] = ft
size_text["fg"] = "#333333"
size_text["justify"] = "center"
size_text["text"] = ""
size_text.place(x=200,y=170,width=281,height=30)

angle_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
angle_label["font"] = ft
angle_label["fg"] = "#333333"
angle_label["justify"] = "center"
angle_label["text"] = "Angle"
angle_label.place(x=90,y=120,width=70,height=25)

angle_text=tk.Entry(root)
angle_text["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
angle_text["font"] = ft
angle_text["fg"] = "#333333"
angle_text["justify"] = "center"
angle_text.insert(0,"110")
angle_text.place(x=200,y=120,width=282,height=30)

size_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
size_label["font"] = ft
size_label["fg"] = "#333333"
size_label["justify"] = "center"
size_label["text"] = "Size"
size_label.place(x=90,y=170,width=70,height=25)

size_text=tk.Entry(root)
size_text["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
size_text["font"] = ft
size_text["fg"] = "#333333"
size_text["justify"] = "center"
size_text["text"] = ""
size_text.place(x=200,y=170,width=281,height=30)

video_text=tk.Entry(root)
video_text["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
video_text["font"] = ft
video_text["fg"] = "#333333"
video_text["justify"] = "center"
video_text["text"] = ""
video_text.place(x=200,y=70,width=284,height=30)

name_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
name_label["font"] = ft
name_label["fg"] = "#333333"
name_label["justify"] = "center"
name_label["text"] = "Name"
name_label.place(x=90,y=220,width=70,height=25)

name_text=tk.Entry(root)
name_text["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
name_text["font"] = ft
name_text["fg"] = "#333333"
name_text["justify"] = "center"
name_text["text"] = ""
name_text.place(x=200,y=220,width=281,height=30)

color_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
color_label["font"] = ft
color_label["fg"] = "#333333"
color_label["justify"] = "center"
color_label["text"] = "Color"
color_label.place(x=90,y=270,width=70,height=25)

color_text=tk.Entry(root)
color_text["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
color_text["font"] = ft
color_text["fg"] = "#333333"
color_text["justify"] = "center"
color_text.insert(0,"BLUE")
color_text.place(x=200,y=270,width=281,height=30)

figure_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
figure_label["font"] = ft
figure_label["fg"] = "#333333"
figure_label["justify"] = "center"
figure_label["text"] = "Figure"
figure_label.place(x=90,y=320,width=70,height=25)

figure_text=tk.Entry(root)
figure_text["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
figure_text["font"] = ft
figure_text["fg"] = "#333333"
figure_text["justify"] = "center"
figure_text.insert(0,"CUBE")
figure_text.place(x=200,y=320,width=281,height=30)

root.mainloop()