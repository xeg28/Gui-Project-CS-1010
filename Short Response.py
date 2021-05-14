import tkinter as tk

root = tk.Tk()
root.title("Short Response")
root.geometry("650x700")
root.configure(bg='red')
# Frames
frame_5= tk.Frame(root, bg='indianred1')
frame_5.place(x=0,y=0,relwidth=1, relheight=1)
# Labels and text boxes
txtBox1= tk.Entry(frame_5,font=('Raleway', '12'))
txtBox1.tag_configure('center', justfy='center', wrap='word')
txtBox1.insert('1.0','Question Variable will go here')
txtBox1.config(state='disabled',borderwidth=1,
               relief='solid')
txtBox1.tag_add('center','1.0','end')
txtBox1.place(relx =.05, rely=.11, relheight=.10, relwidth=.9)
Label_1 = tk.Label(frame_5,text= "Type your question in the box.", relief='solid',
                      borderwidth = 1, bg='deep sky blue', 
                      font=('Times New Roman', '24', 'bold'))
Label_1.place(x=0,y=0,relwidth=1, relheight=.08)

Label_2 = tk.Label(frame_5, text=("Type your answer here."),
                   font=('arial', 16), bg='indianred1')
Label_2.place(relx=.075,rely=.25)

answer = tk.Entry(frame_5)
answer.place(relx=.08,rely=.31)

button_2 = tk.Button(frame_5, text='Next', bg='limegreen',
                     font=('Arial','16'), width=7)
button_2.place(rely = .8, relx= .8)
root.mainloop()
