import tkinter as tk
display = tk.Tk()
display.geometry('650x700')
#Functions
def doButton_2():
    frame_5.tkraise()
#Frame_5
frame_5 = tk.Frame(display,bg='indianred1')
frame_5.place(x=0, y=0, relwidth=1, relheight=1)

#Frame_4
frame_4 = tk.Frame(display,bg='indianred1')
frame_4.place(x=0, y=0, relwidth=1, relheight=1)

#labels in frame 4
label_1 = tk.Label(frame_4,text="Question variable will go here\nnext line",
                   borderwidth=1, relief='solid',bg='deep sky blue',
                   font=('Times New Roman', '20', 'bold'))
label_1.place(x=0,y=0,relwidth=1,relheight=.15)
label_2 = tk.Label(frame_4,text='A.',bg='indianred1',
                   font=('Arial','16'))
label_2.place(rely=.25,relx=.05,relheight=.05, anchor='w')
label_3 = tk.Label(frame_4,text='B.',bg='indianred1',
                   font=('Arial','16'))
label_3.place(rely=.35,relx=.05,relheight=.05, anchor='w')
label_4 = tk.Label(frame_4,text='C.',bg='indianred1',
                   font=('Arial','16'))
label_4.place(rely=.45,relx=.05,relheight=.05, anchor='w')
label_5 = tk.Label(frame_4,text='D.',bg='indianred1',
                   font=('Arial','16'))
label_5.place(rely=.55,relx=.05,relheight=.05, anchor='w')
#labels in frame 5
label_6 = tk.Label(frame_5,text="Question variable will go here\nnext line",
                   borderwidth=1, relief='solid',bg='deep sky blue',
                   font=('Times New Roman', '20', 'bold'))
label_6.place(x=0,y=0,relwidth=1,relheight=.15)
label_7 = tk.Label(frame_5,text='A.',bg='indianred1',
                   font=('Arial','16'))
label_7.place(rely=.25,relx=.05,relheight=.05, anchor='w')
label_8 = tk.Label(frame_5,text='B.',bg='indianred1',
                   font=('Arial','16'))
label_8.place(rely=.35,relx=.05,relheight=.05, anchor='w')
label_9 = tk.Label(frame_5,text='C.',bg='indianred1',
                   font=('Arial','16'))
label_9.place(rely=.45,relx=.05,relheight=.05, anchor='w')
label_10 = tk.Label(frame_5,text='D.',bg='indianred1',
                   font=('Arial','16'))
label_10.place(rely=.55,relx=.05,relheight=.05, anchor='w')
label_11 = tk.Label(frame_5,text='E.',bg='indianred1',
                   font=('Arial','16'))
label_11.place(rely=.65,relx=.05,relheight=.05, anchor='w')


#radio buttons in frame 4
radioVar = tk.IntVar()
radioVar.set(0)
radio_1 = tk.Radiobutton(frame_4)
radio_1.config(text="optionvar", variable=radioVar, value=1,
               bg='indianred1', font=('Arial', '16'))
radio_2 = tk.Radiobutton(frame_4)
radio_2.config(text="optionvar", variable=radioVar, value=2,
               bg='indianred1', font=('Arial', '16'))
radio_3 = tk.Radiobutton(frame_4)
radio_3.config(text="optionvar", variable=radioVar, value=3,
               bg='indianred1', font=('Arial', '16'))
radio_4 = tk.Radiobutton(frame_4)
radio_4.config(text="optionvar", variable=radioVar, value=4,
               bg='indianred1', font=('Arial', '16'))
radio_1.place(rely = .25,relx= .1, relheight = .05, anchor = 'w')
radio_2.place(rely = .35,relx= .1, relheight = .05, anchor = 'w')
radio_3.place(rely = .45,relx= .1, relheight = .05, anchor = 'w')
radio_4.place(rely = .55,relx= .1, relheight = .05, anchor = 'w')

#radio buttons in frame 5
radioVar1 = tk.IntVar()
radioVar1.set(0)
radio_1 = tk.Radiobutton(frame_5)
radio_1.config(text="optionvar", variable=radioVar1, value=1,
               bg='indianred1', font=('Arial', '16'))
radio_2 = tk.Radiobutton(frame_5)
radio_2.config(text="optionvar", variable=radioVar1, value=2,
               bg='indianred1', font=('Arial', '16'))
radio_3 = tk.Radiobutton(frame_5)
radio_3.config(text="optionvar", variable=radioVar1, value=3,
               bg='indianred1', font=('Arial', '16'))
radio_4 = tk.Radiobutton(frame_5)
radio_4.config(text="optionvar", variable=radioVar1, value=4,
               bg='indianred1', font=('Arial', '16'))
radio_5 = tk.Radiobutton(frame_5)
radio_5.config(text="optionvar", variable=radioVar1, value=5,
               bg='indianred1', font=('Arial', '16'))
radio_1.place(rely = .25,relx= .1, relheight = .05, anchor = 'w')
radio_2.place(rely = .35,relx= .1, relheight = .05, anchor = 'w')
radio_3.place(rely = .45,relx= .1, relheight = .05, anchor = 'w')
radio_4.place(rely = .55,relx= .1, relheight = .05, anchor = 'w')
radio_5.place(rely = .65,relx= .1, relheight = .05, anchor = 'w')
#Buttons
button_1 = tk.Button(frame_4, text='Next', bg='limegreen',
                     font=('Arial','16'), width=7, command=doButton_2)
button_1.place(rely = .7, relx= .8)
button_2 = tk.Button(frame_5, text='Next', bg='limegreen',
                     font=('Arial','16'), width=7)
button_2.place(rely = .7, relx= .8)

display.mainloop()
