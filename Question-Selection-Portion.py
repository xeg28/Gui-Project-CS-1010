import tkinter as tk
display = tk.Tk()
display.geometry('650x700')
display.config(bg='indianred1')
#Frame_1
def doButton_1():
    print('worked')

#Frame 2
frame_2 = tk.Frame(display,bg='indianred1')
frame_2.place(x=0, y=0, relwidth=1, relheight=1)
#Text of label_1 will change
label_1 = tk.Label(frame_2,text ='Customize Question #',
                   borderwidth=1, relief= 'solid',bg='deep sky blue',
                   font=('Times New Roman', '24', 'bold'))
label_1.place(x=0,y=0,relwidth = 1, relheight = .08)
label_2 = tk.Label(frame_2,text = 'Type of Question', bg='indianred1',
                   relief='sunken', font=('Arial', '20', 'bold'))
label_2.place(rely=.125, relx=.32)
#radio buttons
radioVar = tk.IntVar()
radioVar.set(0)
radio_1 = tk.Radiobutton(frame_2)
radio_1.config(text="Multiple Choice Question (A-D)", variable=radioVar, value=1,
               bg='indianred1', font=('Arial', '16'))
radio_2 = tk.Radiobutton(frame_2)
radio_2.config(text="Multiple Choice Question (A-E)", variable=radioVar, value=2,
               bg='indianred1', font=('Arial', '16'))
radio_3 = tk.Radiobutton(frame_2)
radio_3.config(text="True or False", variable=radioVar, value=3,
               bg='indianred1', font=('Arial', '16'))
radio_4 = tk.Radiobutton(frame_2)
radio_4.config(text="Short Response", variable=radioVar, value=4,
               bg='indianred1', font=('Arial', '16'))
radio_1.place(rely = .25,relx= .25, relheight = .05, anchor = 'w')
radio_2.place(rely = .35,relx= .25, relheight = .05, anchor = 'w')
radio_3.place(rely = .45,relx= .25, relheight = .05, anchor = 'w')
radio_4.place(rely = .55,relx= .25, relheight = .05, anchor = 'w')
#Buttons
button_1 = tk.Button(frame_2, text='Next', bg='limegreen',
                     font=('Arial','16'), width=7, command=doButton_1)
button_1.place(rely = .8, relx= .8)
display.mainloop()
